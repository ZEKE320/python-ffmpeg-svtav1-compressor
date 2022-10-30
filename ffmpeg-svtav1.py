import argparse
from logging import getLogger
import os
import re
import subprocess

video_ext = [".mp4", ".mkv"]
output_dir_basename = "svtav1"
logger = getLogger("logger")


def search_and_compress(root_path, modified_files):

    for fdpath, sub_folders, files in os.walk(root_path):
        for sub_folder in sub_folders:
            search_and_compress(sub_folder, modified_files)
        for file in files:
            compress(fdpath, file, modified_files)


def compress(fdpath, file, modified_files):
    file_name = os.path.basename(file)
    splitted_file_name = os.path.splitext(file_name)

    if splitted_file_name[1] not in video_ext:
        return

    if re.search(output_dir_basename, fdpath):
        return

    output_dir = f"{fdpath}{os.sep}{output_dir_basename}"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    input_path = f"{fdpath}{os.sep}{file_name}"
    output_path = f"{output_dir}{os.sep}{splitted_file_name[0]}_svtav1.mkv"

    ffmpeg_svtav1_command = [
        "ffmpeg",
        "-n",
        "-i",
        input_path,
        "-c:v",
        "libsvtav1",
        "-preset",
        "5",
        "-crf",
        "32",
        "-g",
        "240",
        "-pix_fmt",
        "yuv420p10le",
        "-svtav1-params",
        "tune=0:film-grain=8",
        "-c:a",
        "copy",
        output_path,
    ]

    logger.info(f"{ffmpeg_svtav1_command}")
    subprocess.call(ffmpeg_svtav1_command, shell=True)
    modified_files.append(
        f"{fdpath}{os.sep}\n"
        f"\t{file_name}\n"
        f"\t-> {output_dir_basename}{os.sep}{splitted_file_name[0]}_svtav1.mkv\n"
    )


parser = argparse.ArgumentParser()
parser.add_argument("target_path")
target_path = parser.parse_args().target_path

if os.path.exists(target_path) == False:
    logger.error("Invalid path.")
    exit()

modified_files = []
search_and_compress(target_path, modified_files)

print("\n--- Files listed below was modified ---\n")
for modified_file in modified_files:
    print(modified_file)
