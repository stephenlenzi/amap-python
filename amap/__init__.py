__version__ = "0.0.10a3"

__author__ = "Adam Tyson, Charly Rousseau, Christian Niedworok"
__license__ = "GPL-3.0"

from . import *

import luddite
from packaging import version

most_recent_version = luddite.get_version_pypi("amap")

if version.parse(__version__) < version.parse(most_recent_version):
    print(f"This version of amap ({__version__}) is not the most recent "
          f"version. Please update to v{most_recent_version} by running: "
          f"'pip install amap --upgrade'")