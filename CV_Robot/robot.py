import requests

try:
    # noinspection PyShadowingBuiltins
    from printlog import printlog as print
except ImportError:
    pass

from CV_Robot import is_Robot, robot_URL

def forward():
    """
    Moves robot forward at speed set by speed command.

    Runs emulated code if GPIO backend not found.
    """
    print("Driving forward...")
    if is_Robot:
        requests.get('http://' + robot_URL + '/forward')


def backward():
    """
    Moves robot backward at speed set by speed command.

    Runs emulated code if GPIO backend not found.
    """
    print("Driving backward...")
    if is_Robot:
        requests.get('http://' + robot_URL + '/reverse')

def left():
    """
    Turns robot left at speed set by speed command.

    Runs emulated code if GPIO backend not found.
    """
    print("Turning left...")
    if is_Robot:
        requests.get('http://' + robot_URL + '/left')

def right():
    """
    Turns robot right at speed set by speed command.

    Runs emulated code if GPIO backend not found.
    """
    print("Turning right...")
    if is_Robot:
        requests.get('http://' + robot_URL + '/right')

def stop():
    """
    Sets speed of all motors to 0.

    Runs emulated code if GPIO backend not found.
    """
    print("Stopping robot...")
    if is_Robot:
        requests.get('http://' + robot_URL + '/stop')

def speed(val):
    """
    Sets driving speed to value specified
    """
    if is_Robot:
        requests.get('http://' + robot_URL + '/speed?val=' + str(val))