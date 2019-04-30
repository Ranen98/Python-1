import win32api
import win32con

def airKeyboard():
    win32api.keybd_event(18, 0, 0, 0)
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)

airKeyboard()