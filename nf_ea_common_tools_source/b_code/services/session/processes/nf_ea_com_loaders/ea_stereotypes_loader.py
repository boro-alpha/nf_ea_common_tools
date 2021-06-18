from ea_interop_service_source.b_code.factories.i_dual_stereotype_factory import create_i_dual_stereotype
from ea_interop_service_source.b_code.i_dual_objects.stereotypes.i_dual_stereotype import IDualStereotype
from pandas import DataFrame
from tqdm import tqdm
from nf_ea_common_tools_source.b_code.services.session.ea_repository_mappers import EaRepositoryMappers
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes


def load_ea_stereotypes(
        ea_repository: EaRepositories,
        ea_stereotypes: DataFrame):
    name_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_OBJECT_NAME.column_name

    ea_guid_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    for index, ea_stereotypes_row in tqdm(ea_stereotypes.iterrows(), total=ea_stereotypes.shape[0]):
        ea_stereotype = \
            __load_ea_stereotype(
                ea_repository=ea_repository,
                ea_stereotype_name=ea_stereotypes_row[name_column_name])

        ea_stereotypes.at[index, ea_guid_column_name] = \
            ea_stereotype.stereotype_guid

    return \
        ea_stereotypes


def __load_ea_stereotype(
        ea_repository: EaRepositories,
        ea_stereotype_name: str) \
        -> IDualStereotype:
    i_dual_repository = \
        EaRepositoryMappers.get_i_dual_repository(
            ea_repository=ea_repository)

    ea_stereotype = \
        create_i_dual_stereotype(
            i_dual_repository=i_dual_repository,
            stereotype_name=ea_stereotype_name)

    return \
        ea_stereotype
