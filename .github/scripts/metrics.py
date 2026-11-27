"""Draws the profile's metrics and stack cards, dark and light, from profile/metrics.json.

The NuGet download total is fetched live; every other tile is a fixed value with its
source named in metrics.json. The script also rewrites both images' alt text and the
"updated" date in README.md, so the content stays readable to search and screen readers.
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
# Stack card. Chip widths are estimated from a monospace advance of 0.6em, so the
# text stays centered whatever monospace font the viewer has.
CHIP_FONT, CHIP_HEIGHT, CHIP_GAP, CHIP_PAD, DOT_SPACE = 14, 30, 8, 12, 14
CHAR_WIDTH = CHIP_FONT * 0.6
CHIPS_LEFT, GROUP_GAP = 156, 20


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


def chip_width(name, production):
    return len(name) * CHAR_WIDTH + 2 * CHIP_PAD + (DOT_SPACE if production else 0)


def draw_chip(x, y, name, production, colors):
    width = chip_width(name, production)
    stroke = (
        f'stroke="{colors["live"]}" stroke-opacity=".6"'
        if production
        else f'stroke="{colors["border"]}"'
    )
    parts = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{CHIP_HEIGHT}" '
        f'rx="{CHIP_HEIGHT / 2}" fill="{colors["foot"]}" {stroke}/>'
    ]
    text_left = x + CHIP_PAD
    if production:
        parts.append(
            f'<circle cx="{x + CHIP_PAD + 4}" cy="{y + CHIP_HEIGHT / 2}" r="4" '
            f'fill="{colors["live"]}"/>'
        )
        text_left += DOT_SPACE
    parts.append(
        f'<text x="{text_left + len(name) * CHAR_WIDTH / 2}" y="{y + 20}" '
        f'text-anchor="middle" font-family="{MONO}" font-size="{CHIP_FONT}" '
        f'fill="{colors["value"]}">{escape(name)}</text>'
    )
    return parts, width


def draw_stack(groups, colors):
    """Chips grouped by area, wrapped to the card width; production chips get a green dot."""
    parts, top = [], GROUP_GAP / 2
    for index, group in enumerate(groups):
        if index:
            parts.append(
                f'<line x1="1" y1="{top - GROUP_GAP / 2}" x2="{WIDTH - 1}" '
                f'y2="{top - GROUP_GAP / 2}" stroke="{colors["rule"]}"/>'
            )
        parts.append(
            f'<text x="24" y="{top + 20}" font-family="{MONO}" font-size="13" '
            f'letter-spacing="1.2" fill="{colors["sub"]}">{escape(group["label"].upper())}</text>'
        )
        x, y = CHIPS_LEFT, top
        chips = [(name, True) for name in group["production"]] + [
            (name, False) for name in group["public"]
        ]
        for name, production in chips:
            if x + chip_width(name, production) > WIDTH - 24:
                x, y = CHIPS_LEFT, y + CHIP_HEIGHT + CHIP_GAP
            chip, width = draw_chip(x, y, name, production, colors)
            parts += chip
            x += width + CHIP_GAP
        top = y + CHIP_HEIGHT + GROUP_GAP
    body = top - GROUP_GAP / 2
    height = body + FOOT_HEIGHT
    return (
        "\n".join(
            [
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
                f'viewBox="0 0 {WIDTH} {height}" role="img" aria-label="{escape(stack_alt(groups))}">',
                f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="8" '
                f'fill="{colors["bg"]}" stroke="{colors["border"]}"/>',
                f'<path d="M1 {body}H{WIDTH - 1}V{height - 9}a8 8 0 0 1-8 8H9a8 8 0 0 1-8-8Z" '
                f'fill="{colors["foot"]}"/>',
                f'<line x1="1" y1="{body}" x2="{WIDTH - 1}" y2="{body}" stroke="{colors["rule"]}"/>',
                *parts,
                f'<circle cx="28" cy="{body + 17}" r="4" fill="{colors["live"]}"/>'
                f'<text x="40" y="{body + 21}" font-family="{MONO}" font-size="12" '
                f'fill="{colors["sub"]}">in production · the rest is used in a public repository above</text>',
                "</svg>",
            ]
        )
        + "\n"
    )


def stack_alt(groups):
    def names(group):
        return [f"{name} (in production)" for name in group["production"]] + group[
            "public"
        ]

    return "Stack: " + "; ".join(
        f"{group['label']}: {', '.join(names(group))}" for group in groups
    )


def alt_text(tiles):
    return "Metrics: " + "; ".join(f"{tile['value']} {tile['label']}" for tile in tiles)


def update_readme(tiles, groups, today):
    text = README_PATH.read_text(encoding="utf-8")
    text = re.sub(r'alt="Metrics:[^"]*"', f'alt="{escape(alt_text(tiles))}"', text)
    text = re.sub(r'alt="Stack:[^"]*"', f'alt="{escape(stack_alt(groups))}"', text)
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
        (ROOT / "profile" / f"stack-{theme}.svg").write_text(
            draw_stack(config["stack"], colors), encoding="utf-8"
        )
    CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    update_readme(tiles, config["stack"], today)


if __name__ == "__main__":
    main()
