import os
import shutil

document_extentions = (
    ".txt",
    ".pdf",
    ".csv",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx"
)

image_extensions = (
    ".png",
    ".PNG",
    ".jpg",
    ".JPG",
    ".gif",
    ".GIF",
    ".WEBP",
    ".webp",
    ".svg"
)

audio_extensions = (
    ".mp3",
    ".flac",
    ".wav"
)

video_extensions = (
    ".mp4",
    ".m4v",
    ".mkv",
    ".avi",
    ".wmv",
    ".mov",
    ".webm"
)

compressed_extensions = (
    ".zip",
    ".rar",
    ".7z"
)


def create_dirs(current_dir: str) -> None:
    """ create the dirs if they don't exist yet"""

    required_directories = [
        "Documents",
        "Images",
        "Audio",
        "Video",
        "Compressed",
        "Others"
    ]

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
    for file_name in os.listdir(current_dir):
        file_to_move = os.path.join(current_dir, file_name)

        # documents items
        if file_name.endswith(document_extentions):
            destination_directory = os.path.join(current_dir, "Documents")
            shutil.move(file_to_move, destination_directory)

        # image items
        elif file_name.endswith(image_extensions):
            destination_directory = os.path.join(current_dir, "Images")
            shutil.move(file_to_move, destination_directory)

        # audio items
        elif file_name.endswith(audio_extensions):
            destination_directory = os.path.join(current_dir, "Audio")
            shutil.move(file_to_move, destination_directory)

        # video items
        elif file_name.endswith(video_extensions):
            destination_directory = os.path.join(current_dir, "Video")
            shutil.move(file_to_move, destination_directory)

        # compressed items
        elif file_name.endswith(compressed_extensions):
            destination_directory = os.path.join(current_dir, "Compressed")
            shutil.move(file_to_move, destination_directory)

        # everything else
        else:
            if os.path.isfile(file_to_move):
                destination_directory = os.path.join(current_dir, "Others")
                shutil.move(file_to_move, destination_directory)

    # fancy console printing
    console_label = f" COMPLETE "
    print(f"{console_label:-^100}")


if __name__ == "__main__":
    main()
