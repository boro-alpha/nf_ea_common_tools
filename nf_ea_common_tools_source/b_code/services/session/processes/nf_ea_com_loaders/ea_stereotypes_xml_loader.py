from nf_ea_common_tools_source.b_code.services.session.ea_repository_mappers import EaRepositoryMappers
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories


def load_ea_stereotypes_xml(
        ea_repository: EaRepositories,
        xml_string: str):
    i_dual_repository = \
        EaRepositoryMappers.get_i_dual_repository(
            ea_repository=ea_repository)

    i_dual_repository.custom_command(
        "Repository",
        "ImportRefData",
        xml_string)
