#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: Victor He
"""


import sys

# %% 1
# https://doc.qt.io/qt-5/qcolordialog.html
# https://doc.qt.io/qt-5/qcolordialog.html#signals
# https://doc.qt.io/qt-5/qcolordialog.html#colorSelected
# since QColorDialog inherits from QWidget, it has a show method

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.works = False
        self.l = 50
        self.x = randint(0, 600-self.l)
        self.y = randint(0, 400-self.l)
        self.color = QColor(255, 0, 0)
        self.Bcolor = self.color
        self.initUI()

    def initUI(self):
        self.initgeo()
        self.show()

    def initgeo(self):
        self.setGeometry(40, 40, 600, 400)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawbg(qp)
        self.drawthing(qp)
        qp.end()

    def drawbg(self, qp):
        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, 600, 400)

    def drawthing(self, qp):
        qp.setPen(self.color)
        qp.setBrush(self.color)
        qp.drawRect(self.x, self.y, self.l, self.l)

    def mousePressEvent(self, event):
        if event.x() in range(self.x, self.x+self.l) and event.y() in range(self.y, self.y+self.l):
            self.difx = event.x()-self.x
            self.dify = event.y()-self.y
            self.works = True

    def mouseMoveEvent(self, event):
        if self.works is True:
            self.x = event.x()-self.difx
            self.y = event.y()-self.dify
            self.update()

    def mouseReleaseEvent(self, event):
        self.works = False

    def mouseDoubleClickEvent(self, event):
        if event.x() in range(self.x, self.x+self.l) and event.y() in range(self.y, self.y+self.l):
            self.clk = QColorDialog()
            self.clk.setCurrentColor(self.Bcolor)
            self.clk.show()
            self.clk.currentColorChanged.connect(self.colorchange)
            self.clk.colorSelected.connect(self.colorpick)
            self.update()

    def colorpick(self, color):
        self.color = color

    def colorchange(self, color):
        self.Bcolor = color


def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()


if len(sys.argv) == 2 and sys.argv[1] == '1':
    main()


# %% 2
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, QThread

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.d = 100
        self.x = 0
        self.y = 0
        self.vx = 20
        self.vy = 20
        self.initUI()
        self.initTimer()

    def initUI(self):
        self.setGeometry(40, 40, 600, 400)
        self.show()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawbackground(qp)
        self.drawball(qp)
        qp.end()
    
    def drawball(self, qp):
        qp.setPen(QColor(255, 0, 0))
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
        
    def drawbackground(self, qp):
        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        
    def animate(self):
        self.x += self.vx
        self.y += self.vy
        self.checkCollision()
        self.update()
        
    def initTimer(self):
        
        self.t = QTimer()
        self.t.timeout.connect(self.timer_method)
        self.t.start(1)
        
    def timer_method(self):
        self.animate()
        
        
    def checkCollision(self):
        if (self.x == 0 and self.vx < 0) or (self.x+self.d == self.width() and self.vx > 0):
           self.vx *= -1
        if (self.y == 0 and self.vy <0) or (self.y+self.d == self.height() and self.vy > 0):
           self.vy *= -1
        if self.x+self.d > self.width():
            self.vx = -20
        if self.y+self.d > self.height():
            self.vy = -20
        
def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()


if len(sys.argv) == 2 and sys.argv[1] == '2':
    main()
