from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.converters.ea_attributes_to_standard_attribute_table_converter import convert_ea_attributes_to_standard_attribute_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.converters.ea_connectors_to_standard_connector_table_converter import convert_ea_connectors_to_standard_connector_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.converters.ea_elements_to_standard_object_table_converter import convert_ea_elements_to_standard_object_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.converters.ea_stereotype_groups_to_standard_stereotype_group_table_converter import convert_ea_stereotype_groups_to_standard_stereotype_group_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.converters.ea_stereotypes_to_standard_stereotype_table_converter import convert_ea_stereotypes_to_standard_stereotype_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.converters.stereotype_usage_to_standard_stereotype_usage_table_converter import convert_stereotype_usage_to_standard_stereotype_usage_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.processes.human_readable_names_to_standard_tables_dictionary_adder import add_human_readable_names_to_standard_tables_dictionary


def convert_nf_ea_com_to_standard_tables_dictionary(
        nf_ea_com_universe: NfEaComUniverses) \
        -> dict:
    standard_tables_dictionary = \
        {}

    standard_tables_dictionary = \
        convert_ea_elements_to_standard_object_table(
            nf_ea_com_universe=nf_ea_com_universe,
            nf_ea_com_classifiers_collection_type=NfEaComCollectionTypes.EA_PACKAGES,
            standard_tables_dictionary=standard_tables_dictionary,
            input_object_table_name=NfEaComCollectionTypes.EA_PACKAGES.collection_name)

    standard_tables_dictionary = \
        convert_ea_elements_to_standard_object_table(
            nf_ea_com_universe=nf_ea_com_universe,
            nf_ea_com_classifiers_collection_type=NfEaComCollectionTypes.EA_CLASSIFIERS,
            standard_tables_dictionary=standard_tables_dictionary,
            input_object_table_name=NfEaComCollectionTypes.EA_CLASSIFIERS.collection_name)

    standard_tables_dictionary = \
        convert_ea_attributes_to_standard_attribute_table(
            nf_ea_com_universe=nf_ea_com_universe,
            standard_tables_dictionary=standard_tables_dictionary)

    standard_tables_dictionary = \
        convert_ea_connectors_to_standard_connector_table(
            nf_ea_com_universe=nf_ea_com_universe,
            standard_tables_dictionary=standard_tables_dictionary)

    standard_tables_dictionary = \
        convert_ea_stereotypes_to_standard_stereotype_table(
            nf_ea_com_universe=nf_ea_com_universe,
            standard_tables_dictionary=standard_tables_dictionary)

    standard_tables_dictionary = \
        convert_ea_stereotype_groups_to_standard_stereotype_group_table(
            nf_ea_com_universe=nf_ea_com_universe,
            standard_tables_dictionary=standard_tables_dictionary)

    standard_tables_dictionary = \
        convert_stereotype_usage_to_standard_stereotype_usage_table(
            nf_ea_com_universe=nf_ea_com_universe,
            standard_tables_dictionary=standard_tables_dictionary)

    standard_tables_dictionary = \
        add_human_readable_names_to_standard_tables_dictionary(
            standard_tables_dictionary=standard_tables_dictionary)

    standard_tables_dictionary = \
        __remove_null_values_from_dataframe_dictionary(
            dataframe_dictionary=standard_tables_dictionary)

    return \
        standard_tables_dictionary


def __remove_null_values_from_dataframe_dictionary(
        dataframe_dictionary: dict) \
        -> dict:
    for dataframe_name, dataframe in dataframe_dictionary.items():
        dataframe_dictionary[dataframe_name] = \
            __remove_null_values_from_dataframe(
                dataframe=dataframe)

    return \
        dataframe_dictionary


def __remove_null_values_from_dataframe(
        dataframe: DataFrame) \
        -> DataFrame:
    for column in dataframe.columns:
        dataframe[column].replace(
            to_replace=DEFAULT_NULL_VALUE,
            value='',
            inplace=True)

    return \
        dataframe
