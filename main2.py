# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from form import *
import sqlite3


class Ui_MainWindow2(object):

    def save(self,i):
        count=0
        temp=""
        tempo=0
        conn=sqlite3.connect("FantasyCricket.db")
        curs=conn.cursor()
        for x in range(len(self.list2)):
            curs.execute("select ctg from stats where player='{}';".format(self.list2[x]))
            ctg=curs.fetchone()
            if ctg[0]=="WK":
                count+=1

        if count<1:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning !")
            msg.setText("Atleast one Wicket-keeper required !")
            msg.setIcon(msg.Critical)
            x=msg.exec_()
            tempo=1
        elif count>1:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning !")
            msg.setText("No more than one Wicket-keeper !")
            msg.setIcon(msg.Critical)
            x=msg.exec_()
            tempo=1


        if i.text()=="Save" and self.total_points<=1000 and tempo==0:
            if self.wk_check_count>1:
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Warning !")
                msg.setText("No more than one Wicket-keeper !")
                msg.setIcon(msg.Critical)
                x=msg.exec_()
            elif self.label_15.text()=="":
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Warning !")
                msg.setText("Enter Team Name !")
                msg.setIcon(msg.Critical)
                x=msg.exec_()
            else:
                for x in range(self.listWidget_2.count()):
                    temp=self.listWidget_2.item(x).text()+" "+temp
                curs.execute("insert into teams values ('{}','{}','0');".format(self.label_15.text(),temp))
                conn.commit()
                conn.close()
                msg1=QtWidgets.QMessageBox()
                msg1.setWindowTitle("Saved ☺")
                msg1.setText("Team saved successfully ☺")
                msg1.setIcon(msg1.Information)
                y=msg1.exec_()
        else:
            if tempo==0:
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Alert !")
                msg.setText("You can not exceed points limit !")
                msg.setIcon(msg.Critical)
                x=msg.exec_()
                

    def message_box(self):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("Alert !")
        msg.setText("Number of Players can not exceed eleven !")
        msg.setIcon(msg.Critical)
        x=msg.exec_()

    def dialog(self):

        self.msg=QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Alert !")
        if self.listWidget_2.count()==0:
            self.msg.setIcon(self.msg.Critical)
            self.msg.setText("Please select players before saving")
        elif self.listWidget_2.count()>0 and self.listWidget_2.count()<11:
            self.msg.setIcon(self.msg.Critical)
            self.msg.setText("Insufficient number of players to form a team!")
        elif self.listWidget_2.count()==11:
            self.msg.setIcon(self.msg.Information)
            self.msg.setText("Do you want to save this team?")
            self.msg.setStandardButtons(self.msg.Save|self.msg.Cancel)
            self.msg.buttonClicked.connect(self.save)
        x=self.msg.exec_()


    def form_evaluate(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi3(self.Form)
        self.Form.show()

    def nothing(self):
        a=0

    def pop_2(self):

        temp=self.listWidget_2.currentItem().text()
        if temp in self.per_bat_list and self.check=="bat":
            item2=self.listWidget_2.takeItem(self.listWidget_2.currentRow())
            self.listWidget.addItem(item2)
        elif temp in self.per_bwl_list and self.check=="bwl":
            item2=self.listWidget_2.takeItem(self.listWidget_2.currentRow())
            self.listWidget.addItem(item2)
        elif temp in self.per_ar_list and self.check=="ar":
            item2=self.listWidget_2.takeItem(self.listWidget_2.currentRow())
            self.listWidget.addItem(item2)
        elif temp in self.per_wk_list and self.check=="wk":
            item2=self.listWidget_2.takeItem(self.listWidget_2.currentRow())
            self.listWidget.addItem(item2)
            self.wk_check_count-=1
        else:
            self.listWidget_2.takeItem(self.listWidget_2.currentRow())

        if temp in self.per_bat_list:
            self.bat_list.append(temp)
            self.bat_count-=1
            self.label_3.setText(str(self.bat_count))

            self.total_points-=int(self.dict_values[temp])
            self.remaining_points+=int(self.dict_values[temp])
            self.label_12.setText(str(self.remaining_points))
            self.label_13.setText(str(self.total_points))
        elif temp in self.per_bwl_list:
            self.bwl_list.append(temp)
            self.bow_count-=1
            self.label_5.setText(str(self.bow_count))

            self.total_points-=int(self.dict_values[temp])
            self.remaining_points+=int(self.dict_values[temp])
            self.label_12.setText(str(self.remaining_points))
            self.label_13.setText(str(self.total_points))
        elif temp in self.per_ar_list:
            self.ar_list.append(temp)
            self.ar_count-=1
            self.label_7.setText(str(self.ar_count))

            self.total_points-=int(self.dict_values[temp])
            self.remaining_points+=int(self.dict_values[temp])
            self.label_12.setText(str(self.remaining_points))
            self.label_13.setText(str(self.total_points))
        elif temp in self.per_wk_list:
            self.wk_list.append(temp)
            self.wk_count-=1
            self.label_9.setText(str(self.wk_count))

            self.total_points-=int(self.dict_values[temp])
            self.remaining_points+=int(self.dict_values[temp])
            self.label_12.setText(str(self.remaining_points))
            self.label_13.setText(str(self.total_points))
        
        else:
            self.nothing()

        if self.listWidget_2.count()==11:
            self.check_message=100
        elif self.listWidget_2.count()>0 and self.listWidget_2.count()<11:
            self.check_message=2
        elif self.listWidget_2.count==0:
            self.check_message=1

        self.list2.pop(self.list2.index(temp))

    def pop_1(self):
        if len(self.list2)<11 or len(self.list2)==None:
            temp=self.listWidget.currentItem().text()
            item2=self.listWidget.takeItem(self.listWidget.currentRow())
            self.listWidget_2.addItem(item2)

            if self.check=="bat":
                self.list2.append(self.bat_list.pop(self.bat_list.index(temp)))
                self.bat_count+=1
                self.label_3.setText(str(self.bat_count))

                self.total_points+=int(self.dict_values[temp])
                self.remaining_points-=int(self.dict_values[temp])
                self.label_12.setText(str(self.remaining_points))
                self.label_13.setText(str(self.total_points))
            elif self.check=="bwl":
                self.list2.append(self.bwl_list.pop(self.bwl_list.index(temp)))
                self.bow_count+=1
                self.label_5.setText(str(self.bow_count))

                self.total_points+=int(self.dict_values[temp])
                self.remaining_points-=int(self.dict_values[temp])
                self.label_12.setText(str(self.remaining_points))
                self.label_13.setText(str(self.total_points))
            elif self.check=="ar":
                self.list2.append(self.ar_list.pop(self.ar_list.index(temp)))
                self.ar_count+=1
                self.label_7.setText(str(self.ar_count))

                self.total_points+=int(self.dict_values[temp])
                self.remaining_points-=int(self.dict_values[temp])
                self.label_12.setText(str(self.remaining_points))
                self.label_13.setText(str(self.total_points))
            elif self.check=="wk":
                self.list2.append(self.wk_list.pop(self.wk_list.index(temp)))
                self.wk_count+=1
                self.label_9.setText(str(self.wk_count))

                self.total_points+=int(self.dict_values[temp])
                self.remaining_points-=int(self.dict_values[temp])
                self.label_12.setText(str(self.remaining_points))
                self.label_13.setText(str(self.total_points))
            else:
                self.nothing()
            if self.listWidget_2.count()==11:
                self.check_message=100
            elif self.listWidget_2.count()>0 and self.listWidget_2.count()<11:
                self.check_message=2
            elif self.listWidget_2.count==0:
                self.check_message=1
        else:
            self.message_box()

    def bat(self):
        self.listWidget.clear()
        self.listWidget.addItems(self.bat_list)
        self.check="bat"

    def bow(self):
        self.listWidget.clear()
        self.check="bwl"
        self.listWidget.addItems(self.bwl_list)

    def ar(self):
        self.listWidget.clear()
        self.check="ar"
        self.listWidget.addItems(self.ar_list)



    def wk(self):
        self.listWidget.clear()
        self.check="wk"
        self.listWidget.addItems(self.wk_list)



    def setupUi2(self, MainWindow):
        self.check_wk=""
        self.bat_count=0
        self.bow_count=0
        self.ar_count=0
        self.wk_count=0
        self.wk_check_count=0
        self.check_message=0
        self.list2=[]
        self.dict_values={}
        self.total_points=0
        self.remaining_points=1000
        self.bat_list,self.per_bat_list=[],[]
        self.bwl_list,self.per_bwl_list=[],[]
        self.ar_list,self.per_ar_list=[],[]
        self.wk_list,self.per_wk_list=[],[]
        self.check=""
        conn=sqlite3.connect("FantasyCricket.db")
        curs=conn.cursor()
        curs.execute("select player from stats where ctg='BAT';")
        result=curs.fetchall()
        for record in result:
            temp=str(record[0])
            self.bat_list.append(temp)
            self.per_bat_list.append(temp)
        curs.execute("select player from stats where ctg='BWL';")
        result=curs.fetchall()
        for record in result:
            temp=str(record[0])
            self.bwl_list.append(temp)
            self.per_bwl_list.append(temp)
        curs.execute("select player from stats where ctg='AR';")
        result=curs.fetchall()
        for record in result:
            temp=str(record[0])
            self.ar_list.append(temp)
            self.per_ar_list.append(temp)
        curs.execute("select player from stats where ctg='WK';")
        result=curs.fetchall()
        for record in result:
            temp=str(record[0])
            self.wk_list.append(temp)
            self.per_wk_list.append(temp)

        curs.execute("select player,value from stats;")
        result=curs.fetchall()
        for record in result:
            temp=str(record[0])
            temp_values=str(record[1])
            self.dict_values.update({temp:temp_values})



        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 901, 91))
        self.frame.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(220, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(350, 50, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(440, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(590, 50, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(660, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(830, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 170, 391, 511))
        self.widget.setObjectName("widget")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(self.bat)

        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 30, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(self.bow)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 30, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_3.clicked.connect(self.ar)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(310, 30, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_4.clicked.connect(self.wk)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 341, 411))
        self.listWidget.setStyleSheet("color: rgb(255, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        
        self.listWidget.clicked.connect(self.pop_1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(540, 170, 391, 511))
        self.widget_2.setObjectName("widget_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 70, 341, 411))
        self.listWidget_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.listWidget_2.clicked.connect(self.pop_2)
        self.label_14.setGeometry(QtCore.QRect(30, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLineEdit(self.widget_2)
        self.label_15.setGeometry(QtCore.QRect(150, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(540, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(210, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(660, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.actionNEW_Team.triggered.connect(self.nothing)
        self.actionSAVE_Team.triggered.connect(self.dialog)
        self.actionOPEN_Team.triggered.connect(self.form_evaluate)
        self.actionEVALUATE_Team.triggered.connect(self.form_evaluate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "All rounders (AR)"))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_9.setText(_translate("MainWindow", ""))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_14.setText(_translate("MainWindow", "Team Name"))
        self.label_15.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", "Points Available"))
        self.label_11.setText(_translate("MainWindow", "Points Used"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", ""))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
