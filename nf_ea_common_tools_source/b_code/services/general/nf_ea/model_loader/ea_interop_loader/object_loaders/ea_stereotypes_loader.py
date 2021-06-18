from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.services.general.ea.xml.ea_stereotypes_xml_orchestrator import orchestrate_ea_stereotypes_xml
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_additional_column_types import \
    NfEaComAdditionalColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.maps.nf_uuids_to_ea_guids_mappings import NfUuidsToEaGuidsMappings
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def map_and_load_ea_stereotypes(
        ea_stereotypes: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository: EaRepositories):
    ea_stereotypes = \
        ea_stereotypes.fillna(
            DEFAULT_NULL_VALUE)

    __load_unmatched_ea_stereotypes(
        ea_stereotypes=ea_stereotypes,
        ea_tools_session_manager=ea_tools_session_manager,
        ea_repository=ea_repository)

    xml_string = \
        orchestrate_ea_stereotypes_xml(
            ea_stereotypes=ea_stereotypes)

    ea_tools_session_manager.load_ea_stereotypes_xml(
        ea_repository=ea_repository,
        xml_string=xml_string)


def __load_unmatched_ea_stereotypes(
        ea_stereotypes: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository: EaRepositories):
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    unmatched_ea_stereotypes = \
        ea_stereotypes.loc[ea_stereotypes[ea_guids_column_name] == DEFAULT_NULL_VALUE]

    original_ea_guids_column_name = \
        NfEaComAdditionalColumnTypes.ORIGINAL_EA_GUIDS.column_name

    if original_ea_guids_column_name in unmatched_ea_stereotypes:
        unmatched_ea_stereotypes = \
            unmatched_ea_stereotypes.loc[ea_stereotypes[original_ea_guids_column_name] == DEFAULT_NULL_VALUE]

    log_message(
        'Loading ' + str(unmatched_ea_stereotypes.shape[0]) + ' stereotypes')

    ea_tools_session_manager.load_ea_stereotypes(
        ea_repository=ea_repository,
        ea_stereotypes=unmatched_ea_stereotypes)

    __map_matched_stereotypes(
        unmatched_ea_stereotypes=unmatched_ea_stereotypes,
        ea_guids_column_name=ea_guids_column_name)


def __map_matched_stereotypes(
        unmatched_ea_stereotypes: DataFrame,
        ea_guids_column_name: str):
    for row_tuple in unmatched_ea_stereotypes.itertuples():
        __map_matched_stereotype(
            row_tuple=row_tuple,
            ea_guids_column_name=ea_guids_column_name)


def __map_matched_stereotype(
        row_tuple: tuple,
        ea_guids_column_name: str):
    nf_uuid = \
        getattr(
            row_tuple,
            NfColumnTypes.NF_UUIDS.column_name)

    ea_guid = \
        getattr(
            row_tuple,
            ea_guids_column_name)

    NfUuidsToEaGuidsMappings.add_single_map(
        nf_uuid=str(nf_uuid),
        ea_guid=ea_guid)
