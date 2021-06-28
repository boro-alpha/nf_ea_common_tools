import pandas
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import EA_OBJECT_TYPE_COLUMN_NAME
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import NF_UUIDS_COLUMN_NAME
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import TOTALS_COLUMN_NAME


def get_objects_by_type_summary_table(
        ea_classifiers: pandas.DataFrame) \
        -> pandas.DataFrame:
    objects_by_type_summary_proto_table = \
        ea_classifiers.groupby(
            EA_OBJECT_TYPE_COLUMN_NAME).count().reset_index()

    summary_table_filter_and_rename_dictionary = \
        {
            EA_OBJECT_TYPE_COLUMN_NAME: EA_OBJECT_TYPE_COLUMN_NAME,
            NF_UUIDS_COLUMN_NAME: TOTALS_COLUMN_NAME
        }

    objects_by_type_summary_table = \
        dataframe_filter_and_rename(
            dataframe=objects_by_type_summary_proto_table,
            filter_and_rename_dictionary=summary_table_filter_and_rename_dictionary)

    return \
        objects_by_type_summary_table
