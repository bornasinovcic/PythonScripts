import os


def main():
    j = 1
    dictionary = {}
    extension = ".jpg"
    os.chdir("../wallpapers-master")
    for i in os.listdir():
        dictionary.update({i: os.path.getsize(i)})
    sorted_d = sorted(dictionary, key=dictionary.get, reverse=True)
    my_list = []
    for x in sorted_d:
        my_list.append(x)
    for i in my_list:
        if j <= 9:
            if os.path.isfile("00" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "00" + str(j) + extension)
                j += 1
        elif 10 <= j <= 99:
            if os.path.isfile("0" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "0" + str(j) + extension)
                j += 1
        elif 100 <= j <= 999:
            if os.path.isfile("" + str(j) + extension):
                j += 1
                continue
            else:
                os.rename(i, "" + str(j) + extension)
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
    print(f"Code finished")
