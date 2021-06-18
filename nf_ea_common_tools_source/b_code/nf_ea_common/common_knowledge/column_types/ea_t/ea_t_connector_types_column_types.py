from enum import auto
from enum import unique
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.ea_t.ea_t_column_types import EaTColumnTypes


@unique
class EaTConnectorTypesColumnTypes(
    EaTColumnTypes):
    T_CONNECTOR_TYPES_CONNECTOR_TYPES = auto()
    T_CONNECTOR_TYPES_DESCRIPTIONS = auto()

    def __column_name(
            self) \
            -> str:
        column_name = \
            column_name_mapping[self]

        return \
            column_name

    def __nf_column_name(
            self) \
            -> str:
        nf_column_name = \
            nf_column_name_mapping[self]

        return \
            nf_column_name

    column_name = \
        property(
            fget=__column_name)

    nf_column_name = \
        property(
            fget=__nf_column_name)


column_name_mapping = \
    {
        EaTConnectorTypesColumnTypes.T_CONNECTOR_TYPES_CONNECTOR_TYPES: 'Connector_Type',
        EaTConnectorTypesColumnTypes.T_CONNECTOR_TYPES_DESCRIPTIONS: 'Description'
    }


nf_column_name_mapping = \
    {
        EaTConnectorTypesColumnTypes.T_CONNECTOR_TYPES_CONNECTOR_TYPES: 't_connector_types_connector_types',
        EaTConnectorTypesColumnTypes.T_CONNECTOR_TYPES_DESCRIPTIONS: 't_connector_types_descriptions'
    }
