import csv
import magic
import os

from bs4 import BeautifulSoup

f = open('result.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(["category", "target_name", "content"])


def check_category(full_path):
    print("[*] file path preprocessing 1 :",
          full_path.partition('/target/')[-1])
    category_str = full_path.partition('/target/')[-1]
    target_name = category_str.partition('/')[-1]
    category_str = category_str.partition('/')[0]
    print("[*] file path preprocessing 2 :", category_str)
    return (category_str, target_name)


def write_csv(full_path):
    # f = open('result.csv', 'w', encoding='utf-8', newline='')
    # wr = csv.writer(f)
    # wr.writerow(["category", "target_name", "content"])

    try:
        splited_path = check_category(full_path)
        open_file = open(full_path, 'rb').read()
        # m = magic.Magic(mime_encoding=True)
        # encoding = m.from_buffer(open_file)
        soup = BeautifulSoup(open_file)

        scripts = soup.find_all('script')
        for i in range(0, len(scripts)):
            # print('\n\n==========', i, ':', full_path,
            #       '==========\n\n', str(scripts[i]).rstrip('\n'))
            content = str(scripts[i]).rstrip('\n')
            content.replace("\n", "")
            wr.writerow([splited_path[0], splited_path[1], content])
    except:
        pass
    f.close


def search_files(dirname):
    serach_result = []
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                print("  [*] search directory", full_filename)
                search_files(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                print("    [*] search file", full_filename)
                write_csv(full_filename)

    except PermissionError:
        pass


path = os.path.dirname(os.path.abspath(__file__))
print("[*] pwd check,", path, os.path.isdir(path))

target_path = '/target'
path += target_path
search_files(path)


f.close
