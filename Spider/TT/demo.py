from requests_html import HTMLSession
from selenium import webdriver

s = HTMLSession()
#
url = 'http://con.chinatowercom.cn:58080/SV/thresholdManage/page?cityid=&countyid=&provinceid=0001935&pageNum=1&pageSize=10'
headers_str = """Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Cookie: acctId=100906317; userOrgCode=80510300; pwdaToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSRVMiLCJpc3MiOiJXUzRBIiwiZXhwIjoxNjkzMzAwMTQyLCJOQU5PU0VDT05EIjoxMzk1Mzk5Mjc0NDc3MjM1OTV9.MOWO8zHHesWbWTNtZ5cVL7h3tpKtK36UkzAlmcMTx5w; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSRVMiLCJpc3MiOiJXUzRBIiwiZXhwIjoxNjkzMzAwMTQyLCJOQU5PU0VDT05EIjoxMzk1Mzk5Mjc0NDc3MjM1OTV9.MOWO8zHHesWbWTNtZ5cVL7h3tpKtK36UkzAlmcMTx5w
Host: con.chinatowercom.cn:58080
Referer: http://con.chinatowercom.cn:58080/monitor/threshold/index?pwdaToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSRVMiLCJpc3MiOiJXUzRBIiwiZXhwIjoxNjkzMzAwMTQyLCJOQU5PU0VDT05EIjoxMzk1Mzk5Mjc0NDc3MjM1OTV9.MOWO8zHHesWbWTNtZ5cVL7h3tpKtK36UkzAlmcMTx5w&acctId=100906317&flag=&loginKey46fa47d8-5d85-4452-9354-957904418001&menuCode=CHNTFSU-6&url=http%3A%2F%2Fcon.chinatowercom.cn%3A58080%2Fmonitor%2Fthreshold%2Findex
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"""
headers = {i.split(': ')[0]: i.split(': ')[1] for i in headers_str.split('\n')}

res = s.post(url, headers=headers).content.decode()
print(res)
