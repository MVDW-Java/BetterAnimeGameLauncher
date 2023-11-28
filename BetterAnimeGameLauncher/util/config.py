from BetterAnimeGameLauncher import *

import os
import ruamel.yaml

yaml = ruamel.yaml.YAML();
def getConfig():
    if not os.path.exists(PATH_CONFIG_FILE):
        createConfig()
    with open(PATH_CONFIG_FILE, 'r') as file:
        CONFIG.update(yaml.load(file))
                
def saveConfig():
    with open(PATH_CONFIG_FILE, 'w') as file:
        yaml.dump(CONFIG, file)
    
def createConfig():
    if not os.path.exists(PATH_CONFIG_DIR):
        os.makedirs(PATH_CONFIG_DIR)

    local_file = open(os.path.join(PATH_MAIN_DIR, "static", "config.yaml"), "r")
    local_data = local_file.read()
    local_file.close()

    config_file = open(PATH_CONFIG_FILE, "w")
    config_file.write(local_data)
    config_file.close()
