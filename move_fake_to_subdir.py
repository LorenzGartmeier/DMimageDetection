import os


for folder in os.listdir("latent_diffusion_trainingset/valid"):
    folder_path = os.path.join("latent_diffusion_trainingset/valid", folder)

    if not os.path.isdir(folder_path):
        continue

    fake_path = os.path.join(folder_path, "1_fake")

    os.mkdir(fake_path)

    for file in os.listdir(folder_path):

        if not os.path.isfile(os.path.join(folder_path, file)):
            continue
        
        os.replace(os.path.join(folder_path, file), os.path.join(fake_path, file))
