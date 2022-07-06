import os


def main():
    j = 1
    dictionary = {}
    extension = ".jpg"
    os.chdir("../../Desktop/wallpapers-master")
    for i in os.listdir():
        if i.endswith(extension):
            dictionary.update({i: os.path.getsize(i)})
    sorted_d = sorted(dictionary, key=dictionary.get, reverse=True)
    for i in sorted_d:
        if j <= 9:
            if not os.path.isfile("00" + str(j) + extension):
                os.rename(i, "00" + str(j) + extension)
        elif 10 <= j <= 99:
            if not os.path.isfile("0" + str(j) + extension):
                os.rename(i, "0" + str(j) + extension)
        elif 100 <= j <= 999:
            if not os.path.isfile("" + str(j) + extension):
                os.rename(i, "" + str(j) + extension)
        elif 1000 <= j <= 9999:
            if not os.path.isfile("0" + str(j) + extension):
                os.rename(i, "0" + str(j) + extension)
        else:
            if not os.path.isfile(str(j) + extension):
                os.rename(i, str(j) + extension)
        j += 1


if __name__ == "__main__":
    main()
    print(f"Code finished")
