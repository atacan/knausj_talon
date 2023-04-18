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
        if number > 9:  # 9 is the last desktop BTT has
            return
        action_number = 206 + number
        applescript.run(
            """
            tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 211}"
            """.replace("211", str(action_number))
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
        if desktop_number > 9:  # 9 is the last desktop BTT has
            return
        actions = {1: 216,
                   2: 217,
                   3: 218,
                   4: 219,
                   5: 220,
                   6: 222,
                   7: 223,
                   8: 224,
                   9: 225, }
        applescript.run(
            """
            tell application "BetterTouchTool" to trigger_action "{\\"BTTPredefinedActionType\\": 211}"
            """.replace("211", str(actions[desktop_number]))
        )
