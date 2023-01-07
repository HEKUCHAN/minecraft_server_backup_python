import yaml
from pydrive.auth import GoogleAuth, GoogleDrive
from fabric.colors import red
from .user_config import Config
from minecraft_backup.config import PYDRIVE_SETTING_FILE_PATH, PYDRIVE_CREDENTIALS_FILE_PATH

class Drive:
    def __init__(self):
        config_check = Config.check_google_drive_file()

        if not config_check["result"]:
            print(red(config_check["message"]))
            self.create_pydrive_init_file()

        self.gauth = GoogleAuth(
            settings_file=Config.get_pydrive_setting_file_path()
        )
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    @classmethod
    def create_pydrive_init_file(cls):
        yaml_temaplte = {
            "client_config_backend": "settings",
            "client_config": {
                "client_id": None,
                "client_secret": None
            },
            "save_credentials": True,
            "save_credentials_backend": "file",
            "save_credentials_file": str(PYDRIVE_CREDENTIALS_FILE_PATH),
            "get_refresh_token": True,
            "oauth_scope":[
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive.install",
            ]
        }

        client_id = input("GoogleDrive client_id: ")
        client_secret = input("GoogleDrive client_secret: ")

        yaml_temaplte["client_config"]["client_id"] = client_id
        yaml_temaplte["client_config"]["client_secret"] = client_secret

        with open(PYDRIVE_SETTING_FILE_PATH, 'w') as file:
            yaml.dump(yaml_temaplte, file)
        Config.change_pydrive_setting_file_path(PYDRIVE_SETTING_FILE_PATH)
        
