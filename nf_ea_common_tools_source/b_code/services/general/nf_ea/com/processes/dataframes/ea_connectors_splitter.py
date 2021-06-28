from nf_common_source.code.services.dataframe_service.dataframe_mergers import inner_merge_dataframes
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_element_types import EaElementTypes
from pandas import concat
from pandas import DataFrame

from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes


def split_ea_connectors(
        ea_connectors: DataFrame,
        ea_classifiers: DataFrame) \
        -> tuple:
    object_type_column_name = \
        NfEaComColumnTypes.ELEMENTS_EA_OBJECT_TYPE.column_name

    place_1_column_name = \
        NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name

    place_2_column_name = \
        NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name

    nf_uuid_column_name = \
        NfColumnTypes.NF_UUIDS.column_name

    proxy_connectors = \
        ea_classifiers.loc[ea_classifiers[object_type_column_name] == EaElementTypes.PROXY_CONNECTOR.type_name]

    if proxy_connectors.empty:
        ea_connectors_connecting_proxy_connector = \
            ea_connectors[
                ~ea_connectors[nf_uuid_column_name].isin(ea_connectors[nf_uuid_column_name])]

        return \
            ea_connectors, \
            ea_connectors_connecting_proxy_connector

    ea_connectors_connecting_proxy_connector_in_place_1 = \
        inner_merge_dataframes(
            master_dataframe=ea_connectors,
            master_dataframe_key_columns=[place_1_column_name],
            merge_suffixes=['_connector', '_proxy_connector'],
            foreign_key_dataframe=proxy_connectors,
            foreign_key_dataframe_fk_columns=[nf_uuid_column_name])

    ea_connectors_connecting_proxy_connector_in_place_2 = \
        inner_merge_dataframes(
            master_dataframe=ea_connectors,
            master_dataframe_key_columns=[place_2_column_name],
            merge_suffixes=['_connector', '_proxy_connector'],
            foreign_key_dataframe=proxy_connectors,
            foreign_key_dataframe_fk_columns=[nf_uuid_column_name])

    ea_connectors_connecting_proxy_connector = \
        concat(
            [
                ea_connectors_connecting_proxy_connector_in_place_1,
                ea_connectors_connecting_proxy_connector_in_place_2
            ])

    ea_connectors_not_connecting_proxy_connector = \
        ea_connectors[
            ~ea_connectors[nf_uuid_column_name].isin(ea_connectors_connecting_proxy_connector[nf_uuid_column_name])]

    return \
        ea_connectors_not_connecting_proxy_connector, \
        ea_connectors_connecting_proxy_connector
