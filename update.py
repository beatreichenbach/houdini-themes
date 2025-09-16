from __future__ import annotations

import logging
import os
import re

logger = logging.getLogger()


def log_differences() -> None:
    """Log the differences between the config in this repo and the original configs."""

    houdini_dir = r'C:\Program Files\Side Effects Software\Houdini 21.0.440'
    source_config_dir = os.path.join(houdini_dir, 'houdini', 'config')

    root = os.path.dirname(__file__)
    dest_config_dir = os.path.join(root, 'source')

    files = (
        ('UIDark.hcs', 'UIDark.yml'),
        ('NodeGraphDark.inc', 'NodeGraphDark.yml'),
        ('NodeGraphCommon.inc', 'NodeGraphCommon.yml'),
    )
    for source, dest in files:
        keys_source = get_keys(os.path.join(source_config_dir, source))
        keys_dest = get_keys(os.path.join(dest_config_dir, dest))
        difference = [k_s for k_s in keys_source if k_s not in keys_dest]
        logger.info(f'Keys not in {dest}:')
        for key in difference:
            logger.info(f'  {key}')


def get_keys(path: str) -> tuple[str, ...]:
    """Return all keys from a config file."""

    keys = []
    with open(path, 'r') as file:
        for line in file.readlines():
            if match := re.match(r'(.*?):', line):
                keys.append(match.group(1))

    return tuple(keys)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    log_differences()
