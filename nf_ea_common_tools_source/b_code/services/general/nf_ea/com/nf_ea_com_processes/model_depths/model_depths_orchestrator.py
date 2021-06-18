from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.collection_types.nf_ea_com_collection_types import \
    NfEaComCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_processes.model_depths.graph_visualisation_input_tables_generator import \
    generate_dependency_graph_input_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_processes.model_depths.higher_relations_depth_level_counting_generator import \
    generate_dependency_depths_table
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_processes.model_depths.higher_relations_graph_generator import generate_dependency_graph


def orchestrate_depths(
        nf_ea_com_registry):
    ea_full_dependencies = \
        nf_ea_com_registry.get_ea_full_dependencies()

    ea_classifiers = \
        nf_ea_com_registry.get_ea_classifiers()

    dependency_graph_input_table = \
        generate_dependency_graph_input_table(
            ea_full_dependencies_dataframe=ea_full_dependencies,
            ea_classifiers_dataframe=ea_classifiers)

    dependency_graph = \
        generate_dependency_graph(
            visualization_input_tables=dependency_graph_input_table)

    dependency_depths_table = \
        generate_dependency_depths_table(
            graph=dependency_graph)

    nf_ea_com_registry.dictionary_of_collections[NfEaComCollectionTypes.DEPENDENCY_DEPTHS_TABLE] = \
        dependency_depths_table
