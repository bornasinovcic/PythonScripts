import os
import operator



def main():
    j = 1
    rijecnik = {}
    extension = ".jpg"
    os.chdir("../wallpapers")
    for i in os.listdir():
        rijecnik.update({i:os.path.getsize(i)})
    sorted_d = dict(sorted(rijecnik.items(), key = operator.itemgetter(1), reverse = True))
    my_list = []
    for x, y in sorted_d.items():
        my_list.append(x)
    for i in my_list:
        if j <= 9:
            if os.path.isfile("0000" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "0000" + str(j) + extension)
                j += 1
        elif 10 <= j <= 99:
            if os.path.isfile("000" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "000" + str(j) + extension)
                j += 1
        elif 100 <= j <= 999:
            if os.path.isfile("00" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "00" + str(j) + extension)
                j += 1
        elif 1000 <= j <= 9999:
            if os.path.isfile("0" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "0" + str(j) + extension)
                j += 1
        else:
            if os.path.isfile(str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, str(j) + extension)
                j += 1



if __name__ == "__main__":
    main()
    print("Code finished")
