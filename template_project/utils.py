import os
import logging

_LOG = logging.getLogger(__name__)


def str2bool(value, allow_none=False):
    if value is None:
        assert allow_none, "str2bool received None value while allow_none=False"
        return value
    return bool(value) if isinstance(value, (int, bool)) else bool(distutils.util.strtobool(value))


PRINT = str2bool(os.environ.get("MICROTVM_API_PRINT", False))
_LOG.setLevel(logging.INFO if PRINT else logging.WARNING)

def check_call(cmd_args, *args, quiet: bool = True, **kwargs):
    cwd_str = "" if "cwd" not in kwargs else f" (in cwd: {kwargs['cwd']})"
    _LOG.info("run%s: %s", cwd_str, " ".join(shlex.quote(str(a)) for a in cmd_args))
    if quiet:
        kwargs["stderr"] = subprocess.DEVNULL
        kwargs["stdout"] = subprocess.DEVNULL
    return subprocess.check_call(cmd_args, *args, **kwargs)


def debug_print(*args, **kwargs):
    if PRINT:
        print(*args, **kwargs)
