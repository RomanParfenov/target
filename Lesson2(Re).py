
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

def main():
    with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Выдача отредактированных данных
        datawriter.writerows(reader_data_start(contacts_list))


def reader_data_start(contact):
    resout = []
    for infor in contact:
        part = []
        output = []
        j = 0
        for i in infor:
            j += 1
            if j <= 3:
                if i != '':
                    tec = re.findall(r'\w+', i)
                    part.append(tec)
            elif j == 6:
                patt_zero = re.compile(r"(\+7|8)\s*\(*(\d{3})\)*[\s-]*(\d{3})\-*(\d{2})\-*(\d+)"
                                       r"(\s?)\(*(\w+)*(\.)*\s*(\d*)\)*")
                res = patt_zero.sub(r"+7(\2)\3-\4-\5\6\7\8\9", i)
                part.append(res)
            else:
                part.append(i)


        for item in part:
            if isinstance(item, (str, int, bool)):
                output.append(item)
            elif isinstance(item, dict):
                for i in item.items():
                    output.extend(i)
            else:
                output.extend(list(item))
        resout.append(list(output))


    rr = (resout[2] + list(set(resout[4]) - set(resout[2])))
    rr[4], rr[7] = rr[7], rr[4]
    del(rr[7])
    rl = resout[7] + list(set(resout[8]) - set(resout[7]))
    del(rl[6])


    rezerval = []
    inm = 0
    for t in resout:
        if inm <= len(resout):
            if t[0] == resout[4][0]:
                rezerval.append(rr)
            elif t[0] == resout[8][0]:
                rezerval.append(rl)
            else:
                rezerval.append(t)
        inm += 1

    index = 1
    while index < len(rezerval):
        if rezerval[index] in rezerval[: index]:
            rezerval.pop(index)
        else: index += 1
    print(rezerval)
    return rezerval





if __name__ == '__main__':
    main()








