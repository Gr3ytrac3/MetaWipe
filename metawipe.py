#!/usr/bin/env python3

import os
import subprocess
import sys
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif', '.webp')
console = Console()

def banner():
    fig = Figlet(font="ansi_shadow")
    banner_text = fig.renderText("META WIPE")
    console.print(f"[bold green]{banner_text}[/bold green]")

    quote = Text('"Clean images. Clean conscience."', style="italic yellow")
    console.print(quote, justify="center")

    console.print("\n[bold cyan] • Wipe metadata from a single image")
    console.print("[bold cyan] • Wipe metadata from all images in a folder")
    console.print("[bold cyan] • Uses exiftool\n")


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
        console.print(f"[green][✓][/green] Cleaned: {image_path}")
    except Exception as e:
        console.print(f"[red][!][/red] Failed to clean {image_path}: {e}")


def verify_metadata_cleared(images):
    console.print("\n[bold yellow]🔍 Verifying metadata removal...[/bold yellow]")
    for image in images:
        result = subprocess.run(['exiftool', image], stdout=subprocess.PIPE, text=True)
        metadata_lines = result.stdout.strip().split('\n')

        if len(metadata_lines) <= 3:
            console.print(f"[green][✓] CLEAN[/green]  {image}")
        else:
            console.print(f"[red][!] NOT CLEAN[/red]  {image} — {len(metadata_lines)} metadata fields")


def main():
    banner()
    path = input("\n📂 Enter the path to the image or folder: ").strip()

    if not os.path.exists(path):
        console.print("[red][!] Path does not exist.[/red]")
        sys.exit(1)

    if os.path.isfile(path) and path.lower().endswith(SUPPORTED_EXTENSIONS):
        images = [path]
    elif os.path.isdir(path):
        images = get_images_from_folder(path)
    else:
        console.print("[red][!] Not a valid image file or directory.[/red]")
        sys.exit(1)

    if not images:
        console.print("[yellow][!] No supported images found in the path.[/yellow]")
        sys.exit(0)

    console.print(f"\n[bold cyan][+] Found {len(images)} image(s). Cleaning metadata...[/bold cyan]\n")
    for image in images:
        wipe_metadata(image)

    verify_metadata_cleared(images)
    console.print("\n[bold green]✅ Done. Metadata wipe and verification complete.[/bold green]")


if __name__ == "__main__":
    main()