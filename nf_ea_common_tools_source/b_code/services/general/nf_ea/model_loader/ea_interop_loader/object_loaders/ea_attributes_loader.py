from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def map_and_load_ea_attributes(
        ea_attributes: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers):
    ea_attributes = \
        ea_attributes.fillna(
            DEFAULT_NULL_VALUE)

    __load_unmatched_ea_attributes(
        ea_attributes=ea_attributes,
        ea_tools_session_manager=ea_tools_session_manager)


def __load_unmatched_ea_attributes(
        ea_attributes: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers):
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    unmatched_ea_attributes = \
        ea_attributes.loc[ea_attributes[ea_guids_column_name] == DEFAULT_NULL_VALUE]

    log_message(
        'Loading ' + str(unmatched_ea_attributes.shape[0]) + ' attributes')

    ea_tools_session_manager.load_ea_attributes(
        ea_attributes=unmatched_ea_attributes)
