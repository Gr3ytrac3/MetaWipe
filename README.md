````markdown
███████╗███████╗████████╗ █████╗     ██╗    ██╗██╗██████╗ ███████╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗    ██║    ██║██║██╔══██╗██╔════╝██╔════╝
███████╗█████╗     ██║   ███████║    ██║ █╗ ██║██║██║  ██║█████╗  █████╗  
╚════██║██╔══╝     ██║   ██╔══██║    ██║███╗██║██║██║  ██║██╔══╝  ██╔══╝  
███████║███████╗   ██║   ██║  ██║    ╚███╔███╔╝██║██████╔╝███████╗███████╗
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═════╝ ╚══════╝╚══════╝


# 🧼 META WIPE

> Clean images. Clean conscience.  
> Secure your privacy by erasing all embedded metadata from image files — effortlessly.


## 🚀 Overview

MetaWipe is a simple, fast, and powerful command-line tool that removes all metadata from individual images or entire folders of image files. Built with `Python`, `ExifTool`, and beautiful terminal visuals (`Rich`, `PyFiglet`), it ensures privacy hygiene with style.

---

## ✨ Features

- 🖼️ Wipe metadata from a single image
- 📁 Recursively clean all images in a folder
- ✅ Verifies whether metadata was fully removed
- 🖥️ Stylish terminal interface with banner and emojis
- 💡 Built using `exiftool` (must be installed)

---

## 📦 Installation

1. Clone the repo

```bash
git clone https://github.com/Gr3ytrac3/metawipe.git
cd metawipe
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Make sure `exiftool` is installed**

```bash
sudo apt install libimage-exiftool-perl   # Debian/Ubuntu
brew install exiftool                     # macOS
```

---

## 🧰 Usage

### 🔹 Run MetaWipe

```bash
python3 metawipe.py
```

Then, follow the prompts to provide the path to either:

* a **single image**, or
* a **folder** containing images

### 📷 Supported formats:

`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`, `.webp`

---




## 🤝 Contributions

Pull requests and forks are welcome. If you have ideas to expand MetaWipe (e.g. GUI, drag-and-drop, format converters), feel free to open an issue or PR!
> “Information is power — gather it wisely, and guard it fiercely.”

---


## 🙋‍♂️ Author

**CyberDevHQ**
 Offensive Security Artisan | Builder of Digital Fortresses

---
© 2025 RedKernel
