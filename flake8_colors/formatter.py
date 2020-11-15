from flake8.formatting import base
import sys
from re import sub


COLORS = dict(
    black=0,
    red=1,
    green=2,
    yellow=3,
    blue=4,
    purple=5,
    cyan=6,
    white=7
)

SUFFIXES = dict(
    fg='0;',
    bold='1;',
    underline='4;',
    bg=''
)

MODS = dict(
    reset='0',
    bold='1',
    underline='4',
)


class ColorFormatter(base.BaseFormatter):
    name = 'flake8-colors'
    version = '0.1.7'

    @classmethod
    def parse_options(cls, options):
        # Only use color formatting if invoked interactively
        if sys.__stdin__.isatty():
            options.format = sub(r'\$\{([\w]+)\}', cls._replace, options.format)
        else:
            options.format = 'default'

    @classmethod
    def _replace(cls, match):
        return '\x1b[' + cls._parse(match.group(1)) + 'm'

    @classmethod
    def _parse(cls, var):
        if var in MODS:
            return MODS.get(var)

        color, _, suffix = var.partition('_')
        if not suffix:
            suffix = 'fg'
        return SUFFIXES.get(suffix) + str(COLORS.get(color) + (30 if suffix in ('fg', 'bold', 'underline') else 40))
