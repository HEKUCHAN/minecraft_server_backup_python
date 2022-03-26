import os
import json
import minecraft_backup
from minecraft_backup.config import *
from pathlib import Path
from typing import TypeVar, Generic
from logging import getLogger, config, Logger

T = TypeVar("T")

if os.path.exists(LOG_CONFIG_PATH):
    with open(LOG_CONFIG_PATH, "r") as f:
        log_conf = json.load(f)
else:
    raise FileNotFoundError(LOG_CONFIG_PATH)

logger: Logger = getLogger(__name__)

if log_conf["handlers"]["fileHandler"]["filename"] == "to be replaced":
    log_conf["handlers"]["fileHandler"]["filename"] = LOG_FILE_PATH

config.dictConfig(log_conf)


class Log(Generic[T]):
    pass
