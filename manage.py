#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    
    # Load the Heroku environment.
    from herokuapp.env import load_env
    load_env(__file__, "fleischer-films")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fleischer_films.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
