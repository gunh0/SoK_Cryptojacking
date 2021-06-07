import os
from bs4 import BeautifulSoup

path = os.path.dirname(os.path.abspath(__file__))
# print(path)
path += '/test.html'
# print(path)

dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

with open(path, encoding='UTF8') as fp:
    soup = BeautifulSoup(fp)

scripts = soup.find_all('script')
for i in range(0, len(scripts)):
    print("URL", scripts[i])
