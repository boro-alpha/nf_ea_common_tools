from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.file_system_service.objects.folders import Folders
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function

from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.orchestrators.nf_ea_com_universe_to_standard_tables_migration_orchestrator import orchestrate_nf_ea_com_universe_to_standard_tables_migration
from nf_ea_common_tools_source.b_code.services.general.nf_ea.domain_migration.nf_ea_com_to_domain_migration.orchestrators.standard_tables_to_xlsx_migration_orchestrator import orchestrate_standard_tables_to_xlsx_migration
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.exporters.all_universes_exporter import export_all_universes


@run_and_log_function
def orchestrate_eapx_to_xlsx_migration(
        input_file: Files,
        output_folder: Folders,
        short_name: str):
    log_message(
        '========== Started Converting eapx to xlsx ==========')

    log_message(
        'Input eapx file - ' + input_file.absolute_path_string)

    log_message(
        'Output folder - ' + output_folder.absolute_path_string)

    with EaToolsSessionManagers() \
                    as ea_tools_session_manager:
        standard_tables_dictionary = \
            orchestrate_nf_ea_com_universe_to_standard_tables_migration(
                ea_tools_session_manager=ea_tools_session_manager,
                ea_repository_file=input_file,
                short_name=short_name)

        orchestrate_standard_tables_to_xlsx_migration(
            standard_tables_dictionary=standard_tables_dictionary,
            output_folder=output_folder)

        export_all_universes(
            ea_tools_session_manager=ea_tools_session_manager,
            output_folder=output_folder)

    log_message(
        '========== Finished Converting eapx to xlsx ==========')
