from __future__ import annotations

import dataclasses
import json
import logging
import os

from PySide6 import QtGui, QtWidgets

logger = logging.getLogger()


@dataclasses.dataclass
class Theme:
    primary: QtGui.QColor | None = None
    secondary: QtGui.QColor | None = None

    magenta: QtGui.QColor | None = None
    red: QtGui.QColor | None = None
    orange: QtGui.QColor | None = None
    yellow: QtGui.QColor | None = None
    green: QtGui.QColor | None = None
    cyan: QtGui.QColor | None = None
    blue: QtGui.QColor | None = None

    text: QtGui.QColor | None = None
    subtext1: QtGui.QColor | None = None
    subtext0: QtGui.QColor | None = None
    overlay2: QtGui.QColor | None = None
    overlay1: QtGui.QColor | None = None
    overlay0: QtGui.QColor | None = None
    surface2: QtGui.QColor | None = None
    surface1: QtGui.QColor | None = None
    surface0: QtGui.QColor | None = None
    base: QtGui.QColor | None = None
    mantle: QtGui.QColor | None = None
    crust: QtGui.QColor | None = None

    def is_dark_theme(self) -> bool:
        return self.text.value() > self.base.value()


def _load(path: str) -> Theme:
    """
    Return the theme from `path`.

    :raises FileNotFoundError: If the theme cannot be found.
    :raises TypeError: If the theme has unexpected data.
    :raises JSONDecodeError: If the theme is invalid json.
    """

    with open(str(path)) as f:
        data = json.load(f)
    colors = {key: QtGui.QColor(value) for key, value in data.items()}
    return Theme(**colors)


def create_color_theme(name: str, output: str) -> None:
    """"""

    root = os.path.dirname(__file__)

    theme_path = os.path.join(root, 'themes', f'{name}.json')
    theme = _load(theme_path)

    if not os.path.exists(output):
        os.makedirs(output)

    config_dir = os.path.join(root, 'config')
    if theme.is_dark_theme():
        ui_file_source = os.path.join(config_dir, 'UIDark.hcs')
        node_graph_source = os.path.join(config_dir, 'NodeGraphDark.inc')
    else:
        ui_file_source = os.path.join(config_dir, 'UILight.hcs')
        node_graph_source = os.path.join(config_dir, 'NodeGraphLight.inc')
    basic_colors_source = os.path.join(config_dir, 'basic_colors.inc')
    node_graph_common_source = os.path.join(config_dir, 'NodeGraphCommon.inc')

    ui_file_dest = os.path.join(output, f'{name}.hcs')
    basic_colors_dest = os.path.join(output, f'{name}_basic_colors.inc')
    node_graph_dest = os.path.join(output, f'{name}_node_graph.inc')
    node_graph_common_dest = os.path.join(output, f'{name}_node_graph_common.inc')

    data = dataclasses.asdict(theme)
    data['name'] = name
    data['basic_colors'] = os.path.basename(basic_colors_dest)
    data['node_graph'] = os.path.basename(node_graph_dest)
    data['node_graph_common'] = os.path.basename(node_graph_common_dest)

    write_file(ui_file_source,  ui_file_dest, data)
    write_file(basic_colors_source,  basic_colors_dest , data)
    write_file(node_graph_source,  node_graph_dest, data)
    write_file(node_graph_common_source,  node_graph_common_dest , data)


def write_file(source: str, dest: str, data: dict) -> None:
    """Write a file by updating the source from the theme."""

    with open(source, 'r') as f:
        text = f.read()

    with open(dest, 'w') as f:
        f.write(text.format(**data))


create_color_theme('one_dark_two', r'D:\files\settings\houdini\houdini21.0\config')
