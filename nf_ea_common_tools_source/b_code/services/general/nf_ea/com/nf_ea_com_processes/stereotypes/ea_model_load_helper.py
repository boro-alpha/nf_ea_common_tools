from nf_common_source.code.services.dataframe_service.dataframe_mergers import left_merge_dataframes
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes


def get_stereotype_usage_with_names_dataframe(
        nf_ea_com_dataframes_dictionary: dict) \
        -> DataFrame:
    nf_uuids_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    object_name_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name

    stereotypes = \
        nf_ea_com_dataframes_dictionary[NfEaComCollectionTypes.EA_STEREOTYPES]

    stereotype_usage = \
        nf_ea_com_dataframes_dictionary[NfEaComCollectionTypes.STEREOTYPE_USAGE]

    stereotype_usage_with_names = \
        left_merge_dataframes(
            master_dataframe=stereotype_usage,
            master_dataframe_key_columns=['stereotype_nf_uuids'],
            merge_suffixes=['_usage', '_stereotypes'],
            foreign_key_dataframe=stereotypes,
            foreign_key_dataframe_fk_columns=[nf_uuids_column_name],
            foreign_key_dataframe_other_column_rename_dictionary=
            {
                object_name_column_name: NfEaComColumnTypes.STEREOTYPE_NAMES.column_name
            })

    if stereotype_usage_with_names.shape[0] == 0:
        stereotype_usage_with_names[NfEaComColumnTypes.STEREOTYPE_NAMES.column_name] = ''

    return \
        stereotype_usage_with_names
