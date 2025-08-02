from bagl import *

from bagl.util.localResources import resourcePath

import argparse
import yaml
import os

def argumentManager():

    args_filepath = os.path.abspath(os.path.join("cli", "bagl_cli", "args.yaml"))

    type_mapping = {
        'str': str,
        'int': int,
        'bool': bool
    }

    with open(args_filepath, 'r') as file:
        args = yaml.safe_load(file)
        ap = argparse.ArgumentParser(
            prog="BetterAnimeGameLauncher",
            usage="A launcher for anime games by that one game studio.",
            epilog="Need support? Join our Discord server",
            allow_abbrev=True,
        )

        for arg_config in args:
            arg_name = arg_config["name"]
            arg_type_str = arg_config.get("type", "str")
            arg_type = type_mapping.get(arg_type_str, str)
            arg_config.pop("name")
            arg_config.pop("type")

            ap.add_argument(arg_name, type=arg_type, **arg_config)

    return ap.parse_args()
