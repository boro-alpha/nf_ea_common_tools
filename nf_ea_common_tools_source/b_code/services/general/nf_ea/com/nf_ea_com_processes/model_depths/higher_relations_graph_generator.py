from pandas import DataFrame
import networkx

from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.nf_ea_com_processes.model_depths.model_depths_constants import \
    PROVIDER_COLUMN_NAME, DEPENDENT_COLUMN_NAME


def generate_dependency_graph(
        visualization_input_tables: DataFrame) \
        -> networkx.Graph:
    # Theoretically, the source should be the DEPENDENT, but apparently, it needs to be set the other way around
    # for Networkx module to retrieve the leaves of the paths properly.
    # This results in the leaves being the last element of the nf_uuids lists reported in the dependency_depths table
    higher_relations_graph = \
        networkx.from_pandas_edgelist(
            visualization_input_tables,
            source=PROVIDER_COLUMN_NAME,
            target=DEPENDENT_COLUMN_NAME,
            create_using=networkx.DiGraph())

    return \
        higher_relations_graph
