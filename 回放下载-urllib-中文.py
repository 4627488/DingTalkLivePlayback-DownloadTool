from urllib.request import urlopen, Request
from os import makedirs, remove
from re import sub
from time import time

tmp = input('网址：')
name = input('名称: ')
path = input('保存路径：') + name + '/'
pattern = r'/\d+\.ts.*'
url = sub(pattern, '/{}.ts', tmp)
print(url)
head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
n = 1
try: makedirs(path)
except: pass
end = b'<Code>NoSuchKey</Code>'

# 下载
while True:
    try:
        print('下载'+str(n)+'.ts...')
        req = Request(url.format(n), headers=head)
        response = urlopen(req)
    except Exception as e:
        print('在网址'+url.format(n)+'由于'+str(e)+'下载'+str(n)+'.ts失败!')
        break
    content = response.read()
    if end in content:
        print('下载完成！')
        break
    print('写入'+str(n)+'.ts...')
    with open(path+str(n)+'.ts','wb') as f:
        f.write(content)
    n += 1
print('整合...')
n -= 1
count = n // 20 + 1

# 整合
for t in range(count):
    p = path+name+'_'+str(int(time()))+'_'+str(t+1)+'.ts'
    print('整合', p)
    with open(p, 'wb') as f:
        for i in range(min(20, n - t * 20)):
            with open(path+str(i+1+t*20)+'.ts', 'rb') as tmp:
                f.write(tmp.read())
            remove(path+str(i+1+t*20)+'.ts')

a = input('程序结束。按回车退出。')
