import pathlib
import os
import shutil
import tarfile
import datetime
import threading
import random
import string


# This is the main task script.
# In the scope of this script, we create a tmp folder if one doesn't exist. Then we start running a thread
# each 0.5 seconds checking if the folder has at least 10 files.
# Once there are at least 10 files, then the files are archived and the folder is cleaned up.

# Create a lock to prevent race conditions
archive_lock = threading.Lock()
# This will signal the background process to stop
stop_event = threading.Event()


# Returns a path to tmp folder in the current working directory.
# If the folder doesn't exist, a new tmp folder is created.
def _get_path_to_tmp_folder_in_working_directory() -> pathlib.Path:
    tmp_folder_name = "tmp"
    # path_to_script = current_file_path = pathlib.Path(__file__).resolve()
    path_to_tmp_folder = pathlib.Path(tmp_folder_name).absolute()
    path_to_tmp_folder.mkdir(exist_ok=True)
    return path_to_tmp_folder


# Checks to see if tmp folder contains 10 or more files. If so, it calls the archive method to clean up the folder
def _check_if_tmp_has_10_files(path_to_tmp_folder: pathlib.Path):
    file_count_in_tmp_folder = len([f for f in os.listdir(path_to_tmp_folder) if
                                    os.path.isfile(os.path.join(path_to_tmp_folder, f))])
    if file_count_in_tmp_folder >= 10:
        _archive_files_in_tmp_folder(path_to_tmp_folder)


# Archives the content of the tmp folder, then it deletes it and all its content. Afterward a new tmp folder is created.
def _archive_files_in_tmp_folder(path_to_tmp: pathlib.Path):
    # The lock prevents an issue to occur that a thread is created while a previous one is running, causing
    # the task requirement to print 'files collected' to sometimes be missed.
    with archive_lock:
        timestamp = datetime.datetime.now().strftime('%y-%m-%dT%H-%M-%S_')
        output_tar = timestamp + 'files.tar.gz'
        # We resolve the absolute path in order for this script to run on multiple environments (Windows, Mac)
        output_file_path = pathlib.Path(output_tar).resolve()

        with tarfile.open(output_file_path, "w:gz") as archive:
            archive.add(path_to_tmp, arcname=".")

        print('files collected')
        shutil.rmtree(path_to_tmp)
        _get_path_to_tmp_folder_in_working_directory()


# This is more of a helper method. It makes our life easier, and it instantly creates 10 randomly named txt files
# inside the 'tmp' folder
def create_10_empty_txt_files_in_tmp_folder():
    _get_path_to_tmp_folder_in_working_directory()
    for x in range(10):
        random_filename_length = 15
        random_file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random_filename_length))
        path_to_random_file = os.path.join('tmp', random_file_name)
        with open('{}.txt'.format(pathlib.Path(path_to_random_file).resolve()), "w"):
            pass  # 'pass' ensures the file remains empty


# A new thread is created every 0.5 seconds which checks if the tmp folder contains at least 10 files.
def run_file_collection_in_background():
    if stop_event.is_set():
        return  # Stop running if the stop flag is set
    threading.Timer(0.5, run_file_collection_in_background).start()
    path_to_temp = _get_path_to_tmp_folder_in_working_directory()
    _check_if_tmp_has_10_files(path_to_temp)
