import os

document_extentions = (".pdf", ".csv", ".docx", ".xlxs")


def create_dirs(current_dir: str) -> None:
    """ create the dirs if they don't exist yet"""

    required_directories = ["Documents", "Images", "Audio", "Video", "Others"]

    for directory in required_directories:

        if os.path.exists(os.path.join(current_dir, directory)):
            print(f"'{directory}' folder already exists")

        else:
            print(f"'{directory}' folder does exist yet, creating one...", end=" ")
            os.mkdir(os.path.join(current_dir, directory))
            print("Done")


def main() -> None:
    """start the damn thing"""

    current_dir = "C:\\Users\\ozone\\Downloads\\Documents\\Workuments\\playground\\bring me joy"
    # current_dir = os.getcwd()

    # fancy console printing
    console_label = f" READING FROM {current_dir} "
    print(f"{console_label:-^100}")

    # create the folders
    create_dirs(current_dir)

    # go shooot!
    for item in os.listdir(current_dir):

        # documents
        if item.endswith(document_extentions):
            print(f"{item} is a supported document")


if __name__ == "__main__":
    main()
