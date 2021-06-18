from nf_common_source.code.services.dataframe_service.dataframe_mergers import left_merge_dataframes
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from pandas import DataFrame

from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_processes.model_depths.model_depths_constants import \
    PROVIDER_COLUMN_NAME, DEPENDENT_COLUMN_NAME, SOURCE_NAME_COLUMN_NAME, TARGET_NAME_COLUMN_NAME


def generate_dependency_graph_input_table(
        ea_full_dependencies_dataframe: DataFrame,
        ea_classifiers_dataframe: DataFrame) \
        -> DataFrame:
    full_dependencies_table_with_source_name_column = \
        __add_source_name_to_input_table(
            ea_full_dependencies_dataframe=ea_full_dependencies_dataframe,
            ea_classifiers_dataframe=ea_classifiers_dataframe)

    uniclass_visualisation_input_table = \
        __add_target_name_column_to_input_table(
            table_with_source_name_column=full_dependencies_table_with_source_name_column,
            ea_classifiers_dataframe=ea_classifiers_dataframe)

    return \
        uniclass_visualisation_input_table


def __add_source_name_to_input_table(
        ea_full_dependencies_dataframe: DataFrame,
        ea_classifiers_dataframe: DataFrame) \
        -> DataFrame:
    table_with_source_name_column_names = {
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name: SOURCE_NAME_COLUMN_NAME
    }

    full_dependencies_table_with_source_name_column = \
        left_merge_dataframes(
            master_dataframe=ea_full_dependencies_dataframe,
            master_dataframe_key_columns=[PROVIDER_COLUMN_NAME],
            merge_suffixes=['1', '2'],
            foreign_key_dataframe=ea_classifiers_dataframe,
            foreign_key_dataframe_fk_columns=[NfColumnTypes.NF_UUIDS.column_name],
            foreign_key_dataframe_other_column_rename_dictionary=table_with_source_name_column_names
        )

    full_dependencies_table_with_source_name_column = \
        full_dependencies_table_with_source_name_column[[
            PROVIDER_COLUMN_NAME,
            DEPENDENT_COLUMN_NAME,
            SOURCE_NAME_COLUMN_NAME
        ]]
    return \
        full_dependencies_table_with_source_name_column


def __add_target_name_column_to_input_table(
        table_with_source_name_column: DataFrame,
        ea_classifiers_dataframe: DataFrame) \
        -> DataFrame:
    uniclass_visualisation_table_column_names = {
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name: TARGET_NAME_COLUMN_NAME
    }

    uniclass_data_visualisation_table = \
        left_merge_dataframes(
            master_dataframe=table_with_source_name_column,
            master_dataframe_key_columns=[PROVIDER_COLUMN_NAME],
            merge_suffixes=['1', '2'],
            foreign_key_dataframe=ea_classifiers_dataframe,
            foreign_key_dataframe_fk_columns=[NfColumnTypes.NF_UUIDS.column_name],
            foreign_key_dataframe_other_column_rename_dictionary=uniclass_visualisation_table_column_names
        )

    uniclass_data_visualisation_table = \
        uniclass_data_visualisation_table[[
            PROVIDER_COLUMN_NAME,
            DEPENDENT_COLUMN_NAME,
            SOURCE_NAME_COLUMN_NAME,
            TARGET_NAME_COLUMN_NAME
        ]]
    return \
        uniclass_data_visualisation_table
