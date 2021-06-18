from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers
from nf_ea_common_tools_source.b_code.services.session.processes.creators.new_nf_ea_com_universe_using_file_creator import create_new_nf_ea_com_universe_using_file


def load_ea_model_into_hdf5(
        ea_tools_session_manager: EaToolsSessionManagers,
        ea_repository_file: Files,
        short_name: str,
        hdf5_file: Files):
    loaded_universe = \
        create_new_nf_ea_com_universe_using_file(
            ea_tools_session_manager=ea_tools_session_manager,
            ea_repository_file=ea_repository_file,
            short_name=short_name)

    loaded_universe.nf_ea_com_registry.export_registry_to_hdf5(
        hdf5_file=hdf5_file)
