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
WIDTH, TILE_HEIGHT, FOOT_HEIGHT = 840, 112, 30
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
    tile_width = WIDTH / len(tiles)
    height = TILE_HEIGHT + FOOT_HEIGHT
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{escape(alt_text(tiles))}">',
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="8" '
        f'fill="{colors["bg"]}" stroke="{colors["border"]}"/>',
        f'<path d="M1 {TILE_HEIGHT}H{WIDTH - 1}V{height - 9}a8 8 0 0 1-8 8H9a8 8 0 0 1-8-8Z" '
        f'fill="{colors["foot"]}"/>',
        f'<line x1="1" y1="{TILE_HEIGHT}" x2="{WIDTH - 1}" y2="{TILE_HEIGHT}" stroke="{colors["rule"]}"/>',
    ]
    for index, tile in enumerate(tiles):
        x = index * tile_width + 18
        if index:
            parts.append(
                f'<line x1="{index * tile_width}" y1="14" x2="{index * tile_width}" '
                f'y2="{TILE_HEIGHT - 14}" stroke="{colors["rule"]}"/>'
            )
        parts.append(
            f'<text x="{x}" y="50" font-family="{SANS}" font-size="30" font-weight="700" '
            f'fill="{colors["value"]}">{escape(tile["value"])}</text>'
        )
        if tile.get("live"):
            live_x = x + len(tile["value"]) * 16.5 + 8
            parts.append(
                f'<rect x="{live_x}" y="30" width="30" height="16" rx="4" fill="none" '
                f'stroke="{colors["live"]}" stroke-opacity=".5"/>'
                f'<text x="{live_x + 15}" y="42" text-anchor="middle" font-family="{MONO}" '
                f'font-size="10" font-weight="600" fill="{colors["live"]}">live</text>'
            )
        parts.append(
            f'<text x="{x}" y="76" font-family="{SANS}" font-size="13.5" '
            f'fill="{colors["label"]}">{escape(tile["label"])}</text>'
        )
        parts.append(
            f'<text x="{x}" y="95" font-family="{MONO}" font-size="11" '
            f'fill="{colors["sub"]}">{escape(tile["sub"])}</text>'
        )
    parts.append(
        f'<text x="18" y="{TILE_HEIGHT + 19}" font-family="{MONO}" font-size="11" '
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
