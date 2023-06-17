import zipfile as zf
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zf.ZipFile(dest_dir + '.zip', 'w') as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=['bonus_16.py'], dest_dir='files')


