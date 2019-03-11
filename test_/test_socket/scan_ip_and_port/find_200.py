import requests


# 提取ip地址列表
def get_ip_ls(txt):
    # 打开ip地址本，读取数据
    with open(txt, "r") as f:
        lines = f.readlines()
    ip_ls = []
    for line in lines:
        ip = 'http://{}'.format(line[:-6])
        ip_ls.append(ip)
    return ip_ls


# 查看状态码是否是200，判断是否能够获取响应
def find_ok(ip):
    # url = 'http://58.60.4.90:81/'
    url = ip
    try:
        # timeout判断请求是否超时
        res = requests.get(url=url, timeout=2)
        response = res.status_code
        return response
    except Exception as e:
        print(e)
        return False
    # return response


txt = 'ip_81-1.txt'
ip_ls = get_ip_ls(txt)

# 获取所有在线ip地址
for ip in ip_ls:
    res = find_ok(ip)
    if res == 200:
        print('{}状态码:{}'.format(ip, res))
