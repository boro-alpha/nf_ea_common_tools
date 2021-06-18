from ea_interop_service_source.b_code.i_dual_objects.elements.i_dual_element import IDualElement
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import Series
from pandas import DataFrame
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.maps.nf_uuids_to_com_objects_mappings import NfUuidsToIDualObjectsMappings
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def reorder_ea_attributes(
        ea_attributes_order: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers):
    log_message(
        'Reordering attributes')

    classifier_id_order = \
        {}

    for index, ea_attributes_order_row in ea_attributes_order.iterrows():
        classifier_id_order = \
            __add_classifier_to_order(
                ea_attributes_order_row=ea_attributes_order_row,
                classifier_id_order=classifier_id_order)
    ea_tools_session_manager.reorder_ea_attributes(
        classifier_id_order=classifier_id_order)


def __add_classifier_to_order(
        ea_attributes_order_row: Series,
        classifier_id_order: dict) \
        -> dict:
    nf_uuids_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    attribute_type_nf_uuid = \
        ea_attributes_order_row[nf_uuids_column_name]

    classifier = \
        NfUuidsToIDualObjectsMappings.get_i_dual_element(
            nf_uuid=attribute_type_nf_uuid)

    if not isinstance(classifier, IDualElement):
        raise \
            TypeError

    classifier_id_order[classifier.element_id] = \
        int(ea_attributes_order_row['attribute_order'])

    return \
        classifier_id_order
