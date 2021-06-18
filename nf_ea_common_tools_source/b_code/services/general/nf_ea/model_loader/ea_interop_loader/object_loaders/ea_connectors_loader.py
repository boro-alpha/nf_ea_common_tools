from nf_common_source.code.constants.standard_constants import DEFAULT_NULL_VALUE
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from pandas import DataFrame
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import \
    NfEaComColumnTypes
from nf_ea_common_tools_source.b_code.services.session.orchestrators.ea_tools_session_managers import \
    EaToolsSessionManagers


def map_and_load_ea_connectors(
        ea_connectors: DataFrame,
        stereotype_usage_with_names: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers):
    ea_connectors = \
        ea_connectors.fillna(
            DEFAULT_NULL_VALUE)

    __load_unmatched_ea_connectors(
        ea_connectors=ea_connectors,
        stereotype_usage_with_names=stereotype_usage_with_names,
        ea_tools_session_manager=ea_tools_session_manager)


def __load_unmatched_ea_connectors(
        ea_connectors: DataFrame,
        stereotype_usage_with_names: DataFrame,
        ea_tools_session_manager: EaToolsSessionManagers):
    ea_guids_column_name = \
        NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name

    unmatched_ea_connectors = \
        ea_connectors.loc[ea_connectors[ea_guids_column_name] == DEFAULT_NULL_VALUE]

    log_message(
        'Loading ' + str(unmatched_ea_connectors.shape[0]) + ' connectors')

    ea_tools_session_manager.load_ea_connectors(
        ea_connectors=unmatched_ea_connectors,
        stereotype_usage_with_names=stereotype_usage_with_names)
