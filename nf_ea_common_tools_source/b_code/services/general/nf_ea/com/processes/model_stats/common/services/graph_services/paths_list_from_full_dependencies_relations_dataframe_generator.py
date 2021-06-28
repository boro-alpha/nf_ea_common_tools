import pandas
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import PATHS_COLUMN_NAME
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import RELATION_TYPE_COLUMN_NAME


def generate_paths_list_from_full_dependencies_relations_dataframe(
        full_dependencies_relations_dataframe: pandas.DataFrame,
        relation_type: str) \
        -> list:
    series_of_paths = \
        full_dependencies_relations_dataframe[
            full_dependencies_relations_dataframe[
                RELATION_TYPE_COLUMN_NAME] ==
            relation_type][
            PATHS_COLUMN_NAME]

    paths_list = \
        pandas.Series.tolist(
            series_of_paths)

    return \
        paths_list
