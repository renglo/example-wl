"""Tenant white-label pack: app name, locales, and logo paths.

Import name is always ``wl`` so controllers stay tenant-agnostic. The
distribution name is ``<tenant>-wl`` (this template: ``example-wl``).

Locales and assets live at the repo root for the npm pack. Editable
installs read those folders. A wheel copies them next to this module.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent


def _data_root() -> Path:
    if (_HERE / "locales").is_dir():
        return _HERE
    repo = _HERE.parent.parent
    if (repo / "locales").is_dir():
        return repo
    return _HERE


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_locales() -> dict[str, dict[str, Any]]:
    folder = _data_root() / "locales"
    found: dict[str, dict[str, Any]] = {}
    if not folder.is_dir():
        return found
    for path in sorted(folder.glob("*.json")):
        payload = _read_json(path)
        if isinstance(payload, dict):
            found[path.stem] = payload
    return found


def _asset(name: str) -> Path | None:
    path = _data_root() / "assets" / name
    return path if path.is_file() else None


locales: dict[str, dict[str, Any]] = _load_locales()

_en = locales.get("en") or {}
app_name = str(_en.get("appName") or "").strip()

_login = _en.get("login") if isinstance(_en.get("login"), dict) else {}
captions = {
    "appName": app_name,
    "loginTitle": str(_login.get("title") or "Login"),
    "loginSubtitle": str(
        _login.get("subtitle") or "Enter your email below to login to your account"
    ),
}

small_logo_path = _asset("small_logo.png")
large_logo_path = _asset("large_logo.png")
background_path = _asset("background.png")


def locale(code: str = "en") -> dict[str, Any]:
    return locales.get(code) or {}
