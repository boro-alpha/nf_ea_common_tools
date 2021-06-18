from nf_common_source.code.nf.python_extensions.collections.nf_bimappings import NfBimappings
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.nf_domains.standard_object_table_column_types import StandardObjectTableColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes


def get_standard_stereotype_group_to_nf_ea_com_column_name_dictionary() \
        -> dict:
    standard_stereotype_group_to_nf_ea_com_column_name_dictionary = \
        __standard_stereotype_group_to_nf_ea_com_column_name_bimapping.get_range_keyed_on_domain()

    return \
        standard_stereotype_group_to_nf_ea_com_column_name_dictionary


def get_nf_ea_com_column_name_to_standard_stereotype_group_dictionary() \
        -> dict:
    nf_ea_com_column_name_to_standard_stereotype_group_dictionary = \
        __standard_stereotype_group_to_nf_ea_com_column_name_bimapping.get_domain_keyed_on_range()

    return \
        nf_ea_com_column_name_to_standard_stereotype_group_dictionary


__standard_stereotype_group_to_nf_ea_com_column_name_bimapping = \
    NfBimappings(
        map=
        {
            StandardObjectTableColumnTypes.NF_UUIDS.column_name: NfColumnTypes.NF_UUIDS.column_name,
            StandardObjectTableColumnTypes.UML_OBJECT_NAMES.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name
        })
