import sys
import os

from BetterAnimeGameLauncher.cli.arg_manager import argumentManager 
from BetterAnimeGameLauncher.cli.runner import runner 

def main() -> int:
    args = argumentManager()
    runner(args);
    return 0;


if __name__ == '__main__':
    sys.exit(main())
