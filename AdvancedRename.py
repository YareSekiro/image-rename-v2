import os
import colorama
from colorama import Fore, Style


class ImageManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.total_images = 0
        self.folder_counts = {}

    def list_images(self):
        # Afficher la liste des images présentes dans le dossier et ses sous-dossiers
        self.total_images = 0  # Réinitialiser le compteur total
        self.folder_counts = {}  # Réinitialiser les compteurs par dossier

        for root, dirs, files in os.walk(self.folder_path):
            folder_images = 0  # Compteur d'images par dossier
            for file in files:
                if self.is_image_file(file):
                    file_path = os.path.join(root, file)
                    folder_images += 1
                    self.total_images += 1
                    print(file_path)
            if folder_images > 0:
                folder_name = os.path.basename(root)
                self.folder_counts[folder_name] = folder_images

        self.print_summary()

    def rename_images(self):
        # Renommer les images en prenant en compte le nom du dossier parent
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if self.is_image_file(file):
                    folder_name = os.path.basename(root)
                    file_path = os.path.join(root, file)
                    new_name = f"{folder_name}_{file}"
                    new_path = os.path.join(root, new_name)

                    try:
                        os.rename(file_path, new_path)
                        print(f"Renamed: {file_path} -> {new_path}")
                    except OSError as e:
                        print(f"Error renaming {file_path}: {e}")

    def is_image_file(self, file):
        # Vérifier si le fichier a une extension d'image valide
        image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
        extension = os.path.splitext(file)[1].lower()
        return extension in image_extensions

    def truncate_name(self, name, max_length):
        if len(name) > max_length:
            return name[:max_length-3] + "..."
        return name

    def print_summary(self):
        colorama.init()
        print(f"Total number of images: {self.total_images}")

        if self.folder_counts:
            print("\nFolder-wise image counts:")
            print(f"{Fore.GREEN}+--------------+--------------+{Style.RESET_ALL}")
            print(f"{Fore.GREEN}| Folder Name  | Image Count  |{Style.RESET_ALL}")
            print(f"{Fore.GREEN}+--------------+--------------+{Style.RESET_ALL}")
            for folder_name, image_count in self.folder_counts.items():
                folder_name = self.truncate_name(folder_name, 12)  # Maximum 12 characters for folder name
                image_count = str(image_count).center(12)
                print(f"| {folder_name.ljust(12)} | {image_count} |")
            print(f"{Fore.GREEN}+--------------+--------------+{Style.RESET_ALL}")
        else:
            print("No images found in any folder.")



if __name__ == "__main__":
    folder_path = "C:/Users/Mus/Pictures/AllGif/" 
    manager = ImageManager(folder_path)

    command = input("Enter a command (list:all, rename:all): ")

    if command == "list:all":
        manager.list_images()
    elif command == "rename:all":
        manager.rename_images()
    else:
        print("Invalid command.")
