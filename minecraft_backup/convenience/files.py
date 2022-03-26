import os
import shutil
import textwrap
import datetime
from pathlib import Path
from enum import IntEnum
from typing import TypeVar, Generic, Dict, Union

from . import logger

T = TypeVar("T")


t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, "JST")
now = datetime.datetime.now(JST)


class CompressType(IntEnum):
    NONE = 0
    ZIP = 1
    TAR = 2
    TAR_AND_ZIP = 4


class File(Generic[T]):
    def __init__(
        self,
        minecraft_folder: Union[str, Path],
        backup_folder: Union[str, Path],
        compress_type: CompressType,
        is_no_log: bool,
    ):
        if type(minecraft_folder) == str:
            minecraft_folder = Path(minecraft_folder).resolve()
        else:
            minecraft_folder = minecraft_folder.resolve()

        if type(backup_folder) == str:
            backup_folder = Path(backup_folder).resolve()
        else:
            backup_folder = backup_folder.resolve()

        if minecraft_folder == backup_folder:
            raise TypeError(
                "The minecraft folder path and backup folder path shouldn't be the same."
            )

        self.minecraft_folder: Union[str, Path] = minecraft_folder
        self.backup_folder: Union[str, Path] = backup_folder
        self.is_no_log: bool = is_no_log
        self.compress_type: CompressType = compress_type

    def backup(self):
        if self.compress_type == CompressType.NONE:
            shutil.copytree(
                self.minecraft_folder,
                self.backup_folder
                / f"{self.minecraft_folder.name}_{now.strftime('%Y-%m-%d_%Hh-%Mm-%Ss')}",
            )
            logger.info(f"{self.minecraft_folder.name}: Backup none compress at {self.backup_folder}")
        elif self.compress_type == CompressType.ZIP:
            shutil.make_archive(
                self.backup_folder
                / f"{self.minecraft_folder.name}_{now.strftime('%Y-%m-%d_%Hh-%Mm-%Ss')}",
                "zip",
                root_dir=self.minecraft_folder,
            )
            logger.info(
                f"{self.minecraft_folder.name}: Backup zip compress at {self.backup_folder}")
        elif self.compress_type == CompressType.TAR:
            shutil.make_archive(
                self.backup_folder
                / f"{self.minecraft_folder.name}_{now.strftime('%Y-%m-%d_%Hh-%Mm-%Ss')}",
                "gztar",
                root_dir=self.minecraft_folder,
            )
            logger.info(
                f"{self.minecraft_folder.name}: Backup tar.gz compress at {self.backup_folder}")
        elif self.compress_type == CompressType.TAR_AND_ZIP:
            shutil.make_archive(
                self.backup_folder
                / f"{self.minecraft_folder.name}_{now.strftime('%Y-%m-%d_%Hh-%Mm-%Ss')}",
                "gztar",
                root_dir=self.minecraft_folder,
            )

            shutil.make_archive(
                self.backup_folder
                / f"{self.minecraft_folder.name}_{now.strftime('%Y-%m-%d_%Hh-%Mm-%Ss')}",
                "zip",
                root_dir=self.minecraft_folder,
            )

            logger.info(
                f"{self.minecraft_folder.name}: Backup zip and tar.gz compress at {self.backup_folder}")

    @classmethod
    def is_can_backup(
        cls, minecraft_folder: Union[str, Path], backup_folder: Union[str, Path]
    ) -> Dict[bool, str]:
        if type(minecraft_folder) == str:
            minecraft_folder = Path(minecraft_folder).resolve()
        else:
            minecraft_folder = minecraft_folder.resolve()

        if type(backup_folder) == str:
            backup_folder = Path(backup_folder).resolve()
        else:
            backup_folder = backup_folder.resolve()

        # Check to avoid the same files.
        if minecraft_folder == backup_folder:
            return {
                "result": False,
                "message": "The minecraft folder path and backup folder path shouldn't be the same.",
            }

        # Check if the file or directory exists.
        if not os.path.exists(minecraft_folder) and not os.path.exists(backup_folder):
            return {
                "result": False,
                "message": "Can't find Minecraft folder and Backup folder.",
            }
        elif not os.path.exists(minecraft_folder):
            return {"result": False, "message": "Can't find Minecraft folder."}
        elif not os.path.exists(backup_folder):
            return {"result": False, "message": "Can't find BackupFolder."}

        # Check if the directory exists by referring to PATH.
        if not os.path.isdir(minecraft_folder) and not os.path.isdir(backup_folder):
            return {
                "result": False,
                "message": "Minecraft folder and Backup folder aren't directory. Please select a directory.",
            }
        elif not os.path.isdir(minecraft_folder):
            return {
                "result": False,
                "message": "Minecraft folder isn't directory. Please select a directory.",
            }
        elif not os.path.isdir(backup_folder):
            return {
                "result": False,
                "message": "Backup folder isn't directory. Plase selct a directory.",
            }

        return {"result": True}

    def __str__(self):
        return textwrap.dedent(
            f"""\
            MinecraftFolder: {self.minecraft_folder}
            BackupFolder: {self.backup_folder}
            """
        )

    def __repr__(self):
        return self
