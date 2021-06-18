from ea_interop_service_source.b_code.i_dual_objects.elements.i_dual_element import IDualElement
from ea_interop_service_source.b_code.i_dual_objects.i_dual_repository import IDualRepository
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import Series
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.session.ea_repository_mappers import EaRepositoryMappers
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_element_types import EaElementTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.maps.nf_uuids_to_com_objects_mappings import NfUuidsToIDualObjectsMappings
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def map_and_load_ea_classifiers(
        ea_classifiers: DataFrame,
        stereotype_usage_with_names: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository: EaRepositories):
    ea_classifiers = \
        ea_classifiers.fillna(
            DEFAULT_NULL_VALUE)

    __map_matched_ea_classifiers(
        ea_classifiers=ea_classifiers,
        ea_repository=ea_repository)

    __load_unmatched_ea_classifiers(
        ea_classifiers=ea_classifiers,
        stereotype_usage_with_names=stereotype_usage_with_names,
        ea_tools_session_manager=ea_tools_session_manager)


def __map_matched_ea_classifiers(
        ea_classifiers: DataFrame,
        ea_repository: EaRepositories):
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    nf_uuid_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    type_column_name = \
        NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name

    matched_ea_classifiers = \
        ea_classifiers.loc[ea_classifiers[ea_guids_column_name] != DEFAULT_NULL_VALUE]

    matched_ea_classifiers = \
        matched_ea_classifiers.loc[ea_classifiers[type_column_name] != EaElementTypes.PROXY_CONNECTOR.type_name]

    log_message(
        'Mapping ' + str(matched_ea_classifiers.shape[0]) + ' classifiers')

    i_dual_repository = \
        EaRepositoryMappers.get_i_dual_repository(
            ea_repository=ea_repository)

    for index, ea_classifier_row in matched_ea_classifiers.iterrows():
        __map_matched_ea_classifier(
            ea_classifier_row=ea_classifier_row,
            i_dual_repository=i_dual_repository,
            nf_uuid_column_name=nf_uuid_column_name,
            ea_guids_column_name=ea_guids_column_name)


def __map_matched_ea_classifier(
        ea_classifier_row: Series,
        i_dual_repository: IDualRepository,
        nf_uuid_column_name: str,
        ea_guids_column_name: str):
    nf_uuid = \
        ea_classifier_row[nf_uuid_column_name]

    ea_guid = \
        ea_classifier_row[ea_guids_column_name]

    ea_classifier = \
        i_dual_repository.get_element_by_guid(
            element_ea_guid=ea_guid)

    if not isinstance(ea_classifier, IDualElement):
        raise \
            TypeError

    NfUuidsToIDualObjectsMappings.map_nf_uuid_to_i_dual_element(
        nf_uuid=nf_uuid,
        i_dual_element=ea_classifier)


def __load_unmatched_ea_classifiers(
        ea_classifiers: DataFrame,
        stereotype_usage_with_names: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers):
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    type_column_name = \
        NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name

    unmatched_ea_classifiers = \
        ea_classifiers.loc[ea_classifiers[ea_guids_column_name] == DEFAULT_NULL_VALUE]

    unmatched_ea_classifiers = \
        unmatched_ea_classifiers.loc[ea_classifiers[type_column_name] != EaElementTypes.PROXY_CONNECTOR.type_name]

    log_message(
        'Loading ' + str(unmatched_ea_classifiers.shape[0]) + ' classifiers')

    ea_tools_session_manager.load_ea_classifiers(
        ea_classifiers=unmatched_ea_classifiers,
        stereotype_usage_with_names=stereotype_usage_with_names)
