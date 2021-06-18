from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid
from pandas import DataFrame
from nf_common_source.code.services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import dataframe_filter_and_rename
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_collection_types import EaCollectionTypes
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes


class EaStereotypeGroupFactories:
    def __init__(
            self,
            nf_ea_com_universe):
        self.nf_ea_com_universe = \
            nf_ea_com_universe

    def create(
            self) \
            -> DataFrame:
        ea_stereotype_groups = \
            self.__create_ea_stereotype_groups_from_stereotypes()

        ea_stereotype_groups = \
            self.__add_identity(ea_stereotype_groups=ea_stereotype_groups)

        return \
            ea_stereotype_groups

    def __create_ea_stereotype_groups_from_stereotypes(
            self) \
            -> DataFrame:
        extended_t_stereotypes_dataframe = \
            self.nf_ea_com_universe.ea_tools_session_manager.nf_ea_sql_stage_manager.nf_ea_sql_universe_manager.get_extended_ea_t_table_dataframe(
                ea_repository=self.nf_ea_com_universe.ea_repository,
                ea_collection_type=EaCollectionTypes.EXTENDED_T_STEREOTYPES)

        ea_stereotype_groups = \
            extended_t_stereotypes_dataframe.groupby(
                'stereotype_group_names').first()

        ea_stereotype_groups = \
            ea_stereotype_groups.reset_index()

        ea_stereotype_groups = \
            ea_stereotype_groups[ea_stereotype_groups['stereotype_group_names'] != '']

        object_name_column_name = \
            NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name

        ea_stereotype_groups = \
            dataframe_filter_and_rename(
                dataframe=ea_stereotype_groups,
                filter_and_rename_dictionary=
                {
                    'stereotype_group_names': object_name_column_name
                })

        return \
            ea_stereotype_groups

    @staticmethod
    def __add_identity(
            ea_stereotype_groups: DataFrame) \
            -> DataFrame:
        nf_uuids_column_name = \
            NfColumnTypes.NF_UUIDS.column_name

        ea_stereotype_groups[nf_uuids_column_name] = \
            ea_stereotype_groups.apply(
                lambda row:
                create_new_uuid(),
                axis=1)

        return \
            ea_stereotype_groups
