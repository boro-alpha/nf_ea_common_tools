from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.factories.common.level_adder import add_level
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.factories.levels.ea_stereotypeable_objects_level_adder import add_ea_stereotypeable_objects_level
from pandas import DataFrame


def add_ea_packageable_objects_level(
        nf_ea_com_universe,
        dataframe: DataFrame) \
        -> DataFrame:
    thin_ea_packageable_objects = \
        nf_ea_com_universe.nf_ea_com_registry.get_thin_ea_packageable_objects()

    dataframe = \
        add_level(
            dataframe=dataframe,
            next_level_dataframe=thin_ea_packageable_objects)

    dataframe = \
        add_ea_stereotypeable_objects_level(
            nf_ea_com_universe,
            dataframe=dataframe)

    return \
        dataframe
