from nf_common_source.code.nf.python_extensions.collections.nf_bimappings import NfBimappings
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.column_types.nf_domains.standard_object_table_column_types import StandardObjectTableColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes


def get_standard_classifier_to_nf_ea_com_column_name_dictionary() \
        -> dict:
    standard_classifier_to_nf_ea_com_column_name_dictionary = \
        __standard_classifier_to_nf_ea_com_column_name_bimapping.get_range_keyed_on_domain()

    return \
        standard_classifier_to_nf_ea_com_column_name_dictionary


def get_nf_ea_com_column_name_to_standard_classifier_dictionary() \
        -> dict:
    nf_ea_com_column_name_to_standard_classifier_dictionary = \
        __standard_classifier_to_nf_ea_com_column_name_bimapping.get_domain_keyed_on_range()

    return \
        nf_ea_com_column_name_to_standard_classifier_dictionary


__standard_classifier_to_nf_ea_com_column_name_bimapping = \
    NfBimappings(
        map=
        {
            StandardObjectTableColumnTypes.NF_UUIDS.column_name: NfColumnTypes.NF_UUIDS.column_name,
            StandardObjectTableColumnTypes.UML_OBJECT_NAMES.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name,
            NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NOTES.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NOTES.column_name,
            NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name: NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name,
            StandardObjectTableColumnTypes.OBJECT_UML_TYPE_IDENTIFIERS.column_name: NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name,
            StandardObjectTableColumnTypes.PARENT_PACKAGE_NF_UUIDS.column_name: NfEaComColumnTypes.PACKAGEABLE_OBJECTS_PARENT_EA_ELEMENT.column_name,
            StandardObjectTableColumnTypes.OBJECT_CLASSIFIER_NF_UUIDS.column_name: NfEaComColumnTypes.ELEMENTS_CLASSIFIER.column_name
        })
