import requests


# with open('218.12_81.txt',"r") as f:
#     line = f.read()
#     print(line)

s = requests.session()
# url = 'http://58.60.4.90:81/'
url = 'http://218.12.10.26:81/'
res = s.get(url=url, stream=True)
response = res.status_code
print(response)


# print(s.cookies.get_dict())
# headers = {}
# {"method":"global.login","session":2013204291,"params":{"userName":"admin","password":"4WzwxXxM","clientType":"Dahua3.0-Web3.0-NOTIE", "authorityType":"OldDigest"},"id":10000}
# data = {"params": {"userName": "admin", "password": "4WzwxXxM", "clientType": "Dahua3.0-Web3.0-NOTIE"}}
# request = s.post(url=url, data=data)


