import requests
import re



sessopm1=requests.session()
url='http://www.toutiao.com/a6434708385005830402/'

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response=sessopm1.request(method='get',headers=headers,url=url)
print response.text

Re_find_qid=re.compile(r'qid: \'.*?\'')
result_re=Re_find_qid.findall(response.text)
print result_re[0].split("'")[1]