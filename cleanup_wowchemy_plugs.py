#!/usr/bin/env python3
"""
cleanup_wowchemy_plugs.py

Removes Wowchemy/georgecushen placeholder content and branding from a
Hugo Academic (Wowchemy) site. Run from the repo root.

What this does:
  1. Deletes all content/*/example* placeholder directories
  2. Sets show_powered_by: false  (removes 'Published with Wowchemy' footer)
  3. Updates the site-wide twitter share handle (georgecushen -> yours)
  4. Creates content/talk/icml-2025/index.md with real metadata from
     https://icml.cc/virtual/2025/poster/40183
"""

import shutil
import re
import textwrap
from pathlib import Path

# ─── CONFIGURE THESE ──────────────────────────────────────────────────────────
REPO_ROOT = Path(".")          # run from repo root, or set absolute path
TWITTER_HANDLE = "CGraziul"    # replaces georgecushen sitewide
# ──────────────────────────────────────────────────────────────────────────────


def delete_placeholder_dirs(repo: Path) -> None:
    """
    Delete any content section subdirectory whose name is 'example',
    starts with 'example-', or starts with 'example_'.

    Targets direct children of content sections (depth == 2 under content/),
    e.g. content/talk/example-talk/ or content/project/example/.
    """
    content_dir = repo / "content"
    if not content_dir.exists():
        print("  [WARN] content/ directory not found — skipping placeholder deletion")
        return

    deleted = []
    for candidate in content_dir.rglob("*"):
        # Only match directories that are exactly 2 levels deep under content/
        # (i.e. content/<section>/<entry>/)
        if (
            candidate.is_dir()
            and candidate.parent.parent == content_dir
        ):
            name = candidate.name.lower()
            if name == "example" or name.startswith("example-") or name.startswith("example_"):
                shutil.rmtree(candidate)
                deleted.append(str(candidate.relative_to(repo)))

    if deleted:
        print("  [OK] Deleted placeholder dirs:")
        for d in deleted:
            print(f"       {d}")
    else:
        print("  [OK] No placeholder dirs found (already clean, or check path)")


def patch_params_yaml(repo: Path, twitter_handle: str) -> None:
    """
    Patch config/_default/params.yaml (with fallback paths) to:
      - Set show_powered_by: false   (kills 'Published with Wowchemy' footer)
      - Replace twitter: georgecushen with the real handle

    Idempotent: safe to run multiple times.
    """
    # Try canonical path first, then common alternates
    candidates = [
        repo / "config" / "_default" / "params.yaml",
        repo / "config" / "_default" / "params.toml",
        repo / "params.yaml",
        repo / "config.yaml",
    ]
    params_path = next((p for p in candidates if p.exists()), None)

    if params_path is None:
        print("  [WARN] params.yaml not found in any expected location — skipping config patches")
        print("         Searched:", [str(p) for p in candidates])
        return

    print(f"  [INFO] Patching {params_path.relative_to(repo)}")
    text = params_path.read_text(encoding="utf-8")
    original = text

    # ── 1. Disable powered-by footer ─────────────────────────────────────────
    # Matches:  show_powered_by: true  (with optional spaces/quotes)
    powered_pattern = re.compile(
        r"(show_powered_by\s*:\s*)(true)",
        re.IGNORECASE,
    )
    if powered_pattern.search(text):
        text = powered_pattern.sub(r"\g<1>false", text)
        print("  [OK] Set show_powered_by: false")
    elif "show_powered_by" not in text:
        # Key missing entirely — append it so the footer is suppressed
        text += "\nshow_powered_by: false\n"
        print("  [OK] Appended show_powered_by: false (key was absent)")
    else:
        print("  [INFO] show_powered_by already false — no change needed")

    # ── 2. Fix sharing.twitter handle ────────────────────────────────────────
    # Matches the twitter key inside a sharing: block (indented) or at top level
    # Handles quoted and unquoted values, and the georgecushen default
    twitter_pattern = re.compile(
        r"([ \t]*twitter\s*:\s*)['\"]?georgecushen['\"]?",
        re.IGNORECASE,
    )
    if twitter_pattern.search(text):
        text = twitter_pattern.sub(rf'\g<1>"{twitter_handle}"', text)
        print(f"  [OK] Updated twitter handle: georgecushen → {twitter_handle}")
    else:
        print("  [INFO] georgecushen twitter handle not found — no change needed")

    # Write only if something actually changed
    if text != original:
        params_path.write_text(text, encoding="utf-8")
    else:
        print("  [INFO] params.yaml unchanged (all patches already applied)")


def create_icml_talk(repo: Path) -> None:
    """
    Create content/talk/icml-2025/index.md with real metadata scraped from
    https://icml.cc/virtual/2025/poster/40183

    Paper: 'Position: Stop treating AGI as the north-star goal of AI research'
    Co-authored with Blili-Hamelin, Hancox-Li, Hazan, El-Mhamdi, Ghosh,
    Heller, Metcalf, Murai, Salvaggio, Smart, Snider, Tighanimine, Ringer,
    Mitchell, Dori-Hacohen.

    Video requires ICML login — left empty; update when you have a public URL.
    Slides and poster PDFs are publicly accessible.
    """
    talk_dir = repo / "content" / "talk" / "icml-2025"
    talk_path = talk_dir / "index.md"

    if talk_path.exists():
        print(f"  [INFO] {talk_path.relative_to(repo)} already exists — skipping")
        print("         Delete it manually if you want to regenerate from scratch")
        return

    talk_dir.mkdir(parents=True, exist_ok=True)

    # Abstract and lay summary are taken directly from the ICML virtual page.
    # Truncated here to the core argument for the site display.
    content = textwrap.dedent("""\
        ---
        title: "Position: Stop Treating 'AGI' as the North-Star Goal of AI Research"

        event: "ICML 2025"
        event_url: "https://icml.cc/virtual/2025/poster/40183"

        location: "Vancouver Convention Center"
        address:
          city: Vancouver
          region: BC
          country: Canada

        summary: >
          Position paper arguing that AGI-centric discourse undermines the AI
          research community's ability to set effective scientific, engineering,
          and societal goals. Presented as a poster at ICML 2025.

        abstract: >
          The AI research community plays a vital role in shaping the scientific,
          engineering, and societal goals of AI research. In this position paper,
          we argue that focusing on the highly contested topic of 'artificial
          general intelligence' ('AGI') undermines our ability to choose effective
          goals. We identify six key traps aggravated by AGI discourse: Illusion of
          Consensus, Supercharging Bad Science, Presuming Value-Neutrality, Goal
          Lottery, Generality Debt, and Normalized Exclusion. To avoid these traps,
          we argue that the AI research community needs to (1) prioritize specificity
          in scientific, engineering, and societal goals, (2) center pluralism about
          multiple worthwhile approaches to multiple valuable goals, and (3) foster
          innovation through greater inclusion of disciplines and communities.

        # ICML 2025: July 13–19 2025, Vancouver. Poster session date TBD.
        date: "2025-07-13T09:00:00Z"
        date_end: "2025-07-19T18:00:00Z"
        all_day: true

        publishDate: "2025-01-01T00:00:00Z"

        authors:
          - admin
          - "Borhane Blili-Hamelin"
          - "Leif Hancox-Li"
          - "Hananel Hazan"
          - "El-Mahdi El-Mhamdi"
          - "Avijit Ghosh"
          - "Katherine Heller"
          - "Jacob Metcalf"
          - "Fabricio Murai"
          - "Eryk Salvaggio"
          - "Andrew Smart"
          - "Todd Snider"
          - "Mariame Tighanimine"
          - "Talia Ringer"
          - "Margaret Mitchell"
          - "Shiri Dori-Hacohen"

        tags:
          - "AI ethics"
          - "AGI"
          - "goal setting"
          - "AI research community"
          - "position paper"

        featured: true

        image:
          focal_point: Right

        # Slides and poster PDFs are publicly accessible without ICML login.
        # Video requires login — update url_video when a public recording is available.
        url_pdf: "https://openreview.net/forum?id=1RlrtH6ydW"
        url_slides: "https://icml.cc/media/icml-2025/Slides/40183.pdf"
        url_poster: "https://icml.cc/media/PosterPDFs/ICML%202025/40183.png"
        url_video: ""
        url_code: ""

        math: false
        ---
    """)

    talk_path.write_text(content, encoding="utf-8")
    print(f"  [OK] Created {talk_path.relative_to(repo)}")
    print("       url_video is blank — add a public URL when ICML releases recordings")


def main():
    repo = REPO_ROOT.resolve()
    print(f"\nRepo root: {repo}\n")

    print("── Step 1: Delete placeholder content dirs ──────────────────────")
    delete_placeholder_dirs(repo)

    print("\n── Step 2: Patch config/_default/params.yaml ────────────────────")
    patch_params_yaml(repo, TWITTER_HANDLE)

    print("\n── Step 3: Create ICML 2025 talk entry ──────────────────────────")
    create_icml_talk(repo)

    print("\n── Done ─────────────────────────────────────────────────────────")
    print("  Next steps:")
    print("  1. git diff                    # review all changes")
    print("  2. hugo server                 # verify locally")
    print("  3. git add -A && git commit -m 'Remove Wowchemy plugs; add ICML 2025 talk'")
    print("  4. git push                    # GitHub Actions rebuilds the site")
    print()
    print("  When ICML releases public recording URLs, update:")
    print("  content/talk/icml-2025/index.md  →  url_video: \"<url>\"")


if __name__ == "__main__":
    main()