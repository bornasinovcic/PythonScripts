import os


def main():
    os.chdir("../test")
    extension = ".c"
    j = 1
    for i in os.listdir():
        if i.endswith(extension):
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
    print("Code successfully finished")
