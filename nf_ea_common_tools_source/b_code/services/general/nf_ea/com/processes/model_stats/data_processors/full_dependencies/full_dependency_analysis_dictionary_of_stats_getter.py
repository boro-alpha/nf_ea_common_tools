from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import FULL_DEPENDENCIES_SUMMARY_TABLE_NAME


def get_full_dependency_analysis_dictionary_of_stats(
        full_dependency_analysis_dictionary_of_stats_high_order_types: dict,
        full_dependency_analysis_dictionary_of_stats_first_class_relations: dict,
        full_dependency_analysis_summary_table: DataFrame,
        full_dependency_analysis_dictionary_of_stats_common: dict) \
        -> dict:
    high_relations_dictionary_of_stats = \
        dict(
            full_dependency_analysis_dictionary_of_stats_high_order_types,
            **full_dependency_analysis_dictionary_of_stats_first_class_relations)

    dataframes_to_dictionary = \
        {
            FULL_DEPENDENCIES_SUMMARY_TABLE_NAME: full_dependency_analysis_summary_table
        }

    temporary_dictionary = \
        dict(
            full_dependency_analysis_dictionary_of_stats_common,
            **dataframes_to_dictionary)

    full_dependency_analysis_dictionary_of_stats = \
        dict(
            temporary_dictionary,
            **high_relations_dictionary_of_stats)

    return \
        full_dependency_analysis_dictionary_of_stats
