#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: Victor He
"""

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.doubleClicked = False
        self.x = 0
        self.y = 0
        self.verts = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Final Widget')
        self.setGeometry(50, 50, 600, 400)
        self.show()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawbg(qp)
        self.drawE(qp)
        qp.end()
        
    def drawbg(self, qp):
        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(0, 0, self.width(), self.height())
        
    def mousePressEvent(self, event):
        if self.doubleClicked is True:
            self.verts.clear()
            self.doubleClicked = False
        self.verts.append((event.x(),event.y()))
        self.update()
        
    def mouseDoubleClickEvent(self, event):
        if len(self.verts) > 1:
            self.doubleClicked = True
            self.update()
        
    def drawE(self, qp):
        qp.setPen(QColor(0, 0, 255))
        qp.setBrush(QColor(0, 0, 255))
        i = 0
        if len(self.verts) > 1:
            while i < (len(self.verts)-1):
                qp.drawLine(self.verts[i][0], self.verts[i][1], self.verts[i+1][0], self.verts[i+1][1])
                i += 1
            if self.doubleClicked is True:
                qp.drawLine(self.verts[0][0], self.verts[0][1], self.verts[-1][0], self.verts[-1][1])
def main():
    app = QApplication([])
    w = MyWidget()
    app.exec_()

main()
