from numpy import NaN
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import PATHS_COLUMN_NAME
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import PATH_LEVEL_DEPTH_COLUMN_NAME


def get_paths_and_path_depths_table_from_path_list(
        path_list: list) \
        -> DataFrame:
    if len(path_list) == 0:
        paths_and_path_depths_table = \
            DataFrame(
                columns=[
                    PATHS_COLUMN_NAME,
                    PATH_LEVEL_DEPTH_COLUMN_NAME])

    else:
        paths_and_path_depths_table_dictionary = \
            {PATHS_COLUMN_NAME: path_list,
             PATH_LEVEL_DEPTH_COLUMN_NAME: NaN}

        paths_and_path_depths_table = \
            DataFrame.from_dict(
                paths_and_path_depths_table_dictionary)

        paths_and_path_depths_table[
            PATH_LEVEL_DEPTH_COLUMN_NAME] = \
            paths_and_path_depths_table[
                PATHS_COLUMN_NAME].str.len() - 1

    return \
        paths_and_path_depths_table
