import os


def main():
    j = 1
    dictionary = {}
    extension = ".jpg"
    os.chdir("../../Desktop/wallpapers-master")
    number_of_files = len(str(len(os.listdir())))
    for i in os.listdir():
        if i.endswith(extension):
            dictionary.update({i: os.path.getsize(i)})
    sorted_d = sorted(dictionary, key=dictionary.get, reverse=True)
    for i in sorted_d:
        if j <= 9:
            number_of_zeros = (number_of_files - 1) * '0'
            if not os.path.isfile(number_of_zeros + str(j) + extension):
                os.rename(i, number_of_zeros + str(j) + extension)
        elif 10 <= j <= 99:
            number_of_zeros = (number_of_files - 2) * '0'
            if not os.path.isfile(number_of_zeros + str(j) + extension):
                os.rename(i, number_of_zeros + str(j) + extension)
        elif 100 <= j <= 999:
            number_of_zeros = (number_of_files - 3) * '0'
            if not os.path.isfile(number_of_zeros + str(j) + extension):
                os.rename(i, number_of_zeros + str(j) + extension)
        elif 1000 <= j <= 9999:
            number_of_zeros = (number_of_files - 4) * '0'
            if not os.path.isfile(number_of_zeros + str(j) + extension):
                os.rename(i, number_of_zeros + str(j) + extension)
        elif 10000 <= j <= 99999:
            number_of_zeros = (number_of_files - 5) * '0'
            if not os.path.isfile(number_of_zeros + str(j) + extension):
                os.rename(i, number_of_zeros + str(j) + extension)
        else:
            number_of_zeros = (number_of_files - 6) * '0'
            if not os.path.isfile(number_of_zeros + str(j) + extension):
                os.rename(i, number_of_zeros + str(j) + extension)
        j += 1


if __name__ == "__main__":
    main()
    print(f"Code finished")
