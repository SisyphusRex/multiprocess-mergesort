#!/usr/bin/env python
"""Bootstrap file"""

# System Imports
import sys

# first party imports
from program import main


def run(*args):
    """Main entry point for program"""
    # Call the main method for the program
    main(*args)


# Prevent running on import.
if __name__ == "__main__":
    run(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it!")
