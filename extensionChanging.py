import os


def main():
    os.chdir("../test")
    old_extension = ".html"
    new_extension = ".php"
    for i in os.listdir():
        if i.endswith(old_extension):
            base = os.path.splitext(i)[0]
            os.rename(i, base + new_extension)


if __name__ == "__main__":
    main()
    print(f"Code successfully finished")
