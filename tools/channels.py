#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Publisher/build configuration only; the installed launcher uses the stock API."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Channel:
    id: str
    name: str
    asset_prefix: str
    tag_prefix: str
    feed_branch: str
    source_branch: str
    prerelease: bool


CHANNELS = {
    'stable': Channel('switch-ui', 'Switch UI', 'SwitchLauncher', 'v',
                      'update-feed', 'main', False),
    'test': Channel('switch-ui-test', 'Switch UI Test', 'SwitchLauncher-Test', 'test-v',
                    'test-update-feed', 'test-versions', True),
    'cartucho': Channel('launcher-cartucho', 'Launcher Cartucho', 'Launcher-Cartucho', 'cartucho-v',
                       'launcher-cartucho-feed', 'spanish-zelda-launcher', True),
}


def config(channel='stable'):
    if channel not in CHANNELS:
        raise ValueError('Unknown release channel: ' + str(channel))
    return CHANNELS[channel]


def for_identifier(identifier):
    for name, channel in CHANNELS.items():
        if channel.id == identifier:
            return name
    raise ValueError('Wrong launcher identity')
