from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.full_nf_ea_com_creation import create_full_nf_ea_com


def create_new_nf_ea_com_universe_using_file(
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository_file: Files,
        short_name: str):
    nf_ea_com_universe_repository = \
        ea_tools_session_manager.create_ea_repository_using_file_and_short_name(
            ea_repository_file=ea_repository_file,
            short_name=short_name)

    nf_ea_com_universe_manager = \
        ea_tools_session_manager.nf_ea_com_endpoint_manager.nf_ea_com_universe_manager

    create_full_nf_ea_com(
        nf_ea_com_universe_manager=nf_ea_com_universe_manager,
        ea_repository=nf_ea_com_universe_repository)

    nf_ea_com_universe = \
        nf_ea_com_universe_manager.nf_ea_com_universe_dictionary[nf_ea_com_universe_repository]

    return \
        nf_ea_com_universe
