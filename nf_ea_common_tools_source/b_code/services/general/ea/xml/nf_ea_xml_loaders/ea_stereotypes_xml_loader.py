from nf_ea_common_tools_source.b_code.services.general.ea.xml.nf_ea_xml_adders.ea_stereotypes_to_dataset_xml_adder import add_ea_stereotypes_to_dataset_xml_root_element
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.maps.nf_uuids_to_ea_guids_mappings import NfUuidsToEaGuidsMappings
from pandas import DataFrame
from xml.etree.ElementTree import Element


def map_and_xml_load_ea_stereotypes(
        ea_stereotypes: DataFrame,
        xml_element_for_stereotypes_dataset: Element) \
        -> Element:
    log_message(
        'Exporting stereotypes')

    ea_stereotypes = \
        ea_stereotypes.fillna(
            DEFAULT_NULL_VALUE)

    __map_ea_stereotypes(
        ea_stereotypes=ea_stereotypes)

    xml_root = \
        __load_ea_stereotypes(
            ea_stereotypes=ea_stereotypes,
            xml_element_for_stereotypes_dataset=xml_element_for_stereotypes_dataset)

    return \
        xml_root


def __map_ea_stereotypes(
        ea_stereotypes: DataFrame):
    NfUuidsToEaGuidsMappings.map_objects_from_dataframe(
        dataframe=ea_stereotypes)


def __load_ea_stereotypes(
        ea_stereotypes: DataFrame,
        xml_element_for_stereotypes_dataset: Element) \
        -> Element:
    xml_root = \
        add_ea_stereotypes_to_dataset_xml_root_element(
            ea_stereotypes=ea_stereotypes,
            xml_element_for_stereotypes_dataset=xml_element_for_stereotypes_dataset)

    return \
        xml_root
