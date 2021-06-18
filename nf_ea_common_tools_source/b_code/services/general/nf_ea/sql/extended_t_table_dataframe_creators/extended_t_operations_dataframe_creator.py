from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_collection_types import EaCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.sql.extended_t_table_dataframe_creators.common_extensions.nf_identity_extender import extend_with_identities


def create_extended_t_operation_dataframe(
        nf_ea_sql_universe,
        universe_key: str) \
        -> DataFrame:
    log_message(
        message='creating extended t_operation dataframe')

    t_operation_dataframe = \
        nf_ea_sql_universe.ea_tools_session_manager.ea_sql_stage_manager.ea_sql_universe_manager.get_ea_t_table_dataframe(
            ea_repository=nf_ea_sql_universe.ea_repository,
            ea_collection_type=EaCollectionTypes.T_OPERATION)

    extended_t_operation_dataframe = \
        t_operation_dataframe

    extended_t_operation_dataframe = \
        extend_with_identities(
            dataframe=extended_t_operation_dataframe,
            universe_key=universe_key,
            collection_type_name='extended_t_operations')

    return \
        extended_t_operation_dataframe
