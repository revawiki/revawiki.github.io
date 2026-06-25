# Portfolio

A neutral (white / grey / black) static portfolio site, generated from Python.

## Structure

- `content.py` — all text content (profile, experience, project, skills, certs). Edit this to change what shows on the site.
- `templates/index.html.j2` — Jinja2 page template.
- `static/css/style.css` — styling.
- `generate.py` — renders the template with `content.py` data into `docs/`.
- `docs/` — generated output. This is what GitHub Pages serves. Do not hand-edit files in here; re-run the generator instead.

## Build

```bash
pip install jinja2
python generate.py
```

## Preview locally

```bash
python -m http.server 8000 --directory docs
```

Then open http://localhost:8000

## Deploy to GitHub Pages

1. Push this repo to GitHub.
2. In the repo settings, go to **Pages**.
3. Under "Build and deployment" → Source, choose **Deploy from a branch**.
4. Branch: `main`, folder: `/docs`.
5. Save. The site will be live at `https://<username>.github.io/<repo>/`.

Whenever you edit `content.py`, `templates/`, or `static/`, re-run `python generate.py` and commit the updated `docs/` folder.

## NDA note

Content is intentionally limited to facts already disclosed on the public CV and the strategic/conceptual slides of the AIOps deck (problem statement, pillars, role mapping, outcome metrics). No internal tool screenshots, dashboards, or client-specific data are included. Expand `content.py` carefully if adding more detail.
