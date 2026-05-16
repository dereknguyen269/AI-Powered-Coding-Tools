import unittest

from scripts import check_links


class LinkSkipTests(unittest.TestCase):
    def test_internal_markdown_anchor_is_skipped(self):
        self.assertTrue(check_links.should_skip_link("#universal-best-practices"))

    def test_external_https_link_is_not_skipped(self):
        self.assertFalse(check_links.should_skip_link("https://github.com/openai/skills"))


if __name__ == "__main__":
    unittest.main()
