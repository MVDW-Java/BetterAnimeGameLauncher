#!/bin/bash
pyinstaller -D -F -F -n BAGL --add-data "./BetterAnimeGameLauncher:." -c ./BetterAnimeGameLauncher/__main__.py
echo "--------------"
echo "output in: $(pwd)/dist" 
