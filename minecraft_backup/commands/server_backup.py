import pathlib
from fabric.colors import red
from minecraft_backup.convenience.files import Files


def backup(args):
    MINECRAFT_FOLDER_PATH: pathlib.Path = pathlib.Path(args.minecraft_folder)
    BACKUP_FOLDER_PATH: pathlib.Path = pathlib.Path(args.backup_folder)
    IS_NO_LOG: bool = args.no_log

    is_can_backup_result = Files.is_can_backup(
        MINECRAFT_FOLDER_PATH, BACKUP_FOLDER_PATH
    )

    if is_can_backup_result["result"]:
        files: Files = Files(MINECRAFT_FOLDER_PATH, BACKUP_FOLDER_PATH, IS_NO_LOG)
    else:
        print(red(is_can_backup_result["message"]))
        return

    print(is_can_backup_result)
    print(files)
