from requests import get
from os import makedirs, remove
from re import sub
from time import time

name = input('Name: ')
path = f"{input('path: ')}/{name}/"
tmp = input('URL: ')
pattern = r'/\d+\.ts.*'
url = sub(pattern, '/{}.ts', tmp)
head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
n = 1
try: makedirs(path)
except: pass
end = b'<Code>NoSuchKey</Code>'

# 下载
while True:
    try:
        print(f'Downloading {n}.ts...')
        re = get(url.format(n), headers=head)
    except Exception as e:
        print(f'Fail to download {n}.ts on "{url.format(n)}" due to {e}')
        break
    if end in re.content:
        print('Finished.')
        break
    print(f'Writing {n}.ts...')
    with open(f'{path}{n}.ts','wb') as f:
        f.write(re.content)
    n += 1
print('Combining...')
n -= 1
count = n // 20 + 1

# 整合为多个文件
for t in range(count):
    p = f'{path}{name}_{int(time())}_{t+1}.ts'
    print('Combining to', p)
    with open(p, 'wb') as f:
        for i in range(min(20, n - t * 20)):
            with open(f'{path}{i+1+t*20}.ts', 'rb') as tmp:
                f.write(tmp.read())
            remove(f'{path}{i+1+t*20}.ts')

a = input('Program finished. Press enter to exit.')
