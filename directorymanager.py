import os

images_list_file = open("latent_diffusion_trainingset/train/real_coco.txt")


images_list = images_list_file.readlines()

print(len(images_list))
images_list_file.close()

for image in os.listdir("unlabeled2017"):

    if image in images_list:
        os.replace(os.path.join("unlabeled2017", image), os.path.join("used_coco", image))


