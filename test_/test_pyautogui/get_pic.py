import pyautogui

mouse_position = pyautogui.position()

print(mouse_position)

def get_pic(mouse_down,mouse_up):
    pass

while True:
    if pyautogui.mouseDown():
        mouse_down_position=pyautogui.position()
