from pandas import DataFrame
from networkx import MultiDiGraph
from networkx import is_empty
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes


def get_nodes_base_table_from_multi_edged_directed_graph(
        multi_edged_directed_graph: MultiDiGraph) \
        -> DataFrame:
    if is_empty(multi_edged_directed_graph):
        nodes_base_table = \
            DataFrame(
                columns=[NfColumnTypes.NF_UUIDS.column_name])

    else:
        nodes_list = \
            list(multi_edged_directed_graph.nodes)

        nodes_table_dictionary = \
            {
                NfColumnTypes.NF_UUIDS.column_name: nodes_list
            }

        nodes_base_table = \
            DataFrame.from_dict(
                nodes_table_dictionary)

    return \
        nodes_base_table
