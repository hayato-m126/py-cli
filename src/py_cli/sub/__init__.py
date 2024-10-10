import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
def sub() -> None:
    """Sub command"""


@sub.command(context_settings=CONTEXT_SETTINGS)
def hello() -> None:
    from command import hello as hello_cmd

    hello_cmd()
