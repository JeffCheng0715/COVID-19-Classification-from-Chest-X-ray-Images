import kagglehub

# Download latest version
path = kagglehub.dataset_download("alsaniipe/chest-x-ray-image")

print("Path to dataset files:", path)