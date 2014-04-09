#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "video1.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.settings")
>>>>>>> 3c62537489ce022cdb61c08a67fdaa29708f45a4

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
