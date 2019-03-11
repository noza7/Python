import socket
from ipaddress import ip_address
# from concurrent.futures import ThreadPoolExecutor
import threadpool


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
        with open('log.txt', 'a+') as f:
            f.write('{}:{}端口开启！'.format(ip, port) + '\n')
    except OSError:
        print('{}:{}端口未响应！'.format(ip, port))
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


# thread_pool = ThreadPoolExecutor(20)
# for i in ip_ls:
#     thread_pool.submit(is_port_used, i)
#     print(is_port_used(i, 81))
ip_ls = get_ip_ls('58.60.0.0', '58.60.1.255')
pool = threadpool.ThreadPool(50)
requests = threadpool.makeRequests(is_port_used, ip_ls)
[pool.putRequest(req) for req in requests]
pool.wait()
