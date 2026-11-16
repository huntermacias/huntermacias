#!/usr/bin/env python3
"""Refresh self-hosted public-project cards from GitHub API.

Only public, non-fork, non-archived repositories are shown.
Never reads private repos, PR contents, or personal auth data.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_assets import make_activity

USERNAME = os.environ.get('GITHUB_PROFILE_USERNAME', 'huntermacias')
API = f'https://api.github.com/users/{USERNAME}/repos'


def fetch_public_repos():
    token = os.environ.get('GH_TOKEN')
    headers = {
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'readme-public-activity-v1',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    if token:
        headers['Authorization'] = f'Bearer {token}'
    repos = []
    for page in range(1, 6):
        url = f'{API}?type=owner&sort=pushed&direction=desc&per_page=100&page={page}'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            batch = json.load(resp)
        if not isinstance(batch, list):
            raise ValueError('Expected a list of repositories')
        repos.extend(batch)
        if len(batch) < 100:
            break

    eligible = [
        repo for repo in repos
        if not repo.get('private')
        and not repo.get('fork')
        and not repo.get('archived')
        and repo.get('name', '').lower() != USERNAME.lower()
    ]
    eligible.sort(key=lambda repo: (repo.get('pushed_at') or '', repo.get('name') or ''), reverse=True)
    return [{'name': r['name'], 'description': r.get('description') or 'Open-source repository and experiments.'}
            for r in eligible[:3]]


def main():
    try:
        entries = fetch_public_repos()
        if not entries:
            raise RuntimeError('No qualifying public repos found; keeping existing SVGs.')
        for theme in ('dark', 'light'):
            make_activity(theme, entries)
        print('Updated activity cards for:', ', '.join(e['name'] for e in entries))
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, RuntimeError) as exc:
        print(f'Cannot refresh activity cards: {exc}', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
