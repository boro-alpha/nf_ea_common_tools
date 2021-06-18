import tkinter as tk
from tkinter import simpledialog
from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_ea_common_tools_source.b_code.services.general.ea.com.ea_com_managers import EaComManagers
from nf_ea_common_tools_source.b_code.services.general.ea.com.ea_repository_factory import create_ea_repository
from nf_ea_common_tools_source.b_code.services.general.ea.com.ea_repository_factory import create_empty_ea_repository
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories


def get_repository() \
        -> EaRepositories:
    with \
            EaComManagers() \
                    as ea_com_manager:
        ea_repository_file = \
            ea_com_manager.get_ea_repository_file()

        short_name = \
            __get_short_name()

        ea_repository = \
            get_repository_using_file_and_short_name(
                ea_repository_file=ea_repository_file,
                short_name=short_name)

        return \
            ea_repository


def get_repository_using_file_and_short_name(
        ea_repository_file: Files,
        short_name: str) \
        -> EaRepositories:
    ea_repository = \
        create_ea_repository(
            ea_repository_file=ea_repository_file,
            short_name=short_name)

    return \
        ea_repository


def get_empty_ea_repository_with_short_name(
        short_name: str) \
        -> EaRepositories:
    ea_repository = \
        create_empty_ea_repository(
            short_name=short_name)

    return \
        ea_repository


def __get_short_name():
    root = \
        tk.Tk()

    root.withdraw()

    short_name = \
        simpledialog.askstring(
            title="Input",
            prompt="Enter The Repository's Short Name")

    return \
        short_name
