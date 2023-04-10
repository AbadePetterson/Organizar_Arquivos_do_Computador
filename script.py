import os
import shutil
from tqdm import tqdm


dowloads_folder = os.path.expanduser("E:\BACKUP\TUDO")
images_folder = os.path.expanduser("E:\BACKUP\TUDO\IMAGES")

os.makedirs(images_folder, exist_ok=True)

for file_name in tqdm(os.listdir(dowloads_folder)):
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        file_path = os.path.join(dowloads_folder, file_name)
        try:
            shutil.move(file_path, images_folder)
        except shutil.Error:
            print(f"{file_name} already exists in the destination folder")
