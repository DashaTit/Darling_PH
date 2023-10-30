import sys

import sqlite3
from PyQt5 import uic
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from random import choice, randint


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 630)
        MainWindow.setMinimumSize(QtCore.QSize(860, 630))
        MainWindow.setMaximumSize(QtCore.QSize(860, 630))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("background-color:#01315C")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.all = QtWidgets.QPushButton(self.centralwidget)
        self.all.setGeometry(QtCore.QRect(10, 10, 321, 21))
        self.all.setMouseTracking(False)
        self.all.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.all.setToolTip("")
        self.all.setAutoFillBackground(False)
        self.all.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.all.setCheckable(False)
        self.all.setAutoDefault(False)
        self.all.setDefault(False)
        self.all.setFlat(False)
        self.all.setObjectName("all")
        self.green = QtWidgets.QPushButton(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(20, 70, 21, 23))
        self.green.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius:10px;")
        self.green.setText("")
        self.green.setObjectName("green")
        self.rotate_r = QtWidgets.QPushButton(self.centralwidget)
        self.rotate_r.setGeometry(QtCore.QRect(240, 520, 91, 21))
        self.rotate_r.setStyleSheet("QPushButton {\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(140, 140, 140);\n"
"}")
        self.rotate_r.setObjectName("rotate_r")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rotate_r)
        self.red = QtWidgets.QPushButton(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(20, 40, 21, 23))
        self.red.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.red.setText("")
        self.red.setObjectName("red")
        self.blue = QtWidgets.QPushButton(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(20, 100, 21, 23))
        self.blue.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"border-radius:10px;")
        self.blue.setText("")
        self.blue.setObjectName("blue")
        self.rotate_l = QtWidgets.QPushButton(self.centralwidget)
        self.rotate_l.setGeometry(QtCore.QRect(10, 520, 91, 21))
        self.rotate_l.setStyleSheet("QPushButton {\n"
"background-color: rgb(120, 120, 120);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(140, 140, 140);\n"
"}")
        self.rotate_l.setObjectName("rotate_l")
        self.buttonGroup.addButton(self.rotate_l)
        self.rSlider = QtWidgets.QSlider(self.centralwidget)
        self.rSlider.setGeometry(QtCore.QRect(50, 40, 271, 21))
        self.rSlider.setMaximum(255)
        self.rSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rSlider.setObjectName("rSlider")
        self.gSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.gSlider_2.setGeometry(QtCore.QRect(50, 70, 271, 21))
        self.gSlider_2.setStyleSheet("")
        self.gSlider_2.setMaximum(255)
        self.gSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.gSlider_2.setObjectName("gSlider_2")
        self.bSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.bSlider_3.setGeometry(QtCore.QRect(50, 100, 271, 21))
        self.bSlider_3.setMaximum(255)
        self.bSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.bSlider_3.setObjectName("bSlider_3")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(350, 10, 500, 500))
        self.image.setMaximumSize(QtCore.QSize(500, 500))
        self.image.setStyleSheet("border-radius:10px;\n"
"background-color: #C0C0C0;")
        self.image.setObjectName("image")
        self.actions_line = QtWidgets.QLabel(self.centralwidget)
        self.actions_line.setGeometry(QtCore.QRect(350, 520, 501, 21))
        self.actions_line.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: #FFE4E1;\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.actions_line.setObjectName("actions_line")
        self.random_b = QtWidgets.QPushButton(self.centralwidget)
        self.random_b.setGeometry(QtCore.QRect(10, 450, 321, 31))
        self.random_b.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.random_b.setObjectName("random_b")
        self.filterSlider = QtWidgets.QSlider(self.centralwidget)
        self.filterSlider.setGeometry(QtCore.QRect(20, 160, 20, 161))
        self.filterSlider.setOrientation(QtCore.Qt.Vertical)
        self.filterSlider.setObjectName("filterSlider")
        self.filter = QtWidgets.QLabel(self.centralwidget)
        self.filter.setGeometry(QtCore.QRect(10, 330, 61, 16))
        self.filter.setStyleSheet("color: rgb(255, 255, 255);")
        self.filter.setObjectName("filter")
        self.bw = QtWidgets.QPushButton(self.centralwidget)
        self.bw.setGeometry(QtCore.QRect(60, 160, 41, 41))
        self.bw.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.bw.setObjectName("bw")
        self.ng = QtWidgets.QPushButton(self.centralwidget)
        self.ng.setGeometry(QtCore.QRect(120, 160, 41, 41))
        self.ng.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.ng.setObjectName("ng")
        self.src = QtWidgets.QPushButton(self.centralwidget)
        self.src.setGeometry(QtCore.QRect(180, 160, 41, 41))
        self.src.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.src.setObjectName("src")
        self.three_D_b = QtWidgets.QPushButton(self.centralwidget)
        self.three_D_b.setGeometry(QtCore.QRect(60, 210, 41, 41))
        self.three_D_b.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.three_D_b.setObjectName("three_D_b")
        self.Andy_Warhol_b = QtWidgets.QPushButton(self.centralwidget)
        self.Andy_Warhol_b.setGeometry(QtCore.QRect(120, 210, 41, 41))
        self.Andy_Warhol_b.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.Andy_Warhol_b.setObjectName("Andy_Warhol_b")
        self.saturation_b = QtWidgets.QPushButton(self.centralwidget)
        self.saturation_b.setGeometry(QtCore.QRect(180, 210, 41, 41))
        self.saturation_b.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.saturation_b.setObjectName("saturation_b")
        self.strange_b = QtWidgets.QPushButton(self.centralwidget)
        self.strange_b.setGeometry(QtCore.QRect(50, 270, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.strange_b.setFont(font)
        self.strange_b.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.strange_b.setObjectName("strange_b")
        self.acid_b = QtWidgets.QPushButton(self.centralwidget)
        self.acid_b.setGeometry(QtCore.QRect(90, 300, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.acid_b.setFont(font)
        self.acid_b.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.acid_b.setObjectName("acid_b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: 2F70AF;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.File_winbow = QtWidgets.QDockWidget(MainWindow)
        self.File_winbow.setMinimumSize(QtCore.QSize(860, 42))
        self.File_winbow.setMaximumSize(QtCore.QSize(860, 60))
        self.File_winbow.setStyleSheet("background-color: #00457D\n"
"")
        self.File_winbow.setObjectName("File_winbow")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.save = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.save.setGeometry(QtCore.QRect(10, 10, 301, 21))
        self.save.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.save.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.save.setObjectName("save")
        self.open = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.open.setGeometry(QtCore.QRect(330, 10, 311, 21))
        self.open.setStyleSheet("QPushButton {\n"
"background-color: #806592;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BA848D;\n"
"}")
        self.open.setObjectName("open")
        self.pushButton_4 = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 10, 201, 21))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.File_winbow.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.File_winbow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.all.setText(_translate("MainWindow", "ALL"))
        self.rotate_r.setText(_translate("MainWindow", ">"))
        self.rotate_l.setText(_translate("MainWindow", "<"))
        self.image.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.actions_line.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.actions_line.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.random_b.setText(_translate("MainWindow", "RANDOM"))
        self.filter.setText(_translate("MainWindow", "размытие"))
        self.bw.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bw.setText(_translate("MainWindow", "bw"))
        self.ng.setText(_translate("MainWindow", "ng"))
        self.src.setText(_translate("MainWindow", "src"))
        self.three_D_b.setText(_translate("MainWindow", "3D"))
        self.Andy_Warhol_b.setText(_translate("MainWindow", "CN"))
        self.saturation_b.setText(_translate("MainWindow", "b.s."))
        self.strange_b.setText(_translate("MainWindow", "strange"))
        self.acid_b.setText(_translate("MainWindow", "acid"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.pushButton_4.setText(_translate("MainWindow", "Exit"))


class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    #выбор изображения из текущей папки с расширением jpg
    fname = QFileDialog.getOpenFileName(
            self, 'Выберете изображение (рек. 500х500):', '',
            'Картинка (*.jpg);;Картинка (*.jpg);;Все файлы (*)')[0]
    '''self.fname.move(300, 300)'''  # открытие окна проводника для выбора изображения
    self.start_image = fname  # исходник
    self.intermediate_img = 'intermediate.jpg'  # промежуточное изображение
    self.new_img = 'new.jpg'  # конечный результат
    if fname: #открытие изображения 1
            img = Image.open(self.start_image)
            img.save(self.new_img) #сразу сохраняет
            img.save(self.intermediate_img) #промежуточный результат (будет исп-ся позже при применениии фильров)
            self.pixmap = QPixmap(self.new_img)
            self.image.setPixmap(self.pixmap)

    self.rotate_l.clicked.connect(self.l_turn)
    self.rotate_r.clicked.connect(self.r_turn)

    self.im_ugol = 0 

    self.initUi()
  

  #инит
  def initUi(self):
      self.setWindowTitle('Darling_PH') #название окна
      self.setWindowIcon(QIcon('icon.jpg')) #logo
      self.pixmap = QPixmap(self.start_image) 
      self.image.setPixmap(self.pixmap)
      self.open.clicked.connect(self.open_image) #открытие изображения в программе
      self.save.clicked.connect(self.save_image) #сохранение изобржения

      #слайдеры rgb, аналог первого задания из классной работы PIL 2.0
      self.red.clicked.connect(self.r_color) # красный слайдер
      self.rSlider.valueChanged.connect(self.change_r) #функция, которая его двигает
      self.green.clicked.connect(self.g_color)
      self.gSlider_2.valueChanged.connect(self.change_g)
      self.blue.clicked.connect(self.b_color)
      self.bSlider_3.valueChanged.connect(self.change_b)

      self.all.clicked.connect(self.full_color) #возвращение к исходному

      self.pushButton_4.clicked.connect(self.end_of_programm) #выход из программы

      self.filterSlider.valueChanged.connect(self.change_filter) #размытие по слайдеру

      self.bw.clicked.connect(self.black_and_white) #чб фильтр
      self.ng.clicked.connect(self.negativity) #негатив фильтр
      self.src.clicked.connect(self.average_color) # средний цвет

      self.three_D_b.clicked.connect(self.three_D) #3д стереопатра задача
      self.Andy_Warhol_b.clicked.connect(self.random_pix) #рандомные пиксели
      self.saturation_b.clicked.connect(self.saturation) #разбитый экран

      self.random_b.clicked.connect(self.random_filt) #рандомный фильр

      self.strange_b.clicked.connect(self.strange)
      self.acid_b.clicked.connect(self.acid)




  def open_image(self):  # открытие изображения нового
        fname = QFileDialog.getOpenFileName(
            self, 'Выберете изображение (рек. 500х500):', '',
            'Картинка (*.jpg);;Картинка (*.jpg);;Все файлы (*)')[0]
        '''self.fname.move(300, 300)'''
        if fname:
            self.start_image = fname
            img = Image.open(self.start_image)
            img.save(self.new_img)
            img.save(self.intermediate_img)
            self.pixmap = QPixmap(self.start_image)
            self.image.setPixmap(self.pixmap)
            self.save.setText('Сохранить')
        else:
            self.start_image = self.start_image

  def k(self):  # костыль для базы данных
        pass

  def save_image(self):  # функция сохранения изображения
        new_img = Image.open(self.new_img)
        new_img.save('new.jpg')  # сохранение изображения (под именем "new.jpg" по умолчанию)
        self.save.setText('Сохраненно')

  def random_filt(self):
      self.full_color()
      functions = (self.negativity, self.saturation, self.random_pix, self.three_D,
                  self.average_color, self.black_and_white)  # кортеж с функциями эффектов
      
      for i in range(randint(1, 3)):
        a = randint(1, len(functions) - 1)
        functions[a]()
      self.actions_line.setText('рандом')

  def r_color(self):  # красный профиль цветов, остальные по нулям
        img = Image.open(self.start_image)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        img = img.rotate(self.im_ugol)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('красный фильтр.')

  def b_color(self):  # синий профиль цветов, остальные в ноль
        img = Image.open(self.start_image)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        img = img.rotate(self.im_ugol)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('синий фильтр.')

  def g_color(self):  #  зеленый профиль цветов, остальные в ноль
        img = Image.open(self.start_image)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        img = img.rotate(self.im_ugol)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('зеленый фильтр.')


  def change_r(self):  # движок слайдера красный
        slider_value = int(self.rSlider.value())
        self.im_curr = Image.open(self.intermediate_img)
        pixels = self.im_curr.load()
        x, y = self.im_curr.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = slider_value, g, b
        self.im_curr.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Смена красного.')

  def change_g(self):  # движок слайдера зеленый
        slider_value = int(self.gSlider_2.value())
        self.im_curr = Image.open(self.intermediate_img)
        pixels = self.im_curr.load()
        x, y = self.im_curr.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, slider_value, b
        self.im_curr.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Смена зеленого.')

  def change_b(self):  # движок слайдера голубой
        slider_value = int(self.bSlider_3.value()) 
        self.im_curr = Image.open(self.intermediate_img)
        pixels = self.im_curr.load()
        x, y = self.im_curr.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, slider_value
        self.im_curr.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Смена синего.')

  def l_turn(self):  # поворот налево
        img = Image.open(self.new_img)
        img = img.rotate(90)
        self.im_ugol += 90
        self.im_ugol %= 360
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Поворот лево.')

  def r_turn(self):  # поворот направо
        img = Image.open(self.new_img)
        img = img.rotate(90)
        self.im_ugol -= 90
        self.im_ugol %= 360
        img = img.transpose(Image.ROTATE_180)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Поворот право.')

  def end_of_programm(self):  # выход, конец программы
        sys.exit(1)

  def full_color(self):  # восстановление изображения, возвращение к исходнику
        img = Image.open(self.start_image)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        self.im_ugol = 0
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setStyleSheet('QLabel {color: white;}')

  def change_filter(self):  # размытие по слайдеру
        slider_value = int(self.filterSlider.value())
        img = Image.open(self.intermediate_img)
        img = img.filter(ImageFilter.GaussianBlur(radius=slider_value))
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Размытие по слайдеру')

  def black_and_white(self):  # изобраение черно-белым
        img = Image.open(self.new_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r + g + b) // 3, (r + g + b) // 3, (r + g + b) // 3
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('чб фильтр')

  def negativity(self):  # негатив задача с того года на противоположный цвет
        img = Image.open(self.new_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 255 - r, 255 - g, 255 - b
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('негатив')
  
  def average_color(self):  # средний цвет изображения задача средний цвет фотографии с того года
        img = Image.open(self.new_img)
        pixels = img.load()
        x, y = img.size
        a, u, c = 0, 0, 0
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                a += r
                u += g
                c += b
        red = a // (x * y)
        green = u // (x * y)
        blue = c // (x * y)
        color = red, green, blue
        for i in range(x):
            for j in range(y):
                pixels[i, j] = red, green, blue
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText(
            f'Цвет изображения равен: {str(color)}')
  
  def three_D(self):  # стереопара по ял
        img = Image.open(self.new_img)
        pixels = img.load()
        x, y = img.size

        for i in range(x - 1, 20 - 1, -1):
            for j in range(y):
                r = pixels[i - 20, j][0]
                R, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        for i in range(20):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, b
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('стереопатра')

  def random_pix(self):  # окрашивем пиксели в рандомные цвета
        img = Image.open(self.new_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                values = [r, g, b, randint(0, 255)]
                pixels[i, j] = choice(values), choice(values), choice(values)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Информационный Шум')

  def saturation(self):  # возводит в абсолют цвета после определенного занчения их цветового профиля
        img = Image.open(self.new_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if r > g and r > b and r > 50:
                    r = 255
                elif g > r and g > b and g > 50:
                    g = 255
                elif b > r and b > g and b > 50:
                    b = 255
                elif g == b == r and (r + g + b) >= 300:
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = 0, 0, 0
                pixels[i, j] = r, g, b
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)
        self.actions_line.setText('Разбитый Экран')

  def strange(self):
        con = sqlite3.connect('preset.db')
        cur = con.cursor()
        result = cur.execute("""SELECT strange FROM my_sets""").fetchall()
        for a in result:
            for b in a:
                eval(b)()
        con.close()
        self.actions_line.setText('strange')

  def acid(self):
        con = sqlite3.connect('preset.db')
        cur = con.cursor()
        result = cur.execute("""SELECT acid FROM my_sets""").fetchall()
        for a in result:
            for b in a:
                eval(b)()
        con.close()
        self.actions_line.setText('acid')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())