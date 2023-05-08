import zipfile
import pathlib


def make_archive(file_paths, destination_dir):
    destination_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(destination_path, "w") as archive:
        for file_path in file_paths:
            file_path = pathlib.Path(file_path)
            archive.write(file_path, arcname=file_path.name)


if __name__ == "__name__":
    make_archive(file_paths=["files/todos.txt",
                             "files/todos2.txt"],
                 destination_dir="files")
