import socket
from ipaddress import ip_address
from concurrent.futures import ThreadPoolExecutor


# 判断IP所在端口是否可用
def is_port_used(ip, port=81):
    """
    check whether the port is used by other program
    检测端口是否被占用

    :param ip:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print('{}:{}端口开启！----------------------'.format(ip, port))
        with open('ip_81.txt', 'a+') as f:
            f.write('{}:{}端口开启！'.format(ip, port) + '\n')
    except OSError:
        # print('{}:{}端口未响应！'.format(ip, port))
        return False
    finally:
        s.close()


# 输入ip地址范围，获得ip地址列表
def get_ip_ls(start, end):
    start = ip_address(start)
    end = ip_address(end)
    result = []
    while start <= end:
        result.append(str(start))
        start += 1
    return result


ip_ls = get_ip_ls('58.86.0.0', '58.99.255.255')
thread_pool = ThreadPoolExecutor(100)
# 创建一个空列表
ret_ls = []
# 把每一个ip地址和函数送到线程池
for i in ip_ls:
    ret = thread_pool.submit(is_port_used, i)
    ret_ls.append(ret)
# 好像是关闭线程池
thread_pool.shutdown()
# 好像是显示运行结果
for ret in ret_ls:
    ret.result()
