import os


def main():
    current_dir = os.getcwd()
    print(f"You are here: {current_dir}")

    for item in os.listdir():
        if os.path.isfile(item):
            print(f"{item} is a file")
        else:
            print(f"{item} is a directory")


if __name__ == "__main__":
    main()
