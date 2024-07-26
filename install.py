import os
import sys
import time


def Log(textMessage, format="INSTALL"):
    RED, GREEN, MAGENTA = '\033[91m', '\033[92m', '\033[95m'
    GREY, CYAN, END     = '\033[90m', '\033[96m', '\033[0m' # NOQA
    tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if   format == "INSTALL": COLOR = GREEN   # NOQA
    elif format == "ERROR"  : COLOR = RED     # NOQA
    elif format == "WARN"   : COLOR = MAGENTA # NOQA
    else:  COLOR = CYAN                       # NOQA
    log_format = f"[{GREY}{tm}{END}] - [{COLOR}{format}{END}] - {textMessage}"
    print(log_format)


def run_command(command):
    exit_code = os.system(command)
    if exit_code != 0:
        Log(f"Command failed with exit code: {exit_code}", "ERROR")
        sys.exit(1)


def upgrade_deps(pyExec):
    Log(f"Upgrading pip and installing dependencies...", "INFO")
    run_command(f"{pyExec} -m pip install --upgrade pip setuptools wheel")


def install_package(pyExec):
    Log("Installing the Package in User Environment...")
    run_command(f"{pyExec} -m pip install . --user")


def main():
    current_platform = sys.platform
    pyExec = sys.executable
    Log(f"Detected platform: {current_platform}", "INFO")

    if len(sys.argv) > 1 and sys.argv[1] == "upgrade":
        upgrade_deps(pyExec)
        return

    if current_platform.startswith('win'):
        upgrade_deps(pyExec)
        install_package(pyExec)
        Log("Installation on Windows completed successfully.")
    elif current_platform.startswith('linux'):
        upgrade_deps(pyExec)
        install_package(pyExec)
        Log("Installation on Linux completed successfully.")
    elif current_platform.startswith('darwin'):
        upgrade_deps(pyExec)
        install_package(pyExec)
        Log("Installation on macOS completed successfully.")
    else:
        Log(f"Unsupported platform: {current_platform}", "ERROR")
        sys.exit(1)


if __name__ == '__main__':
    main()
