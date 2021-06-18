from nf_common_source.code.nf.python_extensions.collections.nf_bimappings import NfBimappings
from ea_interop_service_source.b_code.i_dual_objects.i_dual_repository import IDualRepository
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories


class EaRepositoryMappers:
    __map = \
        NfBimappings({})

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

    @staticmethod
    def store_map(
            ea_repository: EaRepositories,
            i_dual_repository: IDualRepository):
        EaRepositoryMappers.__map.add_mapping(
            domain_value=ea_repository,
            range_value=i_dual_repository)

    @staticmethod
    def get_i_dual_repository(
            ea_repository: EaRepositories) \
            -> IDualRepository:
        i_dual_repository = \
            EaRepositoryMappers.__map.try_get_range_using_domain(
                domain_key=ea_repository).value

        return \
            i_dual_repository

    @staticmethod
    def close_all_ea_repositories():
        for i_dual_repository in EaRepositoryMappers.__map.get_range():
            i_dual_repository.exit()

        EaRepositoryMappers.__map = \
            NfBimappings({})
