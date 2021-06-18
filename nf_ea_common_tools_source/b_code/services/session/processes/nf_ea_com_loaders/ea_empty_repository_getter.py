import importlib
import os
import shutil
from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def get_ea_repository_for_empty_ea_model(
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository_file: Files,
        short_name: str) \
        -> EaRepositories:
    module = \
        importlib.import_module(
            name='nf_ea_common_tools_source.resources.templates')

    module_path_string = \
        module.__path__._path[0]

    resource_full_file_name = \
        os.path.join(
            module_path_string,
            'empty.eapx')

    if not os.path.exists(ea_repository_file.parent_absolute_path_string):
        os.makedirs(
            ea_repository_file.parent_absolute_path_string)

    log_message(
        message='File ' + ea_repository_file.absolute_path_string + ' will be replaced with ' + resource_full_file_name)

    shutil.copy(
        src=resource_full_file_name,
        dst=ea_repository_file.absolute_path_string)

    ea_repository = \
        ea_tools_session_manager.create_ea_repository_using_file_and_short_name(
            ea_repository_file=ea_repository_file,
            short_name=short_name)

    return \
        ea_repository
