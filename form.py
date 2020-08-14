# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form(object):
    def batting(self,player_name):
        name=player_name
        self.curs.execute("select scored from match where player='{}';".format(name))
        runs=self.curs.fetchone()
        runs=runs[0]
        self.curs.execute("select fours from match where player='{}';".format(name))
        four=self.curs.fetchone()
        four=four[0]
        self.curs.execute("select sixes from match where player='{}';".format(name))
        six=self.curs.fetchone()
        six=six[0]
        self.curs.execute("select faced from match where player='{}';".format(name))
        balls=self.curs.fetchone()
        balls=balls[0]
        self.curs.execute("select catched from match where player='{}';".format(name))
        catched=self.curs.fetchone()
        catched=catched[0]
        self.curs.execute("select stumping from match where player='{}';".format(name))
        stumping=self.curs.fetchone()
        stumping=stumping[0]
        self.curs.execute("select ro from match where player='{}';".format(name))
        ro=self.curs.fetchone()
        ro=ro[0]
        field=int(catched)+int(stumping)+int(ro)
        try:
            strike_rate=(runs/balls)*100
        except:
            strike_rate=0
        two=runs//2
        points=two+four+(2*six)+(field*10)
        if strike_rate>80 and strike_rate<100:
            points=points+2
        elif strike_rate>=100:
            points=points+4
        if runs>50:
            points=points+5
        if runs>=100:
            points=points+10
        self.listWidget_points.addItem(str(points))
        self.total_points+=points
        self.label_spoints.setText(str(self.total_points))

    def ar(self,player_name):
        name=player_name
        self.curs.execute("select scored from match where player='{}';".format(name))
        runs=self.curs.fetchone()
        runs=runs[0]
        self.curs.execute("select fours from match where player='{}';".format(name))
        four=self.curs.fetchone()
        four=four[0]
        self.curs.execute("select sixes from match where player='{}';".format(name))
        six=self.curs.fetchone()
        six=six[0]
        self.curs.execute("select faced from match where player='{}';".format(name))
        balls=self.curs.fetchone()
        balls=balls[0]
        self.curs.execute("select catched from match where player='{}';".format(name))
        catched=self.curs.fetchone()
        catched=catched[0]
        self.curs.execute("select stumping from match where player='{}';".format(name))
        stumping=self.curs.fetchone()
        stumping=stumping[0]
        self.curs.execute("select ro from match where player='{}';".format(name))
        ro=self.curs.fetchone()
        ro=ro[0]
        field=int(catched)+int(stumping)+int(ro)
        try:
            strike_rate=(runs/balls)*100
        except:
            strike_rate=0
        two=runs//2
        points=two+four+(2*six)+(field*10)
        if strike_rate>80 and strike_rate<100:
            points=points+2
        elif strike_rate>=100:
            points=points+4
        if runs>50:
            points=points+5
        if runs>=100:
            points=points+10

        self.curs.execute("select wkts from match where player='{}';".format(name))
        wkts=self.curs.fetchone()
        wkts=wkts[0]

        self.curs.execute("select bowled from match where player='{}';".format(name))
        bowled=self.curs.fetchone()
        bowled=bowled[0]
        overs=bowled/6
        
        self.curs.execute("select given from match where player='{}';".format(name))
        runs_given=self.curs.fetchone()
        runs_given=runs_given[0]
        if float(overs)!=0:
            economy_rate=float(runs_given)/float(overs)
        else:
            economy_rate=500
        points+=(int(wkts)*10)
        if int(wkts)>=3 and int(wkts)<5:
            points+=5
        if int(wkts)>=5:
            points+=10
        if economy_rate>3.5 and economy_rate<=4.5:
            points+=4
        elif economy_rate>2 and economy_rate<=3.5:
            points+=7
        elif economy_rate<=2:
            points+=10
        elif economy_rate==500:
            points+=0
        self.listWidget_points.addItem(str(points))
        self.total_points+=points
        self.label_spoints.setText(str(self.total_points))

    def bowling(self,player_name):
        name=player_name
        self.curs.execute("select wkts from match where player='{}';".format(name))
        wkts=self.curs.fetchone()
        wkts=wkts[0]

        self.curs.execute("select bowled from match where player='{}';".format(name))
        bowled=self.curs.fetchone()
        bowled=bowled[0]
        overs=bowled/6
        
        self.curs.execute("select given from match where player='{}';".format(name))
        runs_given=self.curs.fetchone()
        runs_given=runs_given[0]
        economy_rate=float(runs_given)/float(overs)

        self.curs.execute("select catched from match where player='{}';".format(name))
        catched=self.curs.fetchone()
        catched=catched[0]
        self.curs.execute("select stumping from match where player='{}';".format(name))
        stumping=self.curs.fetchone()
        stumping=stumping[0]
        self.curs.execute("select ro from match where player='{}';".format(name))
        ro=self.curs.fetchone()
        ro=ro[0]
        field=int(catched)+int(stumping)+int(ro)
        points=(field*10)

        points+=(int(wkts)*10)
        if int(wkts)>=3 and int(wkts)<5:
            points+=5
        if int(wkts)>=5:
            points+=10
        if economy_rate>3.5 and economy_rate<=4.5:
            points+=4
        elif economy_rate>2 and economy_rate<=3.5:
            points+=7
        elif economy_rate<=2:
            points+=10
        self.listWidget_points.addItem(str(points))
        self.total_points+=points
        self.label_spoints.setText(str(self.total_points))

    def evaluate_points(self):
        self.listWidget_points.clear()
        for x in range(len(self.players_list)):
            if self.evaluate_check==0:
                self.listWidget_points.addItems(self.tempo_list)
                break
            self.curs.execute("select ctg from stats where player='{}';".format(self.players_list[x]))
            temp=self.curs.fetchone()
            if temp[0]=="BAT" or temp[0]=="WK":
                self.batting(self.players_list[x])
            elif temp[0]=="BWL":
                self.bowling(self.players_list[x])
            elif temp[0]=="AR":
                self.ar(self.players_list[x])
        for y in range(self.listWidget_points.count()):
            self.tempo_list.append(self.listWidget_points.item(y).text())
        self.evaluate_check=0
    def show_players(self):
        self.evaluate_check=1
        self.total_points=0
        self.listWidget_players.clear()
        self.curs.execute("select players from teams where name='{}';".format(self.comboBox_team.currentText()))
        result=self.curs.fetchall()
        for record in result:
            self.players_list=record[0].split(" ")
        self.players_list.pop()
        self.listWidget_players.addItems(self.players_list)
    def setupUi3(self, Form):
        self.tempo_list=[]
        self.evaluate_check=0
        conn=sqlite3.connect("FantasyCricket.db")
        self.curs=conn.cursor()
        self.curs.execute("select name from teams;")
        result=self.curs.fetchall()
        self.teams_list=[]
        self.players_list=[]
        for record in result:
            self.teams_list.append(record[0])
        Form.setObjectName("Form")
        Form.resize(843, 681)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 120, 841, 551))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(530, 30, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_spoints = QtWidgets.QLabel(self.widget)
        self.label_spoints.setGeometry(QtCore.QRect(610, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_spoints.setFont(font)
        self.label_spoints.setObjectName("label_spoints")
        self.listWidget_players = QtWidgets.QListWidget(self.widget)
        self.listWidget_players.setGeometry(QtCore.QRect(60, 90, 301, 421))
        self.listWidget_players.setStyleSheet("color: rgb(255, 0, 0);")
        self.listWidget_players.setObjectName("listWidget_players")
        self.listWidget_points = QtWidgets.QListWidget(self.widget)
        self.listWidget_points.setGeometry(QtCore.QRect(480, 90, 301, 421))
        self.listWidget_points.setStyleSheet("color: rgb(0, 0, 255);")
        self.listWidget_points.setObjectName("listWidget_points")

        self.label_2.raise_()
        self.label_3.raise_()
        self.label_spoints.raise_()
        self.listWidget_players.raise_()
        self.listWidget_points.raise_()
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 20, 911, 80))
        self.widget_2.setObjectName("widget_2")
        self.comboBox_team = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_team.setGeometry(QtCore.QRect(120, 41, 181, 31))
        self.comboBox_team.setAccessibleDescription("")
        self.comboBox_team.setEditable(True)
        self.comboBox_team.setCurrentText("Select Team")
        self.comboBox_team.setMaxVisibleItems(20)
        self.comboBox_team.setObjectName("comboBox_team")
        self.comboBox_team.addItems(self.teams_list)
        self.comboBox_match = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_match.setGeometry(QtCore.QRect(542, 41, 201, 31))
        self.comboBox_match.setEditable(True)
        self.comboBox_match.setCurrentText("Select Match")
        self.comboBox_match.setObjectName("comboBox_match")
        self.comboBox_match.addItem("match1")
        self.label_message = QtWidgets.QLabel(self.widget_2)
        self.label_message.setGeometry(QtCore.QRect(20, 0, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_message.setFont(font)
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 110, 751, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.ok = QtWidgets.QPushButton(self.widget)
        self.ok.setGeometry(QtCore.QRect(320, 520, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.ok.clicked.connect(self.evaluate_points)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.comboBox_team.activated.connect(self.show_players)
        

        



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Fantasy Cricket"))
        self.label_2.setText(_translate("Form", "Players"))
        self.label_3.setText(_translate("Form", "Points"))
        self.label_spoints.setText(_translate("Form", "0"))
        self.label_message.setText(_translate("Form", "Evaluate the Performance of Your Fantasy Teams"))
        self.ok.setText(_translate("Form", "Evaluate Points"))


if __name__ == "__main__":
    import sys
    import sqlite3
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi3(Form)
    Form.show()
    sys.exit(app.exec_())
