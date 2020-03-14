from requests import session, packages
from os import makedirs, remove
from re import sub
from time import time
# https://dtliving.alicdn.com/live/f64e2624-f45a-42fa-b990-a31077f22f16/2.ts?auth_key=1585233365-0-0-83f853a2b07c3d139a680060c79a6c11
packages.urllib3.disable_warnings()
x = session()
name = input('Name: ')
path = 'E://Download/钉钉直播/' + name + '/'
tmp = input('URL: ')
pattern = r'/\d+\.ts.*'
url = sub(pattern, '/{}.ts', tmp)
head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
n = 0
try: makedirs(path)
except: pass
end = b'<Code>NoSuchKey</Code>'

# 下载
while True:
    try:
        print(f'Downloading {n+1}.ts...')
        re = x.get(url.format(n+1), headers=head, verify=False)
    except Exception as e:
        print(f'Fail to download {n+1}.ts on "{url.format(n)}" due to {e}')
        break
    if end in re.content:
        print('Finished.')
        break
    print(f'Writing {n+1}.ts...')
    with open(f'{path}{n+1}.ts','wb') as f:
        f.write(re.content)
    n += 1
print('Combining...')
# 整合
p = f'{path}{name}_{int(time())}.ts'
with open(p, 'wb') as f:
    for i in range(n):
        with open(f'{path}{i+1}.ts', 'rb') as tmp:
            f.write(tmp.read())
        remove(f'{path}{i+1}.ts')
a = input('Program finished. Press enter to exit.')