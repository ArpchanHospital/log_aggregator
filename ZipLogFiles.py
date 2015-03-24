import zipfile
import os.path

from Utils import get_current_timestamp


class ZipLogFiles:
    def __init__(self, log_files):
        self.archive_name = 'log_files_' + get_current_timestamp() + '.zip'
        self.log_file_archive = zipfile.ZipFile(self.archive_name, mode='w')
        map(self.add_to_zip, log_files)
        self.log_file_archive.close()

    def add_to_zip(self, log_file):
        if os.path.exists(log_file.file_path):
            self.log_file_archive.write(log_file.file_path)