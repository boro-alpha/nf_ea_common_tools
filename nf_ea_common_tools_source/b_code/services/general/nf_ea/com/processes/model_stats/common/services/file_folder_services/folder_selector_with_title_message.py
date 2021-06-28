from tkinter import Tk
from tkinter import filedialog
from nf_common_source.code.services.file_system_service.objects.folders import Folders


def select_folder_with_title_message(
        title: str) \
        -> Folders:
    root = \
        Tk()

    root.withdraw()

    file_path = \
        filedialog.askdirectory(
            parent=root,
            initialdir="/",
            title=title)

    folder = \
        Folders(
            absolute_path_string=file_path)

    return \
        folder
