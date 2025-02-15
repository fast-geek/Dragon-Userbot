import configparser
import os
import sys
from sys import version_info

from .db import db

modules_help = []
requirements_list = []

github = "<a href=https://github.com/Dragon-Userbot/Dragon-Userbot> github</a>"
license = (
    "<a href=https://github.com/Dragon-Userbot/Dragon-Userbot/blob/master/LICENSE> GNU"
    " General Public License v3.0</a>"
)
copyright = (
    "© <a href=https://github.com/Dragon-Userbot>Dragon-Userbot company</a>, 2021"
)
python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
version = "2.0.2"

config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

pr = db.get("core.main", "prefix")
if pr is None:
    db.set("core.main", "prefix", ".")
    prefix = "."
else:
    prefix = pr
