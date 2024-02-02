import os
import shutil

from tqdm import tqdm

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

        if not os.path.exists(os.path.join(current_dir, directory)):

            print(f"Creating folder '{directory}'... ", end=" ")
            os.mkdir(os.path.join(current_dir, directory))
            print("Done")


def main() -> None:
    """start the damn thing"""

    # current_dir = "C:\\Users\\ozone\\Downloads\\Documents\\Workuments\\playground\\bring me joy"
    current_dir = os.getcwd()

    # fancy console printing
    console_label = " START "
    print(f"{console_label:-^100}")
    print(f"Reading files from: {current_dir}")

    # create the folders
    create_dirs(current_dir)

    print("Processing")
    # go shooot!
    for file_name in tqdm(os.listdir(current_dir)):

        # make sure the exe don't kondo itself, lol
        if file_name != 'kondo.exe':
            file_to_move = os.path.join(current_dir, file_name)

            # documents items
            if file_name.endswith(document_extentions):
                destination_directory = os.path.join(current_dir, "Documents")

                # do not move if the file already exists in the destination
                if not os.path.isfile(os.path.join(destination_directory, file_name)):
                    shutil.move(file_to_move, destination_directory)

            # image items
            elif file_name.endswith(image_extensions):
                destination_directory = os.path.join(current_dir, "Images")

                #
                if not os.path.isfile(os.path.join(destination_directory, file_name)):
                    shutil.move(file_to_move, destination_directory)

            # audio items
            elif file_name.endswith(audio_extensions):
                destination_directory = os.path.join(current_dir, "Audio")

                #
                if not os.path.isfile(os.path.join(destination_directory, file_name)):
                    shutil.move(file_to_move, destination_directory)

            # video items
            elif file_name.endswith(video_extensions):
                destination_directory = os.path.join(current_dir, "Video")

                #
                if not os.path.isfile(os.path.join(destination_directory, file_name)):
                    shutil.move(file_to_move, destination_directory)

            # compressed items
            elif file_name.endswith(compressed_extensions):
                destination_directory = os.path.join(current_dir, "Compressed")

                #
                if not os.path.isfile(os.path.join(destination_directory, file_name)):
                    shutil.move(file_to_move, destination_directory)

            # everything else
            else:
                if os.path.isfile(file_to_move):
                    destination_directory = os.path.join(current_dir, "Others")

                    #
                    if not os.path.isfile(os.path.join(destination_directory, file_name)):
                        shutil.move(file_to_move, destination_directory)

    # fancy console printing
    console_label = f" COMPLETE "
    print(f"{console_label:-^100}")


if __name__ == "__main__":
    main()
