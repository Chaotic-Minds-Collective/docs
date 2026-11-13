"""Regression checks for handbook content.

Adapted for the GitHub Pages (plain markdown) handbook. These checks use
only the standard library because the handbook does not declare a test
framework or a dependency installation path.
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_page(path):
    return (ROOT / path).read_text(encoding="utf-8")


def section(page, heading):
    match = re.search(
        rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)",
        page,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise AssertionError(f"Missing section: {heading}")
    return match.group(1)


def update(page, date):
    match = re.search(
        rf"^## {re.escape(date)}\s*\n(.*?)(?=^## |\Z)",
        page,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise AssertionError(f"Missing changelog update: {date}")
    return match.group(1)


class HandbookTitleTests(unittest.TestCase):
    def test_changed_frontmatter_titles_use_sentence_case(self):
        titles = {
            "brand/identity.md": "Brand identity",
            "divisions/index.md": "Our brands and divisions",
            "governance/operating-principles.md": "Operating principles",
            "projects/index.md": "Projects and ventures",
            "technology/security-principles.md": "Technology and security principles",
        }
        for path, expected in titles.items():
            with self.subTest(path=path):
                page = read_page(path)
                frontmatter = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", page, re.DOTALL)
                self.assertIsNotNone(frontmatter, f"Missing frontmatter in {path}")
                title = re.findall(r'^title:\s*"([^"]+)"\s*$', frontmatter.group(1), re.MULTILINE)
                self.assertEqual(title, [expected])
                # The divisions page intentionally has a different display heading.
                if path != "divisions/index.md":
                    self.assertRegex(page, rf"(?m)^# {re.escape(expected)}\s*$")


class HandbookGuidanceTests(unittest.TestCase):
    def test_brand_guidance_keeps_asset_and_clearance_caveats(self):
        text = section(read_page("brand/identity.md"), "Original visual language")
        self.assertRegex(text, r"Use original assets or assets with appropriate licenses\.")
        clearance = re.search(r"Do not assume\b[^.]*legally cleared[^.]*\.", text)
        self.assertIsNotNone(clearance)
        for asset in ("names", "logos", "fonts", "slogans", "artwork"):
            with self.subTest(asset=asset):
                self.assertRegex(clearance.group(0), rf"\b{asset}\b")
        self.assertIn("concept or draft", clearance.group(0))

    def test_security_guidance_preserves_review_and_safe_testing(self):
        text = section(read_page("technology/security-principles.md"), "Review before release")
        self.assertRegex(text, r"require appropriate review and explicit approval\.")
        self.assertRegex(text, r"Perform testing in a safe environment\.")
        self.assertRegex(
            text,
            r"Do not use live systems for experiments that could affect real users or data\.",
        )


class ChangelogStyleTests(unittest.TestCase):
    def test_november_2_heading_and_deployment_entry(self):
        text = update(read_page("changelog.md"), "November 2, 2026")
        self.assertRegex(text, r"(?m)^\s*### Collective HQ, Chaotic Gaming, and payments\s*$")
        entry = re.search(r"(?m)^\s*- \*\*Chaotic Gaming production deploy[^\n]*$", text)
        self.assertIsNotNone(entry)
        self.assertRegex(entry.group(0), r"\*\*(?::| - )")
        self.assertIn("www.chaoticmindsgaming.com", entry.group(0))
        self.assertNotRegex(entry.group(0), r"[\u2013\u2014]")

    def test_november_1_design_entry_and_deployment_note(self):
        text = update(read_page("changelog.md"), "November 1, 2026")
        entry = re.search(r"(?m)^\s*- \*\*Chaotic Gaming design system v2\*\*:[^\n]*$", text)
        self.assertIsNotNone(entry)
        for detail in ("fonts", "atmosphere", "motion", "mobile"):
            with self.subTest(detail=detail):
                self.assertIn(detail, entry.group(0))
        self.assertNotRegex(entry.group(0), r"[\u2013\u2014]")
        note_lines = re.findall(r"(?m)^\s*> ?(.*)$", text)
        self.assertTrue(note_lines, "No blockquote note found in the November 1 entry")
        note = " ".join(line.strip() for line in note_lines if line.strip())
        self.assertRegex(note, r"[Dd]eployment status.*[Vv]erified")
        self.assertIn("Vercel", note)
        self.assertIn("dashboard", note)
        self.assertIn("after the latest build trigger", note)


if __name__ == "__main__":
    unittest.main()
