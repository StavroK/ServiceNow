import os
from typing import Any

import requests


class ServiceNowClient:
    """Minimal ServiceNow Table API client for portfolio demonstration.

    Credentials are read from environment variables and must never be committed.
    """

    def __init__(self, instance_url: str | None = None, token: str | None = None) -> None:
        self.instance_url = (instance_url or os.getenv("SERVICENOW_INSTANCE_URL", "")).rstrip("/")
        self.token = token or os.getenv("SERVICENOW_TOKEN", "")

    def _headers(self) -> dict[str, str]:
        if not self.token:
            raise RuntimeError("SERVICENOW_TOKEN is not configured")
        return {"Authorization": f"Bearer {self.token}", "Accept": "application/json", "Content-Type": "application/json"}

    def update_incident(self, sys_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        if not self.instance_url:
            raise RuntimeError("SERVICENOW_INSTANCE_URL is not configured")
        url = f"{self.instance_url}/api/now/table/incident/{sys_id}"
        response = requests.patch(url, json=payload, headers=self._headers(), timeout=15)
        response.raise_for_status()
        return response.json()
