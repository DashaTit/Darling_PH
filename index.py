import sys

import sqlite3
from PyQt5 import uic
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi('photo_editor_disign.ui', self)

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

  def save_image(self):  # функция сохранения изображения
        new_img = Image.open(self.new_img)
        new_img.save('new.jpg')  # сохранение изображения (под именем "new.jpg" по умолчанию)
        self.save.setText('Сохраненно')

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())