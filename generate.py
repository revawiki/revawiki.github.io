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

    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"Built site -> {OUTPUT_DIR / 'index.html'}")


if __name__ == "__main__":
    build()
