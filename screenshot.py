# Reference
# https://zhuanlan.zhihu.com/p/97574557
# https://blog.csdn.net/u010906468/article/details/106108906

import win32gui
import win32api
import win32con
import pyautogui
from PIL import Image, ImageGrab

def getTouhouHandle():
        name = "東方妖々夢\u3000～ Perfect Cherry Blossom. ver 1.00b"
        handle = win32gui.FindWindow(0, name)
        if handle == 0:
            raise Exception("你游戏没开")
        else:
            return handle

def listHandle():
    hwnd_title = {}
    def get_all_hwnd(hwnd, _):
        if (win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd)):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(get_all_hwnd, 0)
    print(hwnd_title)
hwnd = getTouhouHandle()
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 强行显示界面后才好截图
win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
#  裁剪得到全图
game_rect = win32gui.GetWindowRect(hwnd)
src_image = ImageGrab.grab(game_rect)
# src_image = ImageGrab.grab((game_rect[0] + 9, game_rect[1] + 190, game_rect[2] - 9, game_rect[1] + 190 + 450))
src_image.show()
if False:
    img_ready = ImageGrab.grab((0,0,300,300))
    # 截图
    img_ready.show()
    # 展示 


'''
def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回坐标值和handle
        return win32gui.GetWindowRect(handle), handle
'''