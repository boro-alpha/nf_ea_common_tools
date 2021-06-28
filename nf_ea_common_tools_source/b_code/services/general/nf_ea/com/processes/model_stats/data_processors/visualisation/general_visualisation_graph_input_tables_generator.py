from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.processes.model_stats.common.constants import \
    SUPPLIER_PLACE1_END_CONNECTORS_COLUMN_NAME, CLIENT_PLACE2_END_CONNECTORS_COLUMN_NAME, \
    EA_CONNECTOR_ELEMENT_TYPE_NAME_COLUMN_NAME


def generate_general_visualisation_graph_input_tables(
        ea_connectors: DataFrame) \
        -> DataFrame:
    general_edges_dataframe = \
        ea_connectors.filter(
            items=[
                SUPPLIER_PLACE1_END_CONNECTORS_COLUMN_NAME,
                CLIENT_PLACE2_END_CONNECTORS_COLUMN_NAME,
                EA_CONNECTOR_ELEMENT_TYPE_NAME_COLUMN_NAME])
    return \
        general_edges_dataframe
