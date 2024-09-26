# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>MainWindow</class>
#  <widget class="QMainWindow" name="MainWindow">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>780</width>
#     <height>600</height>
#    </rect>
#   </property>
#   <property name="font">
#    <font>
#     <pointsize>18</pointsize>
#    </font>
#   </property>
#   <property name="windowTitle">
#    <string>MainWindow</string>
#   </property>
#   <property name="styleSheet">
#    <string notr="true"/>
#   </property>
#   <widget class="QWidget" name="centralwidget">
#    <widget class="QLabel" name="titletrack">
#     <property name="geometry">
#      <rect>
#       <x>120</x>
#       <y>350</y>
#       <width>551</width>
#       <height>121</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>20</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="layoutDirection">
#      <enum>Qt::LeftToRight</enum>
#     </property>
#     <property name="text">
#      <string>Название трека</string>
#     </property>
#     <property name="alignment">
#      <set>Qt::AlignCenter</set>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="pause">
#     <property name="geometry">
#      <rect>
#       <x>340</x>
#       <y>480</y>
#       <width>90</width>
#       <height>100</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>60</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>||</string>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="back">
#     <property name="geometry">
#      <rect>
#       <x>170</x>
#       <y>480</y>
#       <width>121</width>
#       <height>100</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>90</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>&lt;</string>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="next">
#     <property name="geometry">
#      <rect>
#       <x>480</x>
#       <y>480</y>
#       <width>121</width>
#       <height>100</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>90</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>&gt;</string>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="addplaylist">
#     <property name="geometry">
#      <rect>
#       <x>0</x>
#       <y>240</y>
#       <width>180</width>
#       <height>101</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>Добавить</string>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="delplaylist">
#     <property name="geometry">
#      <rect>
#       <x>180</x>
#       <y>240</y>
#       <width>180</width>
#       <height>101</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>Удалить</string>
#     </property>
#    </widget>
#    <widget class="QLabel" name="title1">
#     <property name="geometry">
#      <rect>
#       <x>0</x>
#       <y>0</y>
#       <width>361</width>
#       <height>61</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>Список плейлистов</string>
#     </property>
#     <property name="alignment">
#      <set>Qt::AlignCenter</set>
#     </property>
#    </widget>
#    <widget class="QListWidget" name="listplaylist">
#     <property name="geometry">
#      <rect>
#       <x>0</x>
#       <y>50</y>
#       <width>361</width>
#       <height>191</height>
#      </rect>
#     </property>
#    </widget>
#    <widget class="QListWidget" name="listtrack">
#     <property name="geometry">
#      <rect>
#       <x>420</x>
#       <y>50</y>
#       <width>361</width>
#       <height>191</height>
#      </rect>
#     </property>
#    </widget>
#    <widget class="QLabel" name="title2">
#     <property name="geometry">
#      <rect>
#       <x>420</x>
#       <y>0</y>
#       <width>361</width>
#       <height>61</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>Список треков</string>
#     </property>
#     <property name="alignment">
#      <set>Qt::AlignCenter</set>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="addtrack">
#     <property name="geometry">
#      <rect>
#       <x>420</x>
#       <y>250</y>
#       <width>180</width>
#       <height>101</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>Добавить</string>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="deltrack">
#     <property name="geometry">
#      <rect>
#       <x>600</x>
#       <y>250</y>
#       <width>180</width>
#       <height>101</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#       <bold>true</bold>
#      </font>
#     </property>
#     <property name="text">
#      <string>Удалить</string>
#     </property>
#    </widget>
#   </widget>
#  </widget>
#  <resources/>
#  <connections/>
#  <slots>
#   <signal>signal1()</signal>
#  </slots>
# </ui>
