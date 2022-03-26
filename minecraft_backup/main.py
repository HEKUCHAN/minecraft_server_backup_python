# -*- coding: utf-8 -*-
import argparse
from . import commands


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="""\
        This is a backup management library for Minecraft servers.
        It should be run and used on a regular basis using cron or similar.
        """
    )

    subparser: argparse._SubParsersAction = parser.add_subparsers(
        dest="command", help="Normal Command"
    )

    # Backup Commands
    parser_backup: argparse.ArgumentParser = subparser.add_parser(
        "backup", help="Command to backup your minecraft folder. see `backup -h`"
    )
    parser_backup.set_defaults(handler=commands.backup)

    parser_backup.add_argument(
        "minecraft_folder", help="Write the Minecraft folder path."
    )

    parser_backup.add_argument(
        "backup_folder", help="Write the folder path should you want save buckup."
    )

    parser_backup.add_argument(
        "--no-log", help="Mode to not save the backup log.", action="store_true"
    )

    parser_backup_group = parser_backup.add_mutually_exclusive_group()
    parser_backup_group.add_argument(
        "-z", "--zip", help="Mode to save and compress in zip", action="store_true"
    )

    parser_backup_group.add_argument(
        "-t",
        "--tar",
        help="Mode to save and compress to tgz/tar.gz",
        action="store_true",
    )

    parser_backup_group.add_argument(
        "-tz",
        "--tar-zip",
        help="Mode to save and compress to zip and tgz/tar.gz",
        action="store_true",
    )

    # log Commands
    parser_log: argparse.ArgumentParser = subparser.add_parser(
        "clear", help="Clear the all logs of buckup. see `clear -h`"
    )
    parser_log.set_defaults(handler=commands.clear)

    # Config Commands
    parser_config: argparse.ArgumentParser = subparser.add_parser(
        "config",
        help="You can change or check the config of backup management. see `config -h`",
    )
    parser_config.set_defaults(handler=commands.config)

    parser_config.add_argument(
        "--logs-path",
        help="You can change the path of logs. (Default path is the Minecraft directory) Warning! When you use this command you will be lost your log data. I recommend saving the files if you need to do it before doing it.",
    )

    parser_config.add_argument(
        "--delete-target",
        help="Setting of auto delete target. Example: 7d,00h,00m,00s (Default 7d)",
    )

    parser_config.add_argument("--autodelete", help="You can turn off/on auto delete.")

    args = parser.parse_args()

    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
