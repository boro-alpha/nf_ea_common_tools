from ea_interop_service_source.b_code.i_dual_objects.packages.i_dual_package import IDualPackage
from ea_interop_service_source.b_code.i_dual_objects.packages.i_null_package import INullPackage
from nf_ea_common_tools_source.b_code.services.session.ea_repository_mappers import EaRepositoryMappers
from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_common_source.code.services.tuple_service.tuple_attribute_value_getter import get_tuple_attribute_value_if_required
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from pandas import DataFrame


def rename_nf_ea_packages(
        ea_repository: EaRepositories,
        input_dataframe: DataFrame):
    input_dataframe = \
        input_dataframe.fillna(
            DEFAULT_NULL_VALUE)

    for input_tuple in input_dataframe.itertuples():
        __rename_nf_ea_package_using_input_tuple(
            ea_repository=ea_repository,
            input_tuple=input_tuple)


def __rename_nf_ea_package_using_input_tuple(
        ea_repository: EaRepositories,
        input_tuple: tuple):
    package_guid = \
        get_tuple_attribute_value_if_required(
            owning_tuple=input_tuple,
            attribute_name='guid')

    new_ea_package_name = \
        get_tuple_attribute_value_if_required(
            owning_tuple=input_tuple,
            attribute_name='new_name')

    __rename_nf_ea_package(
        ea_repository=ea_repository,
        package_guid=package_guid,
        new_ea_package_name=new_ea_package_name)


def __rename_nf_ea_package(
        ea_repository: EaRepositories,
        package_guid: str,
        new_ea_package_name: str):
    i_dual_repository = \
        EaRepositoryMappers.get_i_dual_repository(
            ea_repository=ea_repository)

    i_dual_package = \
        i_dual_repository.get_package_by_guid(
            package_ea_guid=package_guid)

    if isinstance(i_dual_package, INullPackage):
        log_message(
            package_guid + "Warning: Package not found")

        return

    if not isinstance(i_dual_package, IDualPackage):
        raise \
            TypeError

    old_ea_package_name = \
        i_dual_package.name

    if old_ea_package_name == new_ea_package_name:
        log_message(
            package_guid + "Current name equals clean name for Package Name (" + old_ea_package_name + ")")

    else:
        i_dual_package.name = \
            new_ea_package_name

        i_dual_package.update()

        log_message(
            package_guid + " : Package Name changed (" + old_ea_package_name + ") to (" + new_ea_package_name + ")")
