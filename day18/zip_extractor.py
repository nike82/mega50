import zipfile


def extract_archive(archive_path, destination_folder):
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(destination_folder)


if __name__ == "__main__":
    extract_archive("C:/WORK/PYTHON/mega_50/day18/files/compressed.zip",
                    "C:/WORK/PYTHON/mega_50/day18/files")
