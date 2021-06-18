from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_registries import NfEaComRegistries
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from pandas import DataFrame

from nf_ea_common_tools_source.b_code.services.session.processes.creators.nf_ea_com_universe_copier import \
    register_universe_copy


class NfEaComUniverses:
    def __init__(
            self,
            ea_tools_session_manager,
            ea_repository: EaRepositories):
        self.ea_tools_session_manager = \
            ea_tools_session_manager

        self.ea_repository = \
            ea_repository

        self.nf_ea_com_registry = \
            NfEaComRegistries(
                self)

    def __enter__(
            self):
        return \
            self

    def __exit__(
            self,
            exception_type,
            exception_value,
            traceback):
        pass

    def copy(
            self,
            short_name=str()):
        ea_repository_copy = \
            EaRepositories(
                short_name=short_name,
                ea_repository_file=self.ea_repository.ea_repository_file)

        self_copy = \
            NfEaComUniverses(
                ea_tools_session_manager=self.ea_tools_session_manager,
                ea_repository=ea_repository_copy)

        self_copy.nf_ea_com_registry = \
            self.nf_ea_com_registry.copy()

        register_universe_copy(
            ea_tools_session_manager=self.ea_tools_session_manager,
            nf_ea_com_universe=self_copy,
            ea_repository_copy=ea_repository_copy)

        return \
            self_copy

    def export_dataframes(
            self,
            project_short_name: str,
            output_folder_name: str):
        self.nf_ea_com_registry.export_dataframes(
            short_name=project_short_name,
            output_folder_name=output_folder_name)

    def get_ea_stereotypes(
            self) \
            -> DataFrame:
        ea_stereotypes = \
            self.nf_ea_com_registry.get_ea_stereotypes()

        return \
            ea_stereotypes

    def get_ea_stereotype_groups(
            self) \
            -> DataFrame:
        ea_stereotype_groups = \
            self.nf_ea_com_registry.get_ea_stereotype_groups()

        return \
            ea_stereotype_groups
