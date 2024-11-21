import os
from PIL import Image, ImageStat

def find_duplicate_images(folder_path):
    image_files = [_ for _ in os.listdir(folder_path) if _.endswith("jpg")]

    duplicate_files = []

    for i, file_org in enumerate(image_files):
        if file_org not in duplicate_files:
            image_org = Image.open(os.path.join(folder_path, file_org))
            pix_mean1 = ImageStat.Stat(image_org).mean

            for j, file_check in enumerate(image_files[i+1:], i+1):
                if file_check != file_org:
                    image_check = Image.open(os.path.join(folder_path, file_check))
                    pix_mean2 = ImageStat.Stat(image_check).mean

                    if pix_mean1 == pix_mean2:
                        duplicate_files.append(file_org)
                        duplicate_files.append(file_check)

    return duplicate_files

if __name__ == "__main__":
    folder_path = r'D:\Internprj\img1'
    duplicate_files = find_duplicate_images(folder_path)
    print(duplicate_files)