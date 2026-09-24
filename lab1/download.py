import kagglehub

# Download latest version
path = kagglehub.dataset_download("maximsuvorov/rutweetcorp")

print("Path to dataset files:", path)