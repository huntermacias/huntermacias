import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import update_activity


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()


class AssetTests(unittest.TestCase):
    def test_all_svg_assets_parse(self):
        for theme in ('dark', 'light'):
            for asset in ('hero', 'spikeproof', 'activity', 'footer'):
                f = ROOT / 'assets' / f'{asset}-{theme}.svg'
                self.assertTrue(f.exists(), f)
                self.assertEqual(ET.parse(f).getroot().tag, '{http://www.w3.org/2000/svg}svg')

    def test_public_repo_filter_and_sort(self):
        sample = [
            {'name':'huntermacias','private':False,'fork':False,'archived':False,'pushed_at':'2026-11-15T12:00:00Z'},
            {'name':'public-b','private':False,'fork':False,'archived':False,'description':'B','pushed_at':'2026-11-14T12:00:00Z'},
            {'name':'private-a','private':True,'fork':False,'archived':False,'pushed_at':'2026-11-15T11:00:00Z'},
            {'name':'public-a','private':False,'fork':False,'archived':False,'description':'A','pushed_at':'2026-11-15T10:00:00Z'},
            {'name':'forked','private':False,'fork':True,'archived':False,'pushed_at':'2026-11-15T11:00:00Z'},
            {'name':'archived','private':False,'fork':False,'archived':True,'pushed_at':'2026-11-15T11:00:00Z'},
        ]
        with patch.object(update_activity.urllib.request, 'urlopen', return_value=FakeResponse(json.dumps(sample).encode())):
            got = update_activity.fetch_public_repos()
        self.assertEqual([r['name'] for r in got], ['public-a','public-b'])

    def test_readme_embeds_theme_assets(self):
        md = (ROOT / 'README.md').read_text()
        self.assertEqual(md.count('<picture>'), 4)
        self.assertEqual(md.count('</picture>'), 4)
        self.assertIn('prefers-color-scheme: dark', md)
        self.assertIn('prefers-color-scheme: light', md)
        self.assertNotIn('github-contribution-grid-snake', md)
        self.assertIn('source is currently private', md)

if __name__ == '__main__':
    unittest.main()
