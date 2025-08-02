from bagl import *

from .arg_manager import argumentManager
from .runner import runner

import sys
import os

def main():
    # Check if system is supported (Sorry BSD users, maybe when I have some time)
    supported_platforms = ["Linux", "Darwin", "Windows"]
    if PLATFORM_NAME not in supported_platforms:
        print(f"error: platform '{PLATFORM_NAME}' is not a supported")
        sys.exit(1)


    args = argumentManager()
    runner(args);
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())
