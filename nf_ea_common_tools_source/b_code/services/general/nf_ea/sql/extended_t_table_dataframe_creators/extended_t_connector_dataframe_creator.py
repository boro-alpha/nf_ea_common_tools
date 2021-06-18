from nf_common_source.code.services.dataframe_service.dataframe_mergers import left_merge_dataframes
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.ea_t.ea_t_connector_column_types import EaTConnectorColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.ea_t.ea_t_object_column_types import EaTObjectColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.extended_t.extended_t_connector_column_types import ExtendedTConnectorColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.extended_t.extended_t_object_column_types import ExtendedTObjectColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_collection_types import EaCollectionTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_property_types import EaPropertyTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.sql.extended_t_table_dataframe_creators.common_extensions.nf_identity_extender import extend_with_identities
from nf_ea_common_tools_source.b_code.services.general.nf_ea.sql.extended_t_table_dataframe_creators.common_extensions.stereotypes_extender import extend_with_stereotypes_data


def create_extended_t_connector_dataframe(
        nf_ea_sql_universe,
        universe_key: str) \
        -> DataFrame:
    log_message(
        message='creating extended t_connector dataframe')

    t_connector_dataframe = \
        nf_ea_sql_universe.ea_tools_session_manager.ea_sql_stage_manager.ea_sql_universe_manager.get_ea_t_table_dataframe(
            ea_repository=nf_ea_sql_universe.ea_repository,
            ea_collection_type=EaCollectionTypes.T_CONNECTOR)

    extended_t_connector_dataframe = \
        extend_with_identities(
            dataframe=t_connector_dataframe,
            universe_key=universe_key,
            collection_type_name='extended_t_connectors')

    extended_t_object_dataframe = \
        nf_ea_sql_universe.get_extended_ea_t_table_dataframe(
            ea_collection_type=EaCollectionTypes.EXTENDED_T_OBJECT)

    extended_t_connector_dataframe = \
        __extend_with_object_data(
            extended_t_connector_dataframe=extended_t_connector_dataframe,
            extended_t_object_dataframe=extended_t_object_dataframe)

    extended_t_connector_dataframe = \
        extend_with_stereotypes_data(
            dataframe=extended_t_connector_dataframe,
            ea_guid_column_name=EaTConnectorColumnTypes.T_CONNECTOR_EA_GUIDS.nf_column_name,
            nf_ea_sql_universe=nf_ea_sql_universe,
            type_filter_text=EaPropertyTypes.CONNECTOR_PROPERTY.type_name)

    extended_t_connector_dataframe[ExtendedTConnectorColumnTypes.T_CONNECTOR_EA_HUMAN_READABLE_NAMES.column_name] = \
        extended_t_connector_dataframe[ExtendedTConnectorColumnTypes.START_T_OBJECT_NAMES.column_name] + \
        ' --' + extended_t_connector_dataframe[EaTConnectorColumnTypes.T_CONNECTOR_TYPES.nf_column_name] + '-> ' + \
        extended_t_connector_dataframe[ExtendedTConnectorColumnTypes.END_T_OBJECT_NAMES.column_name]

    log_message(
        message='created extended object dataframe')

    return \
        extended_t_connector_dataframe


def __extend_with_object_data(
        extended_t_connector_dataframe: DataFrame,
        extended_t_object_dataframe: DataFrame) \
        -> DataFrame:
    nf_uuids_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    extended_t_connector_dataframe = \
        left_merge_dataframes(
            master_dataframe=extended_t_connector_dataframe,
            master_dataframe_key_columns=[EaTConnectorColumnTypes.T_CONNECTOR_START_OBJECT_IDS.nf_column_name],
            merge_suffixes=['_connector', '_object'],
            foreign_key_dataframe=extended_t_object_dataframe,
            foreign_key_dataframe_fk_columns=[EaTObjectColumnTypes.T_OBJECT_IDS.nf_column_name],
            foreign_key_dataframe_other_column_rename_dictionary={
                EaTObjectColumnTypes.T_OBJECT_EA_GUIDS.nf_column_name: ExtendedTConnectorColumnTypes.START_T_OBJECT_EA_GUIDS.column_name,
                nf_uuids_column_name: 'start_t_object_nf_uuids',
                EaTObjectColumnTypes.T_OBJECT_NAMES.nf_column_name: ExtendedTConnectorColumnTypes.START_T_OBJECT_NAMES.column_name,
                ExtendedTObjectColumnTypes.T_OBJECT_PATHS.column_name: 'start_t_object_paths',
                't_object_package_ea_guids': 'start_t_object_package_ea_guids'
            })

    extended_t_connector_dataframe = \
        left_merge_dataframes(
            master_dataframe=extended_t_connector_dataframe,
            master_dataframe_key_columns=[EaTConnectorColumnTypes.T_CONNECTOR_END_OBJECT_IDS.nf_column_name],
            merge_suffixes=['_connector', '_object'],
            foreign_key_dataframe=extended_t_object_dataframe,
            foreign_key_dataframe_fk_columns=[EaTObjectColumnTypes.T_OBJECT_IDS.nf_column_name],
            foreign_key_dataframe_other_column_rename_dictionary={
                EaTObjectColumnTypes.T_OBJECT_EA_GUIDS.nf_column_name: ExtendedTConnectorColumnTypes.END_T_OBJECT_EA_GUIDS.column_name,
                nf_uuids_column_name: 'end_t_object_nf_uuids',
                EaTObjectColumnTypes.T_OBJECT_NAMES.nf_column_name: ExtendedTConnectorColumnTypes.END_T_OBJECT_NAMES.column_name,
                ExtendedTObjectColumnTypes.T_OBJECT_PATHS.column_name: 'end_t_object_paths',
                't_object_package_ea_guids': 'end_t_object_package_ea_guids'
            })

    return \
        extended_t_connector_dataframe
