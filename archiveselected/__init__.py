from datetime import datetime
from shutil import rmtree
import os
import zipfile

from fman import DirectoryPaneCommand, show_alert


def zip_dir(root_zip, path, ziph):
    file_count = 0
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for fileh in files:
            ziph.write(
                os.path.join(root, fileh),
                os.path.join(root_zip, os.path.basename(fileh)),
            )
            file_count += 1
        for dirh in dirs:
            file_count += zip_dir(
                os.path.join(
                    root_zip,
                    os.path.basename(dirh),
                ),
                os.path.join(root, dirh),
                ziph,
            )
    return file_count


class ArchiveSelected(DirectoryPaneCommand):
    archive_dir = '.old'
    archive_file_fmt = '%Y-%m-%dT%H:%M:%S'

    def __call__(self):
        file_list = self.get_chosen_files()
        output = ''

        selected_files = self.pane.get_selected_files()
        if selected_files:
            file_list = selected_files

        dir_path = os.path.dirname(file_list[0])
        zip_path = os.path.join(dir_path, self.archive_dir)
        if not os.path.exists(zip_path):
            os.makedirs(zip_path)

        archive_name = datetime.now().strftime(self.archive_file_fmt)
        zip_name = os.path.join(zip_path, archive_name + '.zip')
        ziph = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        file_count = 0

        for fileh in file_list:
            if os.path.isdir(fileh):
                file_count += zip_dir(
                    os.path.join(os.path.basename(fileh)),
                    fileh,
                    ziph,
                )
            elif os.path.isfile(fileh):
                ziph.write(
                    fileh,
                    os.path.join(os.path.basename(fileh)),
                )
                file_count += 1
        ziph.close()

        for fileh in file_list:
            if os.path.isdir(fileh):
                rmtree(fileh)
            elif os.path.isfile(fileh):
                os.remove(fileh)

        output += str(file_count) + ' files were archived to ' + zip_name
        show_alert(output)
