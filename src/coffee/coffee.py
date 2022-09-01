"""Main module for the Coffee application."""
import time

from coffee.manipulation import enter_input


def keep_alive(time_between_actions_in_seconds: int, perform_n_times: int = 99999999):
    """Perform some action to maintain a resemblance of life."""
    for i in range(perform_n_times):
        enter_input("numlock")
        enter_input("numlock")
        time.sleep(time_between_actions_in_seconds)