from __future__ import annotations

import dataclasses
import json
import logging
import os
import sys

from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger()


@dataclasses.dataclass
class Theme:
    primary: str
    secondary: str

    magenta: str
    red: str
    orange: str
    yellow: str
    green: str
    cyan: str
    blue: str

    text: str
    subtext1: str
    subtext0: str
    overlay2: str
    overlay1: str
    overlay0: str
    surface2: str
    surface1: str
    surface0: str
    base: str
    mantle: str
    crust: str


def mix(color1: str, color2: str, weight: float) -> str:
    values1 = color1.replace('#', '')
    values2 = color2.replace('#', '')
    rgb1 = tuple(int(values1[i:i+2], 16) for i in (0, 2, 4))
    rgb2 = tuple(int(values2[i:i+2], 16) for i in (0, 2, 4))
    mixed_rgb = tuple(
        int((1 - weight) * c1 + weight * c2) for c1, c2 in zip(rgb1, rgb2)
    )
    mixed_color = '#{:02X}{:02X}{:02X}'.format(*mixed_rgb)
    return mixed_color


def load_theme(path: str) -> Theme:
    """
    Return the theme from `path`.

    :raises FileNotFoundError: If the theme cannot be found.
    :raises TypeError: If the theme has unexpected data.
    :raises JSONDecodeError: If the theme is invalid JSON.
    """

    with open(str(path)) as f:
        data = json.load(f)
    theme = Theme(**data)
    return theme


def create_config(theme_path: str, output: str) -> None:
    """Create a ColorScheme Config from a theme."""

    logger.debug(f'Loading theme: {theme_path}')
    theme = load_theme(theme_path)

    name, ext = os.path.splitext(os.path.basename(theme_path))
    data = {k: v.upper() for k, v in dataclasses.asdict(theme).items()}
    data['name'] = name
    data['mix'] = mix
    data['gradient'] = False

    # Render template
    root = os.path.dirname(__file__)
    source_dir = os.path.join(root, 'source')
    env = Environment(loader=FileSystemLoader(source_dir))
    template = env.get_template('UIDark.yml')
    result = template.render(**data)

    # Write config
    if not os.path.exists(output):
        os.makedirs(output)
    dest = os.path.join(output, f'{name}.hcs')
    with open(dest, 'w') as f:
        f.write(result)

    logger.info(f'Created config: {dest}')


def create_configs(output_dir: str) -> None:
    """Create ColorScheme Configs for all themes in this repo."""

    root = os.path.dirname(__file__)
    themes_dir = os.path.join(root, 'themes')

    for file in os.listdir(themes_dir):
        theme_path = os.path.join(themes_dir, file)
        create_config(theme_path, output_dir)

    logger.info('All configs created.')


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) > 1:
        output_dir = os.path.expandvars(os.path.expanduser(sys.argv[1]))
        output_dir = os.path.normpath(output_dir)
    else:
        output_dir = os.path.join(os.path.dirname(__file__), 'config')

    create_configs(output_dir)


if __name__ == '__main__':
    main()
