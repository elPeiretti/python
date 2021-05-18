import win32gui
import win32api
import win32con
# https://docs.microsoft.com/en-us/windows/win32/inputdev/mouse-input-notifications

# Simulates left click at position (x,y), in the window handled by hWnd
def leftClick(x, y, hWnd):

    lParam = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)

# Simulates right click at position (x,y), in the window handled by hWnd
def rightClick(x, y, hWnd):

    lParam = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32gui.SendMessage(hWnd, win32con.WM_RBUTTONUP, None, lParam)

# Simulates key press, in the window handled by hWnd
# argument key should be a keycode, e.g VK_ESCAPE
# https://github.com/SublimeText/Pywin32/blob/master/lib/x32/win32/lib/win32con.py
def pressKey(key,hWnd):
    win32gui.SendMessage(hWnd,win32con.WM_KEYDOWN, key,0)
    win32gui.SendMessage(hWnd,win32con.WM_KEYUP, key,0)
