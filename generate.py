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

    profile = dict(content.PROFILE)
    for ext in ("jpg", "jpeg", "png", "webp"):
        candidate = STATIC_DIR / "img" / f"profile.{ext}"
        if candidate.exists():
            profile["photo"] = f"static/img/profile.{ext}"
            break

    html = template.render(
        profile=profile,
        domain_knowledge=content.DOMAIN_KNOWLEDGE,
        tools=content.TOOLS,
        works=content.FEATURED_WORK,
        experience=content.EXPERIENCE,
        education=content.EDUCATION,
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")

    output_static = OUTPUT_DIR / "static"
    shutil.copytree(STATIC_DIR, output_static, dirs_exist_ok=True,
                     ignore=shutil.ignore_patterns("desktop.ini"))

    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"Built site -> {OUTPUT_DIR / 'index.html'}")


if __name__ == "__main__":
    build()
