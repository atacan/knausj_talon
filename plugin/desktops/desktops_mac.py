import contextlib
import time

from talon import Context, actions, ctrl, ui
from talon.mac import applescript

ctx = Context()
ctx.matches = r"""
os: mac
"""


@contextlib.contextmanager
def _drag_window_mac(win=None):
    if win is None:
        win = ui.active_window()
    fs = win.children.find(AXSubrole="AXFullScreenButton")[0]
    rect = fs.AXFrame["$rect2d"]
    x = rect["x"] + rect["width"] + 5
    y = rect["y"] + rect["height"] / 2
    ctrl.mouse_move(x, y)
    ctrl.mouse_click(button=0, down=True)
    yield
    time.sleep(0.1)
    ctrl.mouse_click(button=0, up=True)


@ctx.action_class("user")
class MacActions:
    def desktop(number: int):
        applescript.run(
            """
            tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 211}"
            """
        )

    def desktop_next():
        applescript.run(
            """
        tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 114}"
        """
        )

    def desktop_last():
        applescript.run(
            """
            tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 113}"
            """
        )

    def desktop_show():
        applescript.run(
            """
            tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 165}"
            """
        )

    def window_move_desktop_left():
        applescript.run(
            """
                tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 151}"
            """
        )

    def window_move_desktop_right():
        applescript.run(
            """
                tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 152}"
            """
        )

    def window_move_desktop(desktop_number: int):
        if ui.apps(bundle="com.amethyst.Amethyst"):
            actions.key(f"ctrl-alt-shift-{desktop_number}")
        else:
            with _drag_window_mac():
                actions.key(f"ctrl-{desktop_number}")