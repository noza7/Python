import pyautogui as pag
import time
import pyperclip

# todo 截取图像,用于判断密码是否输入成功
# 图片生成路径
path = 'pics/password_input.png'
judge_path = 'pics/judge_pic.png'
# 1.获取鼠标位置
# mouse_position = pag.position()

# 2.打印图片坐标
# print(mouse_position)
# mouse_position_l = (629, 355)
# mouse_position_r = (703, 391)
# 判断运行环境截图坐标
# mouse_position_l = (694, 551)
# mouse_position_r = (748, 589)

# 密码输入框坐标
pswd_x = 676
pswd_y = 384
# 确定按钮坐标
confirm_x = 739
confirm_y = 440


# 576 367 788 402


def cut_pic(path, mouse_position_l, mouse_position_r):
    '''
    截取图片到指定位置
    :param path: 图片保存路径
    :param mouse_position_l: 左上角坐标
    :param mouse_position_r: 右下角坐标
    :return:返回截取的图像
    '''
    x_l, y_l = mouse_position_l
    x_r, y_r = mouse_position_r
    left = x_l
    top = y_l
    width = x_r - x_l
    height = y_r - y_l
    pic = pag.screenshot(path, region=(left, top, width, height))
    return pic


# 3.截图并保存
# cut_pic(path, mouse_position_l, mouse_position_r)


def get_pic_locate(path):
    '''
    查找图像，并获得图片坐标
    :param path:待比对的图像路径
    :return:返回找到图片的中心点坐标
    '''
    # 在屏幕查找图片
    pic = pag.locateOnScreen(path)
    # 获取图片中心点坐标
    pic_center = pag.center(pic)
    return pic_center


# x = get_pic_locate(path=path)
# 4.获得密码框图片中心点坐标,用于点击
pic_center_x_y = pag.locateCenterOnScreen(path)
# 用于判断程序是否在运行环境中
judge_pic = pag.locateCenterOnScreen(judge_path)

# 密码字典
# password_book = ['1234', '12345', '456', '123']
# password_book = password_book


def get_password(pic_center_x_y, judge_pic):
    '''
    密码破解
    :param pic_center_x_y: 密码框中心点坐标
    :return:
    '''
    for i in range(100, 100000):
        # 点击密码框
        # pag.doubleClick(pswd_x, pswd_y)
        # 如果找到密码框图片
        if pic_center_x_y:
            # 点击密码框
            pag.doubleClick(pic_center_x_y[0], pic_center_x_y[1])
            # 复制密码
            pyperclip.copy(str(i))
            # 打印密码
            print(i)
            # 粘贴密码到密码框
            # 不知道什么原因，pyperclip的粘贴不起作用，所以用pyautogui自带的功能来解决粘贴问题
            pag.hotkey('ctrl', 'v')
            # 点击确定
            pag.click(confirm_x, confirm_y)
            time.sleep(3)
        else:
            # 如果找不到密码框，但必须在运行环境中
            # 这样,还是通过截图判断是否存在于运行环境中
            # 如果图片被识别,说明程序在运行
            if judge_pic:
                print('密码为：{}'.format(i))
                break
            # 程序不在运行环境中
            print('检查程序是否启动!!!')
            break


# get_password(pic_center_x_y, judge_pic)
