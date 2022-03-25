# -*- coding: utf-8 -*-
import os
import sys
import argparse


def command_backup(args):
    print(args, "backup!!")


def command_log_clear(args):
    print(args, "clear!!")


def main():
    parser = argparse.ArgumentParser(
        description="""\
        This is a backup management library for Minecraft servers.
        It should be run and used on a regular basis using cron or similar.
        """
    )

    subparser = parser.add_subparsers(dest="command", help="Normal Command")

    # Backup Commands
    parser_backup = subparser.add_parser(
        "backup", help="Command to backup your minecraft folder. see `backup -h`"
    )
    parser_backup.set_defaults(handler=command_backup)

    parser_backup.add_argument(
        "minecraft_folder", help="Write the Minecraft folder path."
    )

    parser_backup.add_argument(
        "backup_folder", help="Write the folder path should you want save buckup."
    )

    parser_backup.add_argument(
        "--no-log", help="Mode to not save the backup log.", action="store_true"
    )

    # log Commands
    parser_log = subparser.add_parser(
        "clear", help="Clear the all logs of buckup. see `clear -h`"
    )
    parser_log.set_defaults(handler=command_log_clear)

    # Config Commands
    parser_config = subparser.add_parser(
        "config", help="Change the config of backup management"
    )

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
