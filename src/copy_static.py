import os
import shutil

def copy_static(src_folder: str, dst_folder: str):
        if not os.path.exists(dst_folder) or not os.path.isdir(dst_folder):
            os.mkdir(dst_folder)
        if not os.path.exists(src_folder) or not os.path.isdir(src_folder):
            raise ValueError(f"Source folder {src_folder} does not exist")
        
        src_files = os.listdir(src_folder)
        print(src_files)
        
        for file in src_files:
            if os.path.isfile(os.path.join(src_folder, file)):
                print(f"Copying file {file} to {dst_folder}")
                shutil.copy(os.path.join(src_folder, file), os.path.join(dst_folder, file))
            else:
                print(f"Copying directory {file} to {dst_folder}")
                copy_static(os.path.join(src_folder, file), os.path.join(dst_folder, file))