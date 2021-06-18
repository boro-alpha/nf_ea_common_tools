from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from nf_ea_common_tools_source.b_code.services.session.nf_ea_com_endpoint.orchestrators.universe_managers.nf_ea_com_universe_managers import NfEaComUniverseManagers


def create_full_nf_ea_com(
        nf_ea_com_universe_manager: NfEaComUniverseManagers,
        ea_repository: EaRepositories):
    nf_ea_com_universe_manager.get_ea_packages(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_diagrams(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_full_packages(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_nearest_packages(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_package_contents_summary(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_connector_types(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_diagram_types(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_cardinalities(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_operations(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_attributes(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_element_types(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_object_stereotypes(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_full_generalisations(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_full_dependencies(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_classifiers(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.get_ea_stereotypes(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.create_dependency_depths_table(
        ea_repository=ea_repository)

    nf_ea_com_universe_manager.create_analysis_metrics_table(
        ea_repository=ea_repository)
