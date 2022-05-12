import os


def main():
    os.chdir("/home/borna/Desktop/zero")
    old_extension = ".borna"
    new_extension = ".sh"
    for i in os.listdir():
        if i.endswith(old_extension):
            base = os.path.splitext(i)[0]
            os.rename(i, base + new_extension)


if __name__ == "__main__":
    main()
