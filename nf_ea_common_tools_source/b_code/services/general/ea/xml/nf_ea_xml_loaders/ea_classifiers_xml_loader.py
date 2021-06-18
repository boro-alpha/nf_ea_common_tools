from nf_ea_common_tools_source.b_code.services.general.ea.xml.nf_ea_xml_adders.ea_classifiers_xml_adder import add_ea_classifiers_to_xml_root_element
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_element_types import EaElementTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.maps.nf_uuids_to_ea_guids_mappings import NfUuidsToEaGuidsMappings
from pandas import DataFrame
from xml.etree.ElementTree import Element


def map_and_xml_load_ea_non_proxy_classifiers(
        ea_classifiers: DataFrame,
        start_ea_identifier: int,
        xml_root_element: Element,
        xml_element_for_classifiers: Element,
        stereotype_usage_with_names: DataFrame) \
        -> tuple:
    log_message(
        'Exporting non_proxy classifiers')

    type_column_name = \
        NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name

    ea_non_proxy_classifiers = \
        DataFrame(
            ea_classifiers.loc[ea_classifiers[type_column_name] != EaElementTypes.PROXY_CONNECTOR.type_name])

    xml_root_element, xml_element_for_classifiers = \
        __map_and_xml_load_ea_classifiers(
            ea_classifiers=ea_non_proxy_classifiers,
            start_ea_identifier=start_ea_identifier,
            xml_root_element=xml_root_element,
            xml_element_for_classifiers=xml_element_for_classifiers,
            proxy_load=False,
            stereotype_usage_with_names=stereotype_usage_with_names)

    return \
        xml_root_element, xml_element_for_classifiers


def map_and_xml_load_ea_proxy_classifiers(
        ea_classifiers: DataFrame,
        start_ea_identifier: int,
        xml_root_element: Element,
        xml_element_for_classifiers: Element,
        stereotype_usage_with_names: DataFrame) \
        -> tuple:
    log_message(
        'Exporting proxy classifiers')

    type_column_name = \
        NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name

    ea_proxy_classifiers = \
        DataFrame(
            ea_classifiers.loc[ea_classifiers[type_column_name] == EaElementTypes.PROXY_CONNECTOR.type_name])

    xml_root_element, xml_element_for_classifiers = \
        __map_and_xml_load_ea_classifiers(
            ea_classifiers=ea_proxy_classifiers,
            start_ea_identifier=start_ea_identifier,
            xml_root_element=xml_root_element,
            xml_element_for_classifiers=xml_element_for_classifiers,
            proxy_load=True,
            stereotype_usage_with_names=stereotype_usage_with_names)

    return \
        xml_root_element, xml_element_for_classifiers


def __map_and_xml_load_ea_classifiers(
        ea_classifiers: DataFrame,
        start_ea_identifier: int,
        xml_root_element: Element,
        xml_element_for_classifiers: Element,
        proxy_load: bool,
        stereotype_usage_with_names: DataFrame) \
        -> tuple:
    ea_classifiers = \
        ea_classifiers.fillna(
            DEFAULT_NULL_VALUE)

    __map_matched_ea_classifiers(
        ea_classifiers=ea_classifiers)

    xml_root_element, xml_element_for_classifiers = \
        __load_unmatched_ea_classifiers(
            ea_classifiers=ea_classifiers,
            start_ea_identifier=start_ea_identifier,
            xml_root_element=xml_root_element,
            xml_element_for_classifiers=xml_element_for_classifiers,
            proxy_load=proxy_load,
            stereotype_usage_with_names=stereotype_usage_with_names)

    return \
        xml_root_element, xml_element_for_classifiers


def __map_matched_ea_classifiers(
        ea_classifiers: DataFrame):
    NfUuidsToEaGuidsMappings.map_objects_from_dataframe(
        dataframe=ea_classifiers)


def __load_unmatched_ea_classifiers(
        ea_classifiers: DataFrame,
        start_ea_identifier: int,
        xml_root_element: Element,
        xml_element_for_classifiers: Element,
        proxy_load: bool,
        stereotype_usage_with_names: DataFrame) \
        -> tuple:
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    unmatched_ea_classifiers = \
        ea_classifiers.loc[ea_classifiers[ea_guids_column_name] == DEFAULT_NULL_VALUE]

    xml_root_element, xml_element_for_classifiers = \
        add_ea_classifiers_to_xml_root_element(
            ea_classifiers=unmatched_ea_classifiers,
            xml_root=xml_root_element,
            xml_element_for_classifiers=xml_element_for_classifiers,
            start_ea_identifier=start_ea_identifier,
            proxy_load=proxy_load,
            stereotype_usage_with_names=stereotype_usage_with_names)

    return \
        xml_root_element, xml_element_for_classifiers
