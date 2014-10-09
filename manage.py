#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tdd_django.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
>>>>>>> a577689019d9d6f1987089fdd77c97b2870c12bc

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
