from importlib.metadata import version

import click
from py_cli.sub import sub

try:
    __version__ = version("py-cli")
except Exception:  # noqa
    __version__ = "0.0.0"

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


def main() -> None:
    cmd.add_command(sub)
    cmd()


def print_version(ctx, param, value):  # noqa
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
)
def cmd() -> None:
    """
    Sample Command line tool
    """
