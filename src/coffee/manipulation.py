"""Main manipulation module."""
import pyautogui
import time


pyautogui.FAILSAFE = False


def move_to_position(x: int, y: int):
    pyautogui.moveTo(x, y)


def enter_input(input):
    """Enter some keyboard input, like a user."""
    pyautogui.press(input)


def keep_alive(time_between_actions_in_seconds: int, perform_n_times: int = 99999999):
    """Perform some action to maintain a resemblance of life."""
    for i in range(perform_n_times):
        cursor_position = pyautogui.position()
        move_to_position(cursor_position.x + 1, cursor_position.y)
        move_to_position(cursor_position.x, cursor_position.y)
        print(f"wiggle {i}")
        time.sleep(time_between_actions_in_seconds)
