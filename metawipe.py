#!/usr/bin/env python3
import os
import subprocess
import sys
from pyfiglet import Figlet

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif', '.webp')

def banner():
    fig = Figlet(font='slant')  # Other good options: 'big', 'ansi_shadow', 'banner3-D'
    print(fig.renderText("MetaWipe"))
    print("=== Metadata Wiper CLI Tool ===")
    print("  - Wipe metadata from a single image")
    print("  - Wipe metadata from all images in a folder")
    print("  - Uses exiftool\n")

def get_images_from_folder(folder_path):
    images = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                images.append(os.path.join(root, file))
    return images

def wipe_metadata(image_path):
    try:
        subprocess.run(['exiftool', '-overwrite_original', '-all=', image_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[✓] Cleaned: {image_path}")
    except Exception as e:
        print(f"[!] Failed to clean {image_path}: {e}")

def main():
    banner()
    path = input("Enter the path to the image or folder: ").strip()

    if not os.path.exists(path):
        print("[!] Path does not exist.")
        sys.exit(1)

    images = []
    if os.path.isfile(path) and path.lower().endswith(SUPPORTED_EXTENSIONS):
        images = [path]
    elif os.path.isdir(path):
        images = get_images_from_folder(path)
    else:
        print("[!] Not a valid image file or directory.")
        sys.exit(1)

    print(f"\n[+] Found {len(images)} image(s). Cleaning metadata...\n")
    for image in images:
        wipe_metadata(image)

    print("\n[✓] Done. All metadata wiped.")

if __name__ == "__main__":
    main()
