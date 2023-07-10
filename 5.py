import os
import re


def task1():
    # в папке test найти все файлы filenames вывести количество
    filenames = 'filenames'
    count = 0
    for root, dirs, files in os.walk("test"):
        for filename in files:
            if filenames in filename:
                count += 1
    print(count)



def task2():
    # в папке test найти все email адреса записанные в файлы
    directory = ''
    emails = []
    for root, dirs, files in os.walk("test"):
        if len(files) != 0:
            for i in range(len(files)):
                directory = root + '\\' + files[i]
                way = os.path.abspath(directory)
                weight = os.path.getsize(way)
                if weight > 0:
                    file = open(way, 'r')
                    for line in file:
                        line = line.strip()
                        email = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
                        for j in email:
                            emails.append(j)
    for i in emails:
        print(i)


def main():
    task1()
    task2()
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)


if __name__ == '__main__':
    main()
