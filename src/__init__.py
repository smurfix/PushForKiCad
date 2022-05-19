stderr=open("/dev/tty","w")

# On some Linux based systems site-packages are placed in a different directory.
# KiCad only appends the system-wide directory to path,
# because of this we add the user-wide directory, too.
from sys import path
import os
path.append(os.path.expanduser('~/.local/lib/python3.9/site-packages'))

print("Loading",file=stderr)
import sys
sys.modules.pop("wx",None)
sys.modules.pop("wx.__version__",None)

try:
    from .plugin import PushForKiCadPlugin
    plugin = PushForKiCadPlugin()
    plugin.register()
    print("OK",file=stderr)
except BaseException as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))
    import traceback
    traceback.print_exc(file=stderr)
    raise
