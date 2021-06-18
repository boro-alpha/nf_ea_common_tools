from nf_common_source.code.nf.python_extensions.collections.nf_bimappings import NfBimappings
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.nf_domains.standard_connector_table_column_types import StandardConnectorTableColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes


def get_standard_connector_to_nf_ea_com_column_name_dictionary() \
        -> dict:
    standard_connector_to_nf_ea_com_column_name_dictionary = \
        __standard_connector_to_nf_ea_com_column_name_bimapping.get_range_keyed_on_domain()

    return \
        standard_connector_to_nf_ea_com_column_name_dictionary


def get_nf_ea_com_column_name_to_standard_connector_dictionary() \
        -> dict:
    nf_ea_com_column_name_to_standard_connector_dictionary = \
        __standard_connector_to_nf_ea_com_column_name_bimapping.get_domain_keyed_on_range()

    return \
        nf_ea_com_column_name_to_standard_connector_dictionary


__standard_connector_to_nf_ea_com_column_name_bimapping = \
    NfBimappings(
        map=
        {
            NfColumnTypes.NF_UUIDS.column_name: NfColumnTypes.NF_UUIDS.column_name,
            StandardConnectorTableColumnTypes.SUPPLIER_PLACE_1_NF_UUIDS.column_name: NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name,
            StandardConnectorTableColumnTypes.CLIENT_PLACE_2_NF_UUIDS.column_name: NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name,
            StandardConnectorTableColumnTypes.CONNECTOR_UML_TYPE_IDENTIFIERS.column_name: NfEaComColumnTypes.CONNECTORS_ELEMENT_TYPE_NAME.column_name,
            StandardConnectorTableColumnTypes.CONNECTOR_UML_NAMES.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name,
            StandardConnectorTableColumnTypes.CONNECTOR_NOTES.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NOTES.column_name,
            NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name,
        })
