from numpy import NaN
from pandas import DataFrame
import networkx


def generate_dependency_depths_table(
        graph: networkx.graph) \
        -> DataFrame:
    if networkx.is_empty(graph):
        path_level_counting_tables = \
            DataFrame(
                data={
                    'paths': [[]],
                    'level_depth': [0]
                })

        return \
            path_level_counting_tables

    roots = \
        __generate_graph_roots_list(
            graph=graph)

    leaves = \
        __generate_graph_leaves_list(
            graph=graph)

    all_paths_list = \
        __generate_list_of_simple_paths(
            graph=graph,
            roots=roots,
            leaves=leaves)

    path_level_counting_tables = \
        __generate_path_level_counting_tables(
            all_paths_list=all_paths_list)

    return \
        path_level_counting_tables


def __generate_graph_roots_list(
        graph) \
        -> list:
    roots = []

    for node, depth in graph.in_degree():
        if depth == 0:
            roots.append(
                node)

    return \
        roots


def __generate_graph_leaves_list(
        graph) \
        -> list:
    leaves = []

    for node, depth in graph.out_degree():
        if depth == 0:
            leaves.append(
                node)

    return \
        leaves


def __generate_list_of_simple_paths(
        graph: networkx.Graph,
        roots: list,
        leaves: list) \
        -> list:
    all_paths = []

    for root in roots:
        paths = \
            networkx.all_simple_paths(
                graph,
                root,
                leaves)

        all_paths.extend(
            paths)

    return \
        all_paths


def __generate_path_level_counting_tables(
        all_paths_list: list) \
        -> DataFrame:
    paths_dictionary = {
        'paths': all_paths_list,
        'level_depth': NaN
    }

    path_level_counting_tables = \
        DataFrame.from_dict(
            paths_dictionary)

    path_level_counting_tables['level_depth'] = \
        path_level_counting_tables['paths'].str.len() - 1

    return \
        path_level_counting_tables
