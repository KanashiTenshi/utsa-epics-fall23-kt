import os

def rename_images(folder_path):
    image_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']  # Add more formats if needed
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in image_formats]
    image_files.sort()  # Sort files to ensure sequential renaming

    for index, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"Choken_rat{index:02d}{extension}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")
    
if __name__ == "__main__":
    folder_path = "C:\\Users\\trank\\Documents\\Python"
    rename_images(folder_path)