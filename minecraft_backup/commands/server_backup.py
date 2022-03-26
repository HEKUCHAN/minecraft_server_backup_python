import pathlib
from fabric.colors import red
from minecraft_backup.convenience.files import Files, CompressType


def backup(args):
    MINECRAFT_FOLDER_PATH: pathlib.Path = pathlib.Path(args.minecraft_folder)
    BACKUP_FOLDER_PATH: pathlib.Path = pathlib.Path(args.backup_folder)
    IS_NO_LOG: bool = args.no_log

    if args.zip:
        COMPRESS_TYPE: CompressType = CompressType.ZIP
    elif args.tar:
        COMPRESS_TYPE: CompressType = CompressType.TAR
    elif args.tar_zip:
        COMPRESS_TYPE: CompressType = CompressType.TAR_AND_ZIP
    else:
        COMPRESS_TYPE: CompressType = CompressType.NONE

    is_can_backup_result = Files.is_can_backup(
        MINECRAFT_FOLDER_PATH, BACKUP_FOLDER_PATH
    )

    if is_can_backup_result["result"]:
        files: Files = Files(
            MINECRAFT_FOLDER_PATH, BACKUP_FOLDER_PATH, COMPRESS_TYPE, IS_NO_LOG
        )
    else:
        print(red(is_can_backup_result["message"]))
        return

    files.backup()
