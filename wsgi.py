import sys
from os.path import abspath
from os.path import dirname
import ResumeCenterSystem

sys.path.insert(0, abspath(dirname(__file__)))


application = ResumeCenterSystem.app.configured_app()