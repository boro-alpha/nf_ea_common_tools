from pandas import DataFrame
from typing import Dict

from nf_ea_common_tools_source.b_code.nf_ea_common.common_knowledge.ea_collection_types import EaCollectionTypes


class EaSqlModelDictionaries:
    def __init__(
            self):
        self.ea_sql_model_dictionary = \
            Dict[EaCollectionTypes, DataFrame]

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
