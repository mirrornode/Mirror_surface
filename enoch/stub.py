"""
enoch/stub.py

Enoch Integration Stub for Mirror_surface
-----------------------------------------
This module is a placeholder for the Enoch agent integration.
When the Enoch module is ready, this stub will be replaced by
the live enoch/agent.py implementation.

The CI pipeline monitors for this file's presence to report
integration readiness status.

Architecture:
    Mirror_surface -> enoch/stub.py -> [enoch/agent.py] -> MirrorNode core
"""

from __future__ import annotations
from typing import Any

# Feature flag: set to True when Enoch agent is live
ENOCH_LIVE = False


class EnochStub:
    """
    Stub interface matching the contract that Enoch will fulfill.
    All methods return placeholder responses until the real agent is wired in.
    """

    def __init__(self):
        self.live = ENOCH_LIVE
        self.agent_id = "enoch-stub-v0"

    def query(self, prompt: str, context: dict[str, Any] | None = None) -> dict:
        """
        Send a query to the Enoch reasoning agent.

        Args:
            prompt: Natural language query or instruction.
            context: Optional context dict (session state, memory, etc.)

        Returns:
            Response dict with 'status', 'response', and 'agent_id' keys.
        """
        if self.live:
            # TODO: replace with live Enoch agent call
            # from enoch.agent import EnochAgent
            # return EnochAgent().query(prompt, context)
            raise NotImplementedError("Enoch live mode not yet configured")

        return {
            "status": "stub",
            "agent_id": self.agent_id,
            "response": f"[Enoch stub] Query received: '{prompt}'",
            "context_received": context is not None,
            "note": "Awaiting Enoch module integration",
        }

    def health(self) -> dict:
        """Return integration health status."""
        return {
            "enoch_live": self.live,
            "stub_active": not self.live,
            "agent_id": self.agent_id,
            "status": "ready_for_integration" if not self.live else "live",
        }


# Module-level singleton — import and use directly
enoch = EnochStub()


if __name__ == "__main__":
    print(enoch.health())
    print(enoch.query("Test query from Mirror_surface"))
