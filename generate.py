"""
Static site generator for the portfolio.

Renders templates/index.html.j2 with data from content.py, then writes the
result plus static assets into docs/ — the folder GitHub Pages serves when
configured to deploy from the main branch's /docs directory.

Usage:
    python generate.py
"""

import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import content

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
OUTPUT_DIR = ROOT / "docs"


def build():
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("index.html.j2")

    html = template.render(
        profile=content.PROFILE,
        core_competencies=content.CORE_COMPETENCIES,
        project=content.FEATURED_PROJECT,
        experience=content.EXPERIENCE,
        technical_skills=content.TECHNICAL_SKILLS,
        certifications=content.CERTIFICATIONS,
        education=content.EDUCATION,
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")

    output_static = OUTPUT_DIR / "static"
    if output_static.exists():
        shutil.rmtree(output_static)
    shutil.copytree(STATIC_DIR, output_static)

    # Prevent GitHub Pages from running Jekyll over the output.
    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"Built site -> {OUTPUT_DIR / 'index.html'}")


if __name__ == "__main__":
    build()
