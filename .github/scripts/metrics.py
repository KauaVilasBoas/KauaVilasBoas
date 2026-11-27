"""Draws profile/metrics-dark.svg and profile/metrics-light.svg from profile/metrics.json.

The NuGet download total is fetched live; every other tile is a fixed value with its
source named in metrics.json. The script also rewrites the metrics image's alt text and
the "updated" date in README.md, so the numbers stay readable to search and screen readers.
"""

import datetime
import json
import re
import urllib.request
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "profile" / "metrics.json"
README_PATH = ROOT / "README.md"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "border": "#30363d",
        "rule": "#21262d",
        "value": "#e6edf3",
        "label": "#c9d1d9",
        "sub": "#8d96a0",
        "live": "#3fb950",
        "foot": "#161b22",
    },
    "light": {
        "bg": "#ffffff",
        "border": "#d0d7de",
        "rule": "#eaeef2",
        "value": "#1f2328",
        "label": "#31363c",
        "sub": "#59636e",
        "live": "#1a7f37",
        "foot": "#f6f8fa",
    },
}
WIDTH, ROW_HEIGHT, FOOT_HEIGHT = 840, 118, 34
ROWS = (
    3,
    2,
)  # tiles per row: two rows stay readable when GitHub shrinks the image on a phone
SANS = "'Segoe UI',-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
MONO = "SFMono-Regular,Consolas,Menlo,monospace"


def nuget_downloads(nuget):
    url = f"https://azuresearch-usnc.nuget.org/query?q={nuget['query']}&prerelease=true&take=100"
    with urllib.request.urlopen(url, timeout=30) as response:
        packages = json.load(response)["data"]
    return sum(
        package["totalDownloads"]
        for package in packages
        if package["id"].startswith(nuget["prefix"])
        and nuget["owner"] in [owner.lower() for owner in package.get("owners") or []]
    )


def tile_values(config):
    try:
        config["nuget"]["last"] = nuget_downloads(config["nuget"])
    except Exception as error:  # keep the last known total when NuGet is down
        print(f"NuGet lookup failed, keeping {config['nuget']['last']}: {error}")
    downloads = f"{config['nuget']['last']:,}"
    return [
        dict(tile, value=tile["value"].replace("{nuget}", downloads))
        for tile in config["tiles"]
    ]


def draw(tiles, colors, footer):
    body = ROW_HEIGHT * len(ROWS)
    height = body + FOOT_HEIGHT
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{escape(alt_text(tiles))}">',
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="8" '
        f'fill="{colors["bg"]}" stroke="{colors["border"]}"/>',
        f'<path d="M1 {body}H{WIDTH - 1}V{height - 9}a8 8 0 0 1-8 8H9a8 8 0 0 1-8-8Z" '
        f'fill="{colors["foot"]}"/>',
    ]
    remaining = iter(tiles)
    for row, count in enumerate(ROWS):
        top, tile_width = row * ROW_HEIGHT, WIDTH / count
        parts.append(
            f'<line x1="1" y1="{top + ROW_HEIGHT}" x2="{WIDTH - 1}" '
            f'y2="{top + ROW_HEIGHT}" stroke="{colors["rule"]}"/>'
        )
        for column in range(count):
            tile, x = next(remaining), column * tile_width + 24
            if column:
                parts.append(
                    f'<line x1="{column * tile_width}" y1="{top + 16}" '
                    f'x2="{column * tile_width}" y2="{top + ROW_HEIGHT - 16}" '
                    f'stroke="{colors["rule"]}"/>'
                )
            parts.append(
                f'<text x="{x}" y="{top + 52}" font-family="{SANS}" font-size="38" '
                f'font-weight="700" fill="{colors["value"]}">{escape(tile["value"])}</text>'
            )
            if tile.get("live"):
                live_x = x + len(tile["value"]) * 21 + 10
                parts.append(
                    f'<rect x="{live_x}" y="{top + 28}" width="38" height="20" rx="5" '
                    f'fill="none" stroke="{colors["live"]}" stroke-opacity=".5"/>'
                    f'<text x="{live_x + 19}" y="{top + 43}" text-anchor="middle" '
                    f'font-family="{MONO}" font-size="13" font-weight="600" '
                    f'fill="{colors["live"]}">live</text>'
                )
            parts.append(
                f'<text x="{x}" y="{top + 80}" font-family="{SANS}" font-size="18" '
                f'fill="{colors["label"]}">{escape(tile["label"])}</text>'
            )
            parts.append(
                f'<text x="{x}" y="{top + 101}" font-family="{MONO}" font-size="13" '
                f'fill="{colors["sub"]}">{escape(tile["sub"])}</text>'
            )
    parts.append(
        f'<text x="24" y="{body + 22}" font-family="{MONO}" font-size="12" '
        f'fill="{colors["sub"]}">{escape(footer)}</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def alt_text(tiles):
    return "Metrics: " + "; ".join(f"{tile['value']} {tile['label']}" for tile in tiles)


def update_readme(tiles, today):
    text = README_PATH.read_text(encoding="utf-8")
    text = re.sub(r'alt="Metrics:[^"]*"', f'alt="{escape(alt_text(tiles))}"', text)
    text = re.sub(r"(<!--updated-->).*?(<!--/updated-->)", rf"\g<1>{today}\g<2>", text)
    README_PATH.write_text(text, encoding="utf-8")


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    tiles = tile_values(config)
    today = datetime.date.today().strftime("%d %b %Y").lstrip("0")
    footer = f"updated {today} · NuGet downloads fetched live, the rest from the linked sources"
    for theme, colors in THEMES.items():
        (ROOT / "profile" / f"metrics-{theme}.svg").write_text(
            draw(tiles, colors, footer), encoding="utf-8"
        )
    CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    update_readme(tiles, today)


if __name__ == "__main__":
    main()
