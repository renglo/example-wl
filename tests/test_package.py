#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import wl  # noqa: E402


class WlPackageTests(unittest.TestCase):
    def test_app_name_is_product_not_env(self) -> None:
        self.assertEqual(wl.app_name, "Example")
        self.assertNotIn("example1", wl.app_name.lower())

    def test_invite_locale_has_placeholders(self) -> None:
        invite = wl.locale("en")["email"]["invite"]
        self.assertIn("{appName}", invite["subject"])
        self.assertIn("{team}", invite["subject"])
        self.assertIn("{inviter}", invite["intro"])
        self.assertIn("{code}", invite["code"])

    def test_product_catalog_exists(self) -> None:
        catalog = ROOT / "product.yaml"
        self.assertTrue(catalog.is_file())
        text = catalog.read_text(encoding="utf-8")
        self.assertIn("packages:", text)
        self.assertIn("data:", text)
        self.assertIn("schd:", text)

    def test_small_logo_exists(self) -> None:
        self.assertIsNotNone(wl.small_logo_path)
        self.assertTrue(wl.small_logo_path.is_file())


if __name__ == "__main__":
    unittest.main()
