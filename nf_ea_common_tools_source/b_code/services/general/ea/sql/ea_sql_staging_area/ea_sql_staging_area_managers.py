from nf_ea_common_tools_source.b_code.services.general.ea.sql.ea_sql_staging_area.ea_sql_model_dictionaries import EaSqlModelDictionaries
from nf_ea_common_tools_source.b_code.nf_ea_common.objects.ea_repositories import EaRepositories
from typing import Dict


class EaSqlStagingAreaManagers:
    def __init__(
            self):
        self.ea_repository_dictionary = \
            Dict[EaRepositories, EaSqlModelDictionaries]

    def __enter__(
            self):
        return \
            self

    def __exit__(
            self,
            exception_type,
            exception_value,
            traceback):
        pass
