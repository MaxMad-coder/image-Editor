from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog,QPushButton,QHBoxLayout,QVBoxLayout,QComboBox,QLabel,QListWidget
from PyQt5.QtCore import Qt
import os
from PyQt5.QtGui import QPixmap
from PIL import Image,ImageEnhance,ImageFilter

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoShop")
main_window.resize(900,700)

folderbtn = QPushButton("Folder")
listbtn = QListWidget()

btnleft = QPushButton("Left")
btnright= QPushButton("Right")
mirror =  QPushButton("Mirror")
sharpness =  QPushButton("Sharpness")
gray =  QPushButton("Gray")
saturation =  QPushButton("Saturation")
contrast =  QPushButton("Contrast")
blur =  QPushButton("Blur")
imagelbl = QLabel("Any photo",alignment = Qt.AlignCenter)

filterbox = QComboBox()
filterbox.addItem("Original")
filterbox.addItem("Left")
filterbox.addItem("Right")
filterbox.addItem("Mirror")
filterbox.addItem("Sharpness")
filterbox.addItem("B/W")
filterbox.addItem("Color")
filterbox.addItem("Contrast")
filterbox.addItem("Blur")

master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(folderbtn)
col1.addWidget(listbtn)
col1.addWidget(btnleft)
col1.addWidget(btnright)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)
col2.addWidget(imagelbl)

master_layout.addLayout(col1,20)
master_layout.addLayout(col2,80)

working_directory = ""

#Filter
def filter(files,extensions):
    result=[]
    for file in files:
        for ext in extensions:
            if file.endswith()==ext:
                result.append(file)
    return result

def getWorkingDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = [".jpg","jpeg",".png",".svg"]
    filenames = filter(os.listdir(working_directory),extensions)
    listbtn.clear()
    for filename in filenames:
        listbtn.addItem(filename)

class Editor():
    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.savefolder = "edits/"

    def load_image(self,filename):
        self.filename = filename
        fullname = os.path.join(working_directory,self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(working_directory,self.savefolder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        fullname = os.path.join(path,self.filename)
        self.image.save(fullname)

    def show_image(self,path):
        imagelbl.hide()
        image =QPixmap(path)
        w,h = imagelbl.width(),imagelbl.height()
        image = image.scaled(w,h,Qt.KeepAspectRatio)
        imagelbl.setPixmap(image)
        imagelbl.show()
    def gray(self):
        self.image  = self.image.convert("L")
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)

    def left(self):
        self.image  = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)
    def right(self):
        self.image  = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)

    def mirror(self):
        self.image  = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)

    def sharpen(self):
        self.image  = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)

    def blur(self):
        self.image  = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)

    def contrast(self):
        self.image  = ImageEnhance.Contrast(self.image).enhance(1.2)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)
    def color(self):
        self.image  = ImageEnhance.Color(self.image).enhance(1.2)
        self.save_image()
        image_path = os.path.join(working_directory,self.savefolder,self.filename)
        self.show_image(image_path)
    def apply_filter(self,filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            mapping = {
                "B/W" : lambda image : image.convert("L"),
                "Color" : lambda image : ImageEnhance.Color(image).enhance(1.2),
                "Contrast" : lambda image : ImageEnhance.Contrast(image).enhance(1.2),
                "Blur" : lambda image : image.filter(ImageFilter.BLUR),
                "Left" : lambda image : image.transpose(Image.ROTATE_90),
                "Right" : lambda image : image.transpose(Image.ROTATE_270),
                "Mirror" : lambda image : image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness" : lambda image : image.filter(ImageFilter.SHARPEN)
            }
            filter_function = mapping.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                image_path = os.path.join(working_directory,self.savefolder,self.filename)
                self.show_image(image_path)
            pass
        self.save_image()
        image_path = os.path.join(working_directory, self.savefolder, self.filename)
        self.show_image(image_path)

def handle_filter():
    if listbtn.currentRow()>=0:
        select_filter = filterbox.currentText()
        main.apply_filter(select_filter)


def display_image():
    if listbtn.currentRow()>=0:
        filename = listbtn.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory,main.filename))

main = Editor()

folderbtn.clicked.connect(getWorkingDirectory)
listbtn.clicked.connect(display_image)
filterbox.currentTextChanged.connect(handle_filter)

btnleft.clicked.connect(main.left)
btnright.clicked.connect(main.right)
mirror.clicked.connect(main.mirror)
sharpness.clicked.connect(main.sharpen)
gray.clicked.connect(main.gray)
contrast.clicked.connect(main.contrast)
saturation.clicked.connect(main.color)
blur.clicked.connect(main.blur)
main_window.setLayout(master_layout)

main_window.show()
app.exec_()
