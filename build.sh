#!/bin/bash
pyinstaller -D -F -F -n BAGL --add-data "./BetterAnimeGameLauncher:." -c ./BetterAnimeGameLauncher/__main__.py
if [[ $1 == "install" ]]; then
	if [ "$EUID" -ne 0 ]; then
		echo "Please run as root"
	else
		cp "$(pwd)/dist/BAGL" "/usr/local/bin"
		ln -s /usr/local/bin/BAGL /usr/local/bin/bagl
	fi
fi
echo "--------------"
echo "output in: $(pwd)/dist" 
