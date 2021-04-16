import re
import os


def extract(regularE : str, init : str, stop : str, string : str):
    """
        regularE:   RE to catch string
        init:       First string to replace
        stop:       Last string to replace
        string:     String to apply the RE
    
    With a regular expression and init and stop to replace, gets a
    substring from string argument and returns it.
    """
    return re.findall(regularE, string)[0]\
             .replace(init, "")\
             .replace(stop, "")


def get_term_clock_pid():
    """
        return: int with the PID of term_clock;
                -1 if process doesn't exist.

    Extracts the PID of term_clock process with systemctl.
    """
    # sputnikDriver prints in their own console all the PIDs of its subprocesses
    ret = os.popen("systemctl status sputnikDriver.service").read()
    if ret == "":
        return -1
    return int(extract(r"term_clock .+ PID", "term_clock ", " PID", ret))


def check_alive():
    """
        return: True if java process is running;
                False otherwise

    Check if a java process in sputnikDriver (i.e. the Minecraft Server) is running
    """
    ret = os.popen("systemctl status sputnikDriver.service").read()
    return "java" in ret
