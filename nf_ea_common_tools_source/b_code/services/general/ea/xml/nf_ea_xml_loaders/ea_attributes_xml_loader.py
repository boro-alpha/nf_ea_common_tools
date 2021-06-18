from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.services.general.ea.xml.nf_ea_xml_adders.ea_attributes_xml_adder import \
    add_ea_attributes_to_xml_root_element
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.maps.nf_uuids_to_ea_guids_mappings import NfUuidsToEaGuidsMappings
from pandas import DataFrame
from xml.etree.ElementTree import Element


def map_and_xml_load_ea_attributes(
        ea_attributes: DataFrame,
        ea_classifiers: DataFrame,
        start_ea_identifier: int,
        xml_root_element: Element) \
        -> Element:
    log_message(
        'Exporting attributes')

    ea_attributes = \
        ea_attributes.fillna(
            DEFAULT_NULL_VALUE)

    __map_matched_ea_attributes(
        ea_attributes=ea_attributes)

    __load_unmatched_ea_attributes(
        ea_attributes=ea_attributes,
        ea_classifiers=ea_classifiers,
        start_ea_identifier=start_ea_identifier,
        xml_root_element=xml_root_element)

    return \
        xml_root_element


def __map_matched_ea_attributes(
        ea_attributes: DataFrame):
    NfUuidsToEaGuidsMappings.map_objects_from_dataframe(
        dataframe=ea_attributes)


def __load_unmatched_ea_attributes(
        ea_attributes: DataFrame,
        ea_classifiers: DataFrame,
        start_ea_identifier: int,
        xml_root_element: Element) -> Element:
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    unmatched_ea_attributes = \
        ea_attributes.loc[ea_attributes[ea_guids_column_name] == DEFAULT_NULL_VALUE]

    xml_root_element = \
        add_ea_attributes_to_xml_root_element(
            ea_attributes=unmatched_ea_attributes,
            ea_classifiers=ea_classifiers,
            xml_root=xml_root_element,
            start_ea_identifier=start_ea_identifier)

    return \
        xml_root_element
