stderr=open("/dev/tty","w")

try:
    print("Loading",file=stderr)
    import sys
    sys.modules.pop("wx",None)
    sys.modules.pop("wx.__version__",None)
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
