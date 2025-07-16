import os
import shutil

folders = [folder for folder in os.listdir("latent_diffusion_trainingset/train") if os.path.isdir(os.path.join("latent_diffusion_trainingset/train", folder))]

folders = [os.path.join("latent_diffusion_trainingset/train", folder) for folder in folders]

num_folders = len(folders)

image_paths = os.listdir("coco2017")

num_real_images_per_folder = int(118288 / num_folders)

for folder in os.listdir("latent_diffusion_trainingset/train"):

    folder_path = os.path.join("latent_diffusion_trainingset/train", folder, "0_real")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print(folder_path)
    if not os.path.isdir(folder_path):
        continue

    for _ in range(num_real_images_per_folder):
        if image_paths:
            image = image_paths.pop()
        else:
            break

        shutil.copyfile(os.path.join("coco2017", image), os.path.join(folder_path, image))
            