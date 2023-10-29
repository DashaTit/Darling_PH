import sys

import sqlite3
from PyQt5 import uic
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from random import choice, randint

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