import pathlib
import subprocess
import sys


def run_hooks(hooks_path: pathlib.Path) -> int:
    """
    Run prek using the specified config.

    Args:
        hooks_path: Absolute path of the hooks config file

    Returns:
        The return code of the process
    """
    cmd = [
        "prek",
        "run",
        "--config",
        str(hooks_path),
        "--files",
        *sys.argv[1:],
    ]
    return subprocess.run(cmd, check=False).returncode  # noqa: S603
