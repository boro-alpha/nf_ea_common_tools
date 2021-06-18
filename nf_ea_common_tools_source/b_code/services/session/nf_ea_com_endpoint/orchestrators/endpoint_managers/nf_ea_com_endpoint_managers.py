from nf_ea_common_tools_source.b_code.services.session.nf_ea_com_endpoint.orchestrators.nf_managers import NfManagers
from nf_ea_common_tools_source.b_code.services.session.nf_ea_com_endpoint.orchestrators.universe_managers.nf_ea_com_universe_managers import \
    NfEaComUniverseManagers


class NfEaComEndpointManagers(
        NfManagers):
    def __init__(
            self,
            ea_tools_session_manager):
        NfManagers.__init__(
            self)

        self.nf_ea_com_universe_manager = \
            NfEaComUniverseManagers(
                ea_tools_session_manager=ea_tools_session_manager)

    def close(
            self):
        self.nf_ea_com_universe_manager.close()
