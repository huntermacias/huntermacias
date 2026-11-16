# Deploying this profile

Everything in this folder is a ready-to-copy GitHub profile repository bundle for [`huntermacias/huntermacias`](https://github.com/huntermacias/huntermacias). No JavaScript runtime, third-party widget server, or custom GitHub token is required.

## Installation

1. Make a local backup of your existing profile repository, including its current contribution snake workflow.
2. Copy `README.md`, `assets/`, `scripts/`, `docs/`, and `.github/workflows/update-activity.yml` into the **root** of the public `huntermacias/huntermacias` repository.
3. **Important for macOS:** Your current profile file is named lowercase `readme.md`. Rename it to `README.md` using two `git mv` operations on case-insensitive filesystems:

   ```bash
   git mv readme.md readme-old.tmp.md
   git mv readme-old.tmp.md README.md
   ```

   Then replace `README.md` with the one from the bundle. If you use GitHub's web editor, simply remove the old lowercase file and upload the new `README.md`.
4. Disable or remove the old contribution-snake generation workflow **if you no longer want it**. This package deliberately does not overwrite any existing workflows.
5. Review the README's public statements and links, then commit and push the changes from your own terminal.
6. In the repository's **Settings → Actions → General → Workflow permissions**, allow `Read and write permissions` if your policy requires it. Branch protection must allow the workflow to push generated assets.
7. Open **Actions → Update public profile activity → Run workflow**. The image is seeded with verified public examples until the first successful refresh.

GitHub will automatically feature a nonempty root `README.md` in a public repository whose name matches your username.

## What makes it work

- `assets/hero-{dark,light}.svg`: original animated profile masthead.
- `assets/spikeproof-{dark,light}.svg`: original feature illustration (clearly marked illustrative).
- `assets/activity-{dark,light}.svg`: generated cards for the three most recently pushed public, non-fork, non-archived repositories, excluding the profile repository.
- `assets/footer-{dark,light}.svg`: small animated telemetry signature.
- `scripts/render_assets.py`: pure-Python generator for all graphics; only Python's standard library required. Running this script **resets activity cards to sample data**, so use it when editing graphic layouts, then refresh activity again.
- `scripts/update_activity.py`: fetches public repository metadata from the GitHub REST API and updates the activity SVGs. It never fetches private repository data.
- `.github/workflows/update-activity.yml`: scheduled / manual regeneration. Commits **only when an asset actually changes**, avoiding daily meaningless commits.
- `<picture>` sources automatically adapt to GitHub's light or dark theme.
- CSS-keyframe animation uses no script or remote fonts, and honors `prefers-reduced-motion`. Some GitHub surfaces display only a static SVG state.
- `<details>` sections and the Mermaid source-to-evidence diagram are native GitHub-supported interactions.

## Things intentionally not included

- Visitor counters, fake 'currently online' indicators, or made-up metrics.
- A proprietary source-code link for Spikeproof. Its release repository is public; the app source is private.
- Hosted statistics images that can go down or expose request metadata.
- Browser JavaScript; GitHub sanitizes scripts and much of inline CSS in Markdown.

## Tailoring

Edit `README.md` for story, voice and links. Edit the text/layout/colors in `scripts/render_assets.py` for the SVG design, then run `python scripts/render_assets.py` followed by `python scripts/update_activity.py` (the latter requires Internet). To change the workflow username in forks, edit `GITHUB_PROFILE_USERNAME` in the workflow.

Some GitHub clients or image proxies may suppress complex SVG animation. Every asset has a useful static state. Please check actual GitHub rendering on desktop, mobile, dark mode, and light mode after pushing. The local preview is an approximation of GitHub typography/layout, not the actual GitHub Markdown renderer.

## Security & upkeep

The workflow uses the automatically provided `GITHUB_TOKEN` only for public API rate limits and committing the generated file; no personal access token or secrets should be added. Never accept arbitrary untrusted HTML in generated images without XML escaping. An inactive scheduled workflow may be disabled automatically by GitHub; use manual dispatch to re-enable. If you don't want any automatic commits, remove the schedule and keep manual dispatch only.

**Image URL note:** The README uses absolute `raw.githubusercontent.com/huntermacias/huntermacias/main/assets/…` URLs so that `<picture>` works in profile, repository and embedded contexts. If you fork or change the branch, update that prefix. GitHub may cache updated images briefly.
