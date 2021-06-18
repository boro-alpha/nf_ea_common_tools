from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def get_ea_repository(
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository_file: Files,
        short_name: str) \
        -> EaRepositories:
    ea_repository = \
        ea_tools_session_manager.create_ea_repository_using_file_and_short_name(
            ea_repository_file=ea_repository_file,
            short_name=short_name)

    return \
        ea_repository
