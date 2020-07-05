from pharmacy import Ui_MainWindow
from PyQt5 import QtWidgets
import sqlite3

class function(QtWidgets.QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.con = sqlite3.connect("pharmacy.sqlite")
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.delete)
        self.tableWidget.cellPressed.connect(self.edit)
        self.pushButton_3.clicked.connect(self.update)
        self.pushButton_5.clicked.connect(self.clear)
        self.druglist()




    def insert(self):
        self.cur.execute("insert into medicine values (? , ? , ? , ? ,? ,? , ? ,?)" , (self.lineEdit.text() , self.lineEdit_2.text() ,
                                                                                self.lineEdit_3.text() ,
                                                                                self.lineEdit_4.text() , self.lineEdit_5.text() ,
                                                                                self.lineEdit_6.text() ,
                                                                                self.lineEdit_7.text() , self.lineEdit_8.text()))
        self.con.commit()
        self.druglist()

    def druglist(self):
        self.cur.execute("Select * from medicine order by ROWID desc ")
        self.result = self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_no, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_no)
            for col_no, data in enumerate(row_data):
                self.tableWidget.setItem(row_no, col_no, QtWidgets.QTableWidgetItem(str(data)))




    def delete(self):
        if (self.lineEdit_2.text() == ''):
            print("Please , select the drug you want  to delete ")

        elif (self.tableWidget.currentItem().text()) :
            self.x = self.tableWidget.currentRow()
            self.y = self.tableWidget.item(self.x, 0).text()
            self.cur.execute("delete from medicine where drug_code = ? ", (self.y,))
            self.con.commit()
            self.druglist()


    def edit(self):
        self.x = self.tableWidget.currentRow()
        self.drug_code = self.tableWidget.item(self.x , 0).text()
        self.drug_name = self.tableWidget.item(self.x , 1).text()
        self.ex_date = self.tableWidget.item(self.x , 2).text()
        self.barcode_no = self.tableWidget.item(self.x , 3).text()
        self.price = self.tableWidget.item(self.x , 4).text()
        self.piece = self.tableWidget.item(self.x , 5).text()
        self.company = self.tableWidget.item(self.x , 6).text()
        self.usage = self.tableWidget.item(self.x , 7).text()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit.insert(self.drug_code)
        self.lineEdit_2.insert(self.drug_name)
        self.lineEdit_3.insert(self.ex_date)
        self.lineEdit_4.insert(self.barcode_no)
        self.lineEdit_5.insert(self.price)
        self.lineEdit_6.insert(self.piece)
        self.lineEdit_7.insert(self.company)
        self.lineEdit_8.insert(self.usage)

    def update(self):
        self.cur.execute("update medicine set drug_code = ? , drug_name = ? , expiration_date = ? , barcode_no = ? , price = ? , piece = ? ,\
                         producing_company = ? , usage = ? where drug_code = ?" , (self.lineEdit.text() , self.lineEdit_2.text() ,
                                                                                   self.lineEdit_3.text() , self.lineEdit_4.text() ,
                                                        self.lineEdit_5.text() , self.lineEdit_6.text() , self.lineEdit_7.text() ,
                                                                                   self.lineEdit_8.text() , self.drug_code))
        self.con.commit()
        self.druglist()

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()

    def search(self):
        if (self.lineEdit_2.text() != ''):
            self.cur.execute("select * from medicine")
            self.data = self.cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_data in self.data:
                if (row_data[1].lower() == self.lineEdit_2.text().lower()):
                    self.tableWidget.insertRow(0)
                    for col_no, data in enumerate(row_data):
                        self.tableWidget.setItem(0, col_no, QtWidgets.QTableWidgetItem(str(data)))











