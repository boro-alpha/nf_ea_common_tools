from nf_common_source.code.nf.python_extensions.collections.nf_bimappings import NfBimappings
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.ea_t.ea_t_xref_column_types import EaTXrefColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.nf_domains.standard_object_table_column_types import StandardObjectTableColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes


def get_standard_stereotype_usage_to_nf_ea_com_column_name_dictionary() \
        -> dict:
    standard_stereotype_usage_to_nf_ea_com_column_name_dictionary = \
        __standard_stereotype_usage_to_nf_ea_com_column_name_bimapping.get_range_keyed_on_domain()

    return \
        standard_stereotype_usage_to_nf_ea_com_column_name_dictionary


def get_nf_ea_com_column_name_to_standard_stereotype_usage_dictionary() \
        -> dict:
    nf_ea_com_column_name_to_standard_stereotype_usage_dictionary = \
        __standard_stereotype_usage_to_nf_ea_com_column_name_bimapping.get_domain_keyed_on_range()

    return \
        nf_ea_com_column_name_to_standard_stereotype_usage_dictionary


__standard_stereotype_usage_to_nf_ea_com_column_name_bimapping = \
    NfBimappings(
        map=
        {
            StandardObjectTableColumnTypes.CLIENT_NF_UUIDS.column_name: NfEaComColumnTypes.STEREOTYPE_CLIENT_NF_UUIDS.column_name,
            StandardObjectTableColumnTypes.STEREOTYPE_NF_UUIDS.column_name: 'stereotype_nf_uuids',
            StandardObjectTableColumnTypes.CLIENT_EA_GUIDS.column_name: EaTXrefColumnTypes.T_XREF_CLIENT_EA_GUIDS.nf_column_name,
            StandardObjectTableColumnTypes.STEREOTYPE_EA_GUIDS.column_name: 'stereotype_guids'
        })
