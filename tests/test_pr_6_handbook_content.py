"""Regression checks for the handbook style changes in PR 6.

These checks use only the standard library because the handbook does not
currently declare a test framework or a dependency installation path.
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
        rf'<Update\s+label="{re.escape(date)}"[^>]*>(.*?)</Update>',
        page,
        re.DOTALL,
    )
    if not match:
        raise AssertionError(f"Missing changelog update: {date}")
    return match.group(1)


class HandbookTitleTests(unittest.TestCase):
    def test_changed_frontmatter_titles_use_sentence_case(self):
        titles = {
            "brand/identity.mdx": "Brand identity",
            "divisions/index.mdx": "Our divisions",
            "governance/operating-principles.mdx": "Operating principles",
            "projects/index.mdx": "Projects and ventures",
            "technology/security-principles.mdx": "Technology and security principles",
        }
        for path, expected in titles.items():
            with self.subTest(path=path):
                page = read_page(path)
                frontmatter = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", page, re.DOTALL)
                self.assertIsNotNone(frontmatter, f"Missing frontmatter in {path}")
                title = re.findall(r'^title:\s*"([^"]+)"\s*$', frontmatter.group(1), re.MULTILINE)
                self.assertEqual(title, [expected])
                # The divisions page intentionally has a different display heading.
                if path != "divisions/index.mdx":
                    self.assertRegex(page, rf"(?m)^# {re.escape(expected)}\s*$")


class HandbookGuidanceTests(unittest.TestCase):
    def test_brand_guidance_keeps_asset_and_clearance_caveats(self):
        text = section(read_page("brand/identity.mdx"), "Original visual language")
        self.assertRegex(text, r"Use original assets or assets with appropriate licenses\.")
        clearance = re.search(r"Do not assume\b[^.]*legally cleared[^.]*\.", text)
        self.assertIsNotNone(clearance)
        for asset in ("names", "logos", "fonts", "slogans", "artwork"):
            with self.subTest(asset=asset):
                self.assertRegex(clearance.group(0), rf"\b{asset}\b")
        self.assertIn("concept or draft", clearance.group(0))

    def test_security_guidance_preserves_review_and_safe_testing(self):
        text = section(read_page("technology/security-principles.mdx"), "Review before release")
        self.assertRegex(text, r"require appropriate review and explicit approval\.")
        self.assertRegex(text, r"Perform testing in a safe environment\.")
        self.assertRegex(
            text,
            r"Do not use live systems for experiments that could affect real users or data\.",
        )


class ChangelogStyleTests(unittest.TestCase):
    def test_november_2_heading_and_deployment_entry(self):
        text = update(read_page("changelog.mdx"), "November 2, 2026")
        self.assertRegex(text, r"(?m)^\s*## Collective HQ, Chaotic Gaming, and payments\s*$")
        entry = re.search(r"(?m)^\s*- \*\*Chaotic Gaming production deploy[^\n]*$", text)
        self.assertIsNotNone(entry)
        self.assertIn("**: ", entry.group(0))
        self.assertIn("www.chaoticmindsgaming.com", entry.group(0))
        self.assertNotRegex(entry.group(0), r"\s[-–—]\s")

    def test_november_1_design_entry_and_deployment_note(self):
        text = update(read_page("changelog.mdx"), "November 1, 2026")
        entry = re.search(r"(?m)^\s*- \*\*Chaotic Gaming design system v2\*\*:[^\n]*$", text)
        self.assertIsNotNone(entry)
        for detail in ("fonts", "atmosphere", "motion", "mobile"):
            with self.subTest(detail=detail):
                self.assertIn(detail, entry.group(0))
        self.assertNotRegex(entry.group(0), r"\s[-–—]\s")
        note = re.search(r"<Note>\s*(.*?)\s*</Note>", text, re.DOTALL)
        self.assertIsNotNone(note)
        self.assertRegex(note.group(1), r"^Verify the Chaotic Gaming site's deployment status")
        self.assertIn("Vercel dashboard", note.group(1))
        self.assertIn("after the latest build trigger", note.group(1))


if __name__ == "__main__":
    unittest.main()
