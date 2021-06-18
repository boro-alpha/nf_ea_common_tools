import os
from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.file_system_service.objects.folders import Folders
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_universes import NfEaComUniverses
from nf_ea_common_tools_source.b_code.services.general.nf_ea.model_loader.native_xml_loader.nf_ea_xml_load_to_empty_ea_model_orchestrator import orchestrate_nf_ea_xml_load_to_empty_ea_model
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers


@run_and_log_function
def orchestrate_nf_ea_com_universe_to_eapx_migration(
        ea_tools_session_manager: EaToolsSessionManagers,
        nf_ea_com_universe: NfEaComUniverses,
        short_name: str,
        output_folder: Folders):
    ea_export_folder_path = \
        os.path.join(
            output_folder.absolute_path_string,
            short_name,
            short_name + '_ea_export')

    ea_repository_file_path = \
        os.path.join(
            ea_export_folder_path,
            short_name + '_ea_export.eapx')

    ea_repository_file = \
        Files(
            absolute_path_string=ea_repository_file_path)

    output_xml_file_full_path = \
        os.path.join(
            ea_export_folder_path,
            short_name + '_ea_export.xml')

    orchestrate_nf_ea_xml_load_to_empty_ea_model(
        ea_tools_session_manager=ea_tools_session_manager,
        nf_ea_com_universe=nf_ea_com_universe,
        output_xml_file_full_path=output_xml_file_full_path,
        ea_repository_file=ea_repository_file,
        short_name=short_name + '_ea_export')
