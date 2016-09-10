from pydgutils_bootstrap import use_pydgutils
use_pydgutils()

import pydgutils
import os
import sys

source_dir = pydgutils.process()

source_dir = os.path.realpath(os.path.abspath(source_dir))
if source_dir not in sys.path:
    sys.path.insert(0, source_dir)

from docker_maintain.__main__ import main

if __name__ == "__main__":
    main()
