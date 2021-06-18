from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame
from xml.etree.ElementTree import Element
from nf_ea_common_tools_source.b_code.services.general.ea.xml.nf_ea_xml_adders.ea_stereotype_usages_xml_adder import add_ea_stereotype_usages_to_xml_root_element


def map_and_xml_load_ea_stereotype_usages(
        stereotype_usage_with_names: DataFrame,
        xml_root_element: Element) \
        -> Element:
    log_message(
        'Exporting stereotype usages')

    xml_root_element = \
        add_ea_stereotype_usages_to_xml_root_element(
            stereotype_usage_with_names=stereotype_usage_with_names,
            xml_root=xml_root_element)

    return \
        xml_root_element
