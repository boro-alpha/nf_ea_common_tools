from pandas import DataFrame
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.factories.common.nf_uuid_getter import \
    get_nf_uuid_from_ea_guid


class EaFullDependenciesOfTypeFactories:
    def __init__(
            self,
            nf_ea_com_universe,
            type_ea_guid: str):
        self.nf_ea_com_universe = \
            nf_ea_com_universe

        self.type_ea_guid = \
            type_ea_guid

    def create(
            self) \
            -> DataFrame:
        ea_full_dependencies = \
            self.nf_ea_com_universe.nf_ea_com_registry.get_ea_full_dependencies()

        type_nf_uuid = \
            get_nf_uuid_from_ea_guid(
                nf_ea_com_universe=self.nf_ea_com_universe,
                ea_guid=self.type_ea_guid)

        ea_full_dependencies_of_type = \
            ea_full_dependencies.loc[ea_full_dependencies['provider'] == type_nf_uuid]

        nf_uuids_column_name = \
            NfColumnTypes.NF_UUIDS.column_name

        ea_full_dependencies_of_type = \
            dataframe_filter_and_rename(
                dataframe=ea_full_dependencies_of_type,
                filter_and_rename_dictionary=
                {
                    'dependent': nf_uuids_column_name
                })

        return \
            ea_full_dependencies_of_type
