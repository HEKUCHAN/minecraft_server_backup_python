import os
import textwrap
from pathlib import Path
from typing import TypeVar, Generic, Dict, Union

T = TypeVar("T")


class Files(Generic[T]):
    def __init__(
        self, minecraft_folder: Union[str, Path], backup_folder: Union[str, Path], is_no_log: bool
    ):
        if type(minecraft_folder) == str or type(backup_folder) == str:
            minecraft_folder = Path(minecraft_folder).resolve()
            backup_folder = Path(backup_folder).resolve()
        else:
            minecraft_folder = minecraft_folder.resolve()
            backup_folder = backup_folder.resolve()

        if minecraft_folder == backup_folder:
            raise TypeError(
                "The minecraft folder path and backup folder path shouldn't be the same."
            )

        self.minecraft_folder: Union[str, Path] = minecraft_folder
        self.backup_folder: Union[str, Path] = backup_folder
        self.is_no_log: bool = is_no_log

    def backup_folder(self):
        pass

    @classmethod
    def is_can_backup(
        cls, minecraft_folder: Union[str, Path], backup_folder: Union[str, Path]
    ) -> Dict[bool, str]:
        if type(minecraft_folder) == str or type(backup_folder) == str:
            minecraft_folder = Path(minecraft_folder).resolve()
            backup_folder = Path(backup_folder).resolve()
        else:
            minecraft_folder = minecraft_folder.resolve()
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
