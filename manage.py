#!/usr/bin/env python
import os
import sys

import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()

    os.environ.setdefault(
        "config.settings." + os.environ.get("ENVIRONMENT_MODULE", "develop"),
        "config.settings.develop")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
