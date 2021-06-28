from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import STATS_COLUMN_NAME
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import TOTALS_COLUMN_NAME


def create_summary_table_from_names_and_values_lists(
        names: list,
        values: list) \
        -> DataFrame:
    summary_table_dictionary = \
        {
            STATS_COLUMN_NAME: names,
            TOTALS_COLUMN_NAME: values
        }

    summary_table = \
        DataFrame.from_dict(
            data=summary_table_dictionary)

    return \
        summary_table
