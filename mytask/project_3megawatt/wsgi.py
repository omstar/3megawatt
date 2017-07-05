"""
WSGI config for project_3megawatt project.
"""

import os
import sys
import site

sys.stdout = sys.stderr

# Project root
root = '/var/www/www.3megawatt.com/mytask/'
sys.path.insert(0, root)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_3megawatt.settings")

# Packages from virtualenv
activate_this = '/var/www/www.3megawatt.com/venv/stage/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# Set environmental variable for Django and fire WSGI handler 
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_3megawatt.settings'
os.environ["CELERY_LOADER"] = "django"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
