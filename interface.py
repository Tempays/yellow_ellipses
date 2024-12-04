import io

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>615</width>
    <height>503</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="button">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>440</y>
     <width>131</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Создать круги</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(design)
        uic.loadUi(f, self)
        self.setFixedSize(615, 500)