#!/usr/bin/env python3
import os
import subprocess
import sys
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet

# Supported image formats
SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif', '.webp')


def banner():
    console = Console()
    fig = Figlet(font="big")  # Try 'block', 'big', or 'ansi_shadow'

    banner_text = fig.renderText("META WIPE")
    console.print(f"[bold green]{banner_text}[/bold green]")

    quote = Text('"Clean images. Clean conscience."', style="italic yellow")
    console.print(quote, justify="center")

    console.print("\n[bold cyan] - Wipe metadata from a single image")
    console.print("[bold cyan] - Wipe metadata from all images in a folder")
    console.print("[bold cyan] - Uses exiftool\n")

    console = Console()

    # Stylized green blocky banner
    console.print(justify="center")

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
    path = input("\n📂 Enter the path to the image or folder: ").strip()

    if not os.path.exists(path):
        print("[!] Path does not exist.")
        sys.exit(1)

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
