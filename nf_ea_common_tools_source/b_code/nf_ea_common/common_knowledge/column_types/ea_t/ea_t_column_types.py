from enum import unique
from nf_common_source.code.nf.types.column_types import ColumnTypes


@unique
class EaTColumnTypes(
    ColumnTypes):
    def __column_name(
            self) \
            -> str:
        raise \
            NotImplementedError

    def __nf_column_name(
            self) \
            -> str:
        raise \
            NotImplementedError

    column_name = \
        property(
            fget=__column_name)

    nf_column_name = \
        property(
            fget=__nf_column_name)
