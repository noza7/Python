import pyautogui as pag

# todo 截取图像
# 图片生成路径
path = 'pics/num_7.png'

# 获取鼠标位置
mouse_x, mouse_y = pag.position()
# print(mouse_x, mouse_y)
# 80 365 100 388


# 先用函数提取图片到指定位置
def cut_pic(path, left, top, left2, top2):
    width = left2 - left
    height = top2 - top
    pic = pag.screenshot(path, region=(left, top, width, height))
    return pic


# cut_pic(path, 80, 365, 20, 23)

# todo 定位函数
# 发现一个问题，自己截取的图片不能用，必须使用上面函数提取的图片


# 获得截取图片坐标
def get_pic_locate(path):
    # 获取定点坐标
    pic_4 = pag.locateOnScreen(path)
    pic_center = pag.center(pic_4)
    return pic_4, pic_center


# 直接获取图片中心点坐标
try:
    pic_x, pic_y = pag.locateCenterOnScreen(path)
    print(pic_x, pic_y)
    # 点击按钮
    pag.click(pic_x, pic_y)
except TypeError as e:
    print('没有找到图片！')
except FileNotFoundError as e:
    print('图片路径错误！')

# pic_x, pic_y = pag.locateCenterOnScreen(path)
# print(pic_x, pic_y)
# # 点击按钮
# pag.click(pic_x, pic_y)
