"""
Settings used by fleischer_films project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from fleischer_films.settings.production import *

# Import optional local settings.
try:
    from fleischer_films.settings.local import *
except ImportError:
    pass