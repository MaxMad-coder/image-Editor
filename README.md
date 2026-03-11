# 🖼️ PhotoShop - Image Editor

A simple desktop **Image Editor** application built with **Python**, **PyQt5**, and **Pillow (PIL)**. It allows users to browse images from a folder, apply filters, and save edited versions automatically.

---

## 🖥️ Features

- 📁 Browse and load images from any folder
- 🔄 Rotate images Left or Right
- 🪞 Mirror / Flip images horizontally
- ⬛ Convert to Black & White (Grayscale)
- 🎨 Boost Color saturation
- 🔲 Increase Contrast
- 🌀 Apply Blur effect
- ✨ Sharpen images
- 💾 Auto-saves edited images to an `edits/` subfolder
- 🖼️ Live preview of the edited image

---

## 📸 Screenshots

> Add a screenshot of your app here after running it.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| PyQt5 | GUI framework |
| Pillow (PIL) | Image processing and filters |
| OS Module | File and folder management |

---


## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/image-editor.git
cd image-editor
```

### 2. Install Dependencies
Make sure Python 3 is installed, then run:
```bash
pip install PyQt5 Pillow
```

### 3. Run the Application
```bash
python imageEdit.py
```

---

## 🚀 How to Use

1. Click **"Folder"** to open a folder containing images
2. Select an image from the **list on the left**
3. The image will appear in the **preview panel on the right**
4. Apply any of the following:

| Button / Filter | Effect |
|---|---|
| **Left** | Rotate image 90° counter-clockwise |
| **Right** | Rotate image 90° clockwise |
| **Mirror** | Flip image horizontally |
| **Gray** | Convert to black & white |
| **Saturation** | Boost color saturation |
| **Contrast** | Increase contrast |
| **Blur** | Apply blur effect |
| **Sharpness** | Sharpen the image |

5. Use the **dropdown (ComboBox)** to apply filters including **Original** to reset
6. Edited images are **automatically saved** in an `edits/` subfolder inside your selected folder

---

## 📂 Supported Image Formats

```
.jpg    .jpeg    .png    .svg
```

---

## 🐛 Known Issues / Bug Fixes

The following bugs exist in the current code:

| # | Bug | Location | Fix |
|---|---|---|---|
| 1 | `file.endswith()==ext` | `filter()` function | Change to `file.endswith(ext)` |
| 2 | Missing `.` before `jpeg` | extensions list | Change `"jpeg"` to `".jpeg"` |
| 3 | Double save and show after filter | `apply_filter()` | Remove duplicate `save_image()` and `show_image()` outside the if block |

---

## 📌 Requirements

```
Python >= 3.7
PyQt5 >= 5.15
Pillow >= 9.0
```

Install all at once:
```bash
pip install PyQt5 Pillow
```

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋 Author

**Your Name**
- GitHub: [@MaxMad-coder](https://github.com/your-username)
- Email: manash212005@gmail.com
