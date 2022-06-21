from ui_login import *
from ui_Splash import *
from database import *
from ui_Dashboard_admin import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer 
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit, QDialog
from PyQt5.QtWidgets import QApplication
import sys
#import PySide2
from PySide2 import *
import os
from PyQt5.uic import loadUiType
from PySide2 import QtGui
from Custom_Widgets.Widgets import *
import sqlite3 as sql


#-----------------Dashboard----------------------------

class Main(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.dashBoard()
        self.showMaximized()
        self.Handel_Buttons()

    def Handel_Buttons(self):

        #----------------MenuButtons---------------------

        self.ui.dashboard_btn.clicked.connect(lambda: self.dashBoard())
        self.ui.Hospital_btn.clicked.connect(lambda: self.WholeSalerPage())
        self.ui.sale_history_btn.clicked.connect(lambda: self.SaleHistory())
        self.ui.users_btn.clicked.connect(lambda: self.UserPage())
        self.ui.inventory_btn.clicked.connect(lambda: self.pageDisease())
        self.ui.custom_querying.clicked.connect(lambda: self.CustomQuery())
        self.ui.developer_info.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.info_page))
        # self.ui.inventory_sort1_combo.currentIndexChanged.connect(lambda: self.Inventory_Combo_Details())
        #--------------------------------------------------

        #---------------TopMenuButtons---------------------

        self.ui.logout_btn.clicked.connect(self.logOut)        
        self.ui.users_btn_2.clicked.connect(lambda: self.PopUser())
        self.ui.refresh_btn.clicked.connect(lambda: self.refresh())

        # #--------------------------------------------------

        # #-----------------WholesalerPageButtons-----------------

        self.ui.wholesaler_show_all_btn.clicked.connect(lambda: self.wholesalerAll())
        self.ui.wholesaler_sort1_combo.currentIndexChanged.connect(lambda: self.WholeSalerCombo1())
        self.ui.wholesaler_search.clicked.connect(lambda: self.WholeSalerSearch())        
        self.ui.Wholesaler_RadioButton.toggled.connect(lambda: self.WholeSalerSortReset())
        self.ui.wholesaler_add_btn.clicked.connect(lambda: self.AddWholeSaler())
        self.ui.wholesaler_clear_btn.clicked.connect(lambda: self.WholeSalerPageClear())
        self.ui.wholesaler_update_btn.clicked.connect(lambda: self.WholeSalerPageUpdate())
        # self.ui.wholesaler_addmore_btn_2.clicked.connect(lambda: self.WholeSalerPageAddChemical())

        # #--------------------------------------------------

        # #-----------------NewProduct-ChemicalPageButtons-----------------

        self.ui.new_show_all_btn.clicked.connect(lambda: self.DiseasesAll())
        self.ui.radioButton.toggled.connect(lambda: self.DiseaseSortReset())
        # self.ui.exit_btn.clicked.connect(lambda: self.)

        # #--------------------------------------------------

        # #-----------------SaleHistoryPageButtons-----------------

        self.ui.sale_history_show_all_btn.clicked.connect(lambda: self.SaleHistoryAll())
        self.ui.sale_history_delete.clicked.connect(lambda: self.SaleHistoryDel())
        self.ui.sale_history_search_btn.clicked.connect(lambda: self.SaleHistorySearchCombo2())
        self.ui.sale_history_checkbox.toggled.connect(lambda: self.SaleHistorySortReset())
        self.ui.sale_history_sort1_combo.currentIndexChanged.connect(lambda: self.Historycombo())
        #self.ui.sale_history_deleteAll.clicked.connect(lambda: self.SaleHistoryDeleteAll())

        # #--------------------------------------------------

        # #-----------------UsersPageButtons-----------------

        self.ui.users_add_btn.clicked.connect(lambda: self.UserAdd())
        self.ui.uses_clear_btn.clicked.connect(lambda: self.UserClear())
        self.ui.users_delete_btn.clicked.connect(lambda: self.UserDel())
        self.ui.users_update_btn.clicked.connect(lambda: self.UserUpdate())
        self.ui.User_RadioBtn.toggled.connect(lambda: self.UserTableSorting())

        # #--------------------------------------------------

        # #-----------------CustomQueryPageButtons-----------------

        self.ui.query_search.clicked.connect(lambda: self.QuerySearch())
        self.ui.query_reset.clicked.connect(lambda: self.QueryTableReset())
        self.ui.query_RadioBtn.toggled.connect(lambda: self.QueryTableSorting())
        self.ui.query_clear.clicked.connect(lambda: self.QueryClear())
        self.ui.query1.clicked.connect(lambda: self.Query1())
        self.ui.query2.clicked.connect(lambda: self.Query2())
        self.ui.query3.clicked.connect(lambda: self.Query3())
        self.ui.query4.clicked.connect(lambda: self.Query4())
        self.ui.query5.clicked.connect(lambda: self.Query5())
        self.ui.query_header.clicked.connect(lambda: self.InputHeader())

        # #--------------------------------------------------


    #------------TopButtonFunctionalities-----------------------

    def logOut(self):
        self.close()
        print("You have been successfully logged out!")
        QMessageBox.information(self, "Logout", Login.User_Name+"\nYou have been successfully logged out!")

    def PopUser(self):
        QMessageBox.information(self, "User Details", "User Name : "+Login.User_ID+"\nName : "+Login.User_Name+"\nID : "+Login.ID+"\nID : "+Login.Type)
              
    def refresh(self):
        DataBase_Connection()

    #-----------------------------------------------------

    #---------------Dashboard Setup-----------------------
    def dashBoard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
        self.ui.user_name.setText(Login.User_Name)
        self.dashBoardDetails()

    def dashBoardDetails(self):
        self.ui.number_of_Hospitals.setText(DataBase_Connection.totalhospital(self))
        self.ui.number_of_cases.setText(DataBase_Connection.totalsearchhistory(self))
        self.ui.number_of_doctors.setText(DataBase_Connection.numberdoctors(self))
        self.ui.total_users.setText(DataBase_Connection.totalusers(self))
        self.ui.total_diseases.setText(DataBase_Connection.totaldiseases(self))

    #--------------------------------------------------------

    #-----------------------Diseases-------------------------

    def pageDisease(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_new)

    def DiseasesAll(self):
        self.ui.tableWidget_6.setHorizontalHeaderLabels(['illnessID', 'illnessName', 'Agent Name', 'Symptomps',''])
        query1 = '''SELECT DISTINCT I.IllnessID, I.Illnessname, A.Agentname, S.Symptompname
                    from ILLNESS I, SYMPTOMPS S, AGENT A
                    where I.IllnessID = A.IllnessID and S.IllnessID = I.IllnessID'''
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute(query1)
            row = cursor.fetchall()
            self.ui.tableWidget_6.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_6.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_6.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def DiseaseSortReset(self):
        if self.ui.radioButton.isChecked():
            self.ui.tableWidget_6.setSortingEnabled(True)
        else:
            self.ui.tableWidget_6.setSortingEnabled(False)

    #-------------------------------------------------------

    #-------------------WholeSalerPage-----------------------

    def WholeSalerPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_wholesaler)
        self.WholeSalerCombo1()
        # self.wholeSalerPageCombo()

    def wholesalerAll(self):
        self.ui.tableWidget_3.setHorizontalHeaderLabels(['Hospital ID', 'Name', 'DeptID', 'Doctor Name', 'Phone Number', 'City', 'State'])         
        query = ''' SELECT DISTINCT H.HospitalID, H.Name, D.DeptID, D.Doctorname, H.Phnumber, H.City, H.State
                    FROM HOSPITAL H, DEPARTMENT D
                    WHERE H.HospitalID = D.HospitalID '''
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            self.ui.tableWidget_3.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_3.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_3.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def WholeSalerCombo1(self):
        self.ui.wholesaler_sort2_combo.clear()
        item = self.ui.wholesaler_sort1_combo.currentText()
        if item == 'Hospital':
            try:
                conn = sql.connect('IDMS.db')
                cursor = conn.cursor()
                cursor.execute('''SELECT Name from HOSPITAL''')
                row = cursor.fetchall()
                for i in row:
                    self.ui.wholesaler_sort2_combo.addItems(i)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def WholeSalerSearch(self):
        Combo1 = self.ui.wholesaler_sort1_combo.currentText()
        Combo2 = self.ui.wholesaler_sort2_combo.currentText()
        query1 = '''SELECT H.HospitalID, H.Name, D.Deptname, D.Doctorname,I.Illnessname, H.Phnumber, H.City, H.State
                    FROM HOSPITAL H, DEPARTMENT D, AGENT A, ILLNESS I
                    WHERE H.HospitalID = D.HospitalID and H.Name = ? and D.AgentID = A.AgentID and A.IllnessID = I.IllnessID'''

        if Combo1 == 'Hospital':
            if (Combo2 != ''):
                try:
                    self.ui.tableWidget_3.setHorizontalHeaderLabels(['Hospital ID', 'Name', 'Department', 'Doctor','Illness Name', 'Phone Number', 'City', 'State'])
                    conn = sql.connect('IDMS.db')
                    cursor = conn.cursor()
                    cursor.execute(query1, (Combo2,))
                    row = cursor.fetchall()
                    self.ui.tableWidget_3.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.tableWidget_3.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.tableWidget_3.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            else:
                QMessageBox.warning(self, "Error", "Nothing Is Selected/DataBase is Empty")


    def WholeSalerSortReset(self):
        if self.ui.Wholesaler_RadioButton.isChecked():
            self.ui.tableWidget_3.setSortingEnabled(True)
        else:
            self.ui.tableWidget_3.setSortingEnabled(False)

    def AddWholeSaler(self):
        hospitalName = self.ui.wholesaler_name.text()
        phno = self.ui.wholesaler_phone_no.text()
        city = self.ui.wholesaler_address.text()
        doctor = self.ui.wholesaler_id_number_3.text()
        state = self.ui.wholesaler_id_number.text()
        dept = self.ui.departmentcombo1.currentText()
        Illness = self.ui.illnessNameCombo.currentText()
        query1 = '''insert into HOSPITAL(Name, Phnumber, City, State) values (?,?,?,?)'''
        query2 = '''SELECT HospitalID from HOSPITAL where Name = ?'''
        query3 = '''select A.AgentID
                    from AGENT A, ILLNESS I
                    where  I.Illnessname = ? and I.IllnessID = A.IllnessID'''
        query4 = '''INSERT into DEPARTMENT(HospitalID, Deptname, Doctorname, AgentID) values (?,?,?,?) '''
        if (hospitalName != "" and phno != "" and city != "" and doctor != "" and state != ""  and dept != "" and phno.isdigit() ):
            phno = int(phno)
            try:
                conn = sql.connect('IDMS.db')
                cursor = conn.cursor()
                cursor.execute(query1, (hospitalName,phno, city, state,))
                conn.commit()
                try:
                    cursor.execute(query2, (hospitalName,))
                    row = cursor.fetchone()
                    hospitalID = int(row[0])
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
                try:
                    cursor.execute(query3, (Illness,))
                    row1 = cursor.fetchone()
                    agentID = int(row1[0])
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
                try:
                    cursor.execute(query4, (hospitalID, dept, doctor, agentID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the inputs again ")

    def WholeSalerPageAddChemical(self):
        query1 = '''select Dealer_Id, Chemical_Name from Dealer_Chemical_Supply where Dealer_Id = ? and Chemical_Name = ?'''
        query2 = '''insert into Dealer_Chemical_Supply (Dealer_Id, Chemical_Name) VALUES (?,?)'''
        Chemicals = []
        DealerID, ok = QInputDialog.getText(self, "Dealer ID", "Input Dealer ID")
        if ok == True and DealerID.isdigit():
            try:
                conn = sql.connect('IDMS.db')
                cursor = conn.cursor()
                cursor.execute('''select Chemical_Name from Chemical_Stock''')
                row = cursor.fetchall()
                for j in row:
                    for i in j:
                        Chemicals.append(str(i)) 
                chemical, select = QInputDialog.getItem(self, "Chemicals", "Select Chemical",Chemicals,0, False)
                if select and chemical:
                    try:
                        conn = sql.connect('IDMS.db')
                        cursor = conn.cursor()
                        cursor.execute(query1, (int(DealerID),str(chemical),))
                        row1 = cursor.fetchone()
                        if row1 is None:   
                            try:
                                cursor.execute(query2, (int(DealerID),str(chemical),))
                                conn.commit()
                                QMessageBox.information(self, "Succesfull", "Successfully Added")
                            except Exception as e:
                                print(e)
                                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
                        else:
                            QMessageBox.warning(self, "Error", "Dealer already Supplies the Chemical")
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))

    def WholeSalerPageClear(self):
        self.ui.wholesaler_name.setText('')
        self.ui.wholesaler_phone_no.setText('')
        self.ui.wholesaler_address.setText('')
        self.ui.wholesaler_id_number_3.setText('')
        self.ui.wholesaler_id_number.setText('')
        self.ui.departmentcombo1.setCurrentIndex(0)

    def WholeSalerPageUpdate(self):
        hospitalName = self.ui.wholesaler_name.text()
        dept = self.ui.departmentcombo1.currentText()
        doctor = self.ui.wholesaler_id_number_3.text()
        Illness = self.ui.illnessNameCombo.currentText()
        conn = sql.connect('IDMS.db')        
        query2 = '''select A.AgentID
                    from AGENT A, ILLNESS I
                    where  I.Illnessname = ? and I.IllnessID = A.IllnessID'''
        query3 = '''INSERT into DEPARTMENT(HospitalID, Deptname, Doctorname, AgentID) values (?,?,?,?) '''
        if (hospitalName != "") and doctor != '':
            try:
                conn = sql.connect('IDMS.db')  
                cursor= conn.cursor() 
                query = '''select HospitalID from HOSPITAL where Name = ? '''
                cursor.execute(query,(hospitalName,))
                row = cursor.fetchone()
                hospitalID = int(row[0])
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid Hospital Name")
                else:
                    try:
                        cursor.execute(query2, (Illness,))
                        row1 = cursor.fetchone()
                        agentID = int(row1[0])
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
                    try:
                        cursor.execute(query3, (hospitalID, dept, doctor, agentID,))
                        conn.commit()
                        QMessageBox.information(self, "Succesfull", "Successfully Updated")
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input all fields")

    #--------------------------------------------------------

    #----------------SaleHistory-------------------------
    def SaleHistory(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sale_history)

    def SaleHistoryAll(self):         
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT P.PatientID, U.Name, I.Illnessname, H.Name, D.Deptname, D.Doctorname, P.Date
                            FROM PATIENTHISTORY P, USERS U, ILLNESS I, DEPARTMENT D, HOSPITAL H
                            WHERE P.UserID = U.ID and P.IllnessID = I.IllnessID and P.DeptID = D.DeptID  and D.HospitalID = H.HospitalID ''')
            row = cursor.fetchall()
            self.ui.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_2.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def SaleHistoryDel(self):
        billNumber = self.ui.employee_update_ssn_3.text()
        conn = sql.connect('IDMS.db')        
        query2 = '''delete from PATIENTHISTORY where PatientID = ? '''
        if (billNumber != "") and billNumber.isdigit():
            billNumber = int(billNumber)
            try:
                conn = sql.connect('IDMS.db')  
                cursor= conn.cursor() 
                query = '''select PatientID from PATIENTHISTORY where PatientID = ? '''
                cursor.execute(query,(billNumber,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid Bill Number")
                else:
                    try:
                        cursor = conn.cursor()
                        cursor.execute(query2, (billNumber,))
                        conn.commit()
                        QMessageBox.information(self, "Successful", "Successfully Deleted from DataBase\nPlease Refresh")
                        self.ui.employee_update_ssn_3.setText("")
                    except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input all fields")


    def SaleHistoryDeleteAll(self):         
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''delete from PATIENTHISTORY''')
            conn.commit()
            QMessageBox.information(self, "Successful", "Successfully Deleted All Order in DataBase")
            self.SaleHistoryAll()
        except Exception as e:
            print(e)

    def SaleHistorySearch(self):
        billNumber = self.ui.sale_history_billsearch.text()
        conn = sql.connect('IDMS.db')        
        query = '''SELECT P.PatientID, U.Name, I.Illnessname, H.Name, D.Deptname, D.Doctorname, P.Date  
                   FROM PATIENTHISTORY P, USERS U, ILLNESS I, DEPARTMENT D, HOSPITAL H
                   WHERE P.UserID = U.ID and P.IllnessID = I.IllnessID and P.DeptID = D.DeptID  and D.HospitalID = H.HospitalID and P.PatientID = ? '''
        if (billNumber != "") and billNumber.isdigit():
            billNumber = int(billNumber)
            try:
                conn = sql.connect('IDMS.db')  
                cursor= conn.cursor() 
                cursor.execute(query,(billNumber,))
                row = cursor.fetchall()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid PatientID")
                else:
                    self.ui.tableWidget_2.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.tableWidget_2.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input any fields")

    def Historycombo(self):
        combo = self.ui.sale_history_sort1_combo.currentText()
        billNumber = self.ui.sale_history_billsearch.text()
        combo2 = self.ui.sale_history_sort2_combo.currentText()
        if combo == '' :
            pass
        elif combo == 'ILLNESS':
            self.Combo2Illness()
        elif combo == 'Hospital':
            self.Combo2Hospital()
        
    def Combo2Illness(self):
        self.ui.sale_history_sort2_combo.clear()
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT Illnessname from ILLNESS''')
            row = cursor.fetchall()
            self.ui.sale_history_sort2_combo.insertItem(0,'')
            for i in row:
                self.ui.sale_history_sort2_combo.addItems(i)
        except Exception as e:
            print(e)

    def Combo2Hospital(self):
        self.ui.sale_history_sort2_combo.clear()
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT Name from HOSPITAL''')
            row = cursor.fetchall()
            self.ui.sale_history_sort2_combo.insertItem(0,'')
            for i in row:
                self.ui.sale_history_sort2_combo.addItems(i)
        except Exception as e:
            print(e)

    def SaleHistorySearchCombo2(self):
        Allsort = self.ui.sale_history_sort1_combo.currentText()
        productsort = self.ui.sale_history_sort2_combo.currentText()
        billNumber = self.ui.sale_history_billsearch.text()
        conn = sql.connect('IDMS.db')        
        query1 = '''SELECT P.PatientID, U.Name, I.Illnessname, H.Name, D.Deptname, D.Doctorname, P.Date
                    FROM PATIENTHISTORY P, USERS U, ILLNESS I, DEPARTMENT D, HOSPITAL H
                    WHERE P.UserID = U.ID and P.IllnessID = I.IllnessID and P.DeptID = D.DeptID  
                    and D.HospitalID = H.HospitalID and I.Illnessname = ?'''

        query2 = '''SELECT P.PatientID, U.Name, I.Illnessname, H.Name, D.Deptname, D.Doctorname, P.Date
                    FROM PATIENTHISTORY P, USERS U, ILLNESS I, DEPARTMENT D, HOSPITAL H
                    WHERE P.UserID = U.ID and P.IllnessID = I.IllnessID and P.DeptID = D.DeptID  
                    and D.HospitalID = H.HospitalID and H.Name = ?'''

        if ((Allsort != "") and (productsort != "")):
            if (Allsort == 'ILLNESS'):
                try:
                    conn = sql.connect('IDMS.db')  
                    cursor= conn.cursor()
                    cursor.execute(query1,(productsort,))
                    row = cursor.fetchall()
                    if row is None:
                        QMessageBox.warning(self, "No Orders", "No Orders Yet")
                    else:
                        self.ui.tableWidget_2.setRowCount(0)
                        for row_number, row_data in enumerate(row):
                            self.ui.tableWidget_2.insertRow(row_number)
                            for coloumn_number, data in enumerate(row_data):
                                self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                            print(e)
                            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

            elif (Allsort == "Hospital"):
                try:
                    conn = sql.connect('IDMS.db')  
                    cursor= conn.cursor()
                    cursor.execute(query2, (productsort,))
                    row = cursor.fetchall()
                    if row is None:
                        QMessageBox.warning(self, "No Orders", "No Orders Yet")
                    else:
                        self.ui.tableWidget_2.setRowCount(0)
                        for row_number, row_data in enumerate(row):
                            self.ui.tableWidget_2.insertRow(row_number)
                            for coloumn_number, data in enumerate(row_data):
                                self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
                except Exception as e:
                            print(e)
                            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

        elif (((Allsort == "") and (productsort == "")) | billNumber.isdigit()):
            self.SaleHistorySearch()

        else:
            QMessageBox.information(self, "Table Sorting", "Enable Table Sorting to Use Custom Sort ")

    def SaleHistorySortReset(self):
        if self.ui.sale_history_checkbox.isChecked():
            self.ui.tableWidget_2.setSortingEnabled(True)
        else:
            self.ui.tableWidget_2.setSortingEnabled(False)
             
    #----------------------------------------------------

    #----------------CustomQueryPage--------------------

    def CustomQuery(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.custom_query)

    def QuerySearch(self):
        query = self.ui.query_inbox.toPlainText()
        self.QueryResults(query)

    def QueryResults(self, query):
        if (query != ""):
            try:
                conn = sql.connect('IDMS.db')  
                cursor= conn.cursor() 
                cursor.execute(query)
                row = cursor.fetchall()
                if row is None:
                    QMessageBox.warning(self, "Successfull", "Successfully Executed")
                else:
                    self.ui.query_table.setRowCount(0)
                    for row_number, row_data in enumerate(row):
                        self.ui.query_table.insertRow(row_number)
                        for coloumn_number, data in enumerate(row_data):
                            self.ui.query_table.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
            except Exception as e:
                        print(e)
                        QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Blank", "Input is Blank")

    def QueryTableReset(self):
        self.ui.query_table.setRowCount(0)
        self.ui.query_table.setHorizontalHeaderLabels(['','','','','','','','','','','',])

    def QueryTableSorting(self):
        if self.ui.query_RadioBtn.isChecked():
            self.ui.query_table.setSortingEnabled(True)
        else:
            self.ui.query_table.setSortingEnabled(False)

    def QueryClear(self):
        self.ui.query_inbox.clear()

    def Query1(self):
        self.QueryClear()
        query = 'select * from ILLNESS'
        self.ui.query_inbox.insertPlainText(query)

    def Query2(self):
        self.QueryClear()
        query = 'SELECT * from HOSPITAL'
        self.ui.query_inbox.insertPlainText(query)

    def Query3(self):
        self.QueryClear()
        query = 'select Doctorname from DEPARTMENT where DeptID=2;'
        self.ui.query_inbox.insertPlainText(query)

    def Query4(self):
        self.QueryClear()
        query = 'SELECT * from AGENT'
        self.ui.query_inbox.insertPlainText(query)

    def Query5(self):
        self.QueryClear()
        query = 'select * from SYMPTOMPS'
        self.ui.query_inbox.insertPlainText(query)

    def InputHeader(self):
        header, result = QInputDialog.getText(self, "InputHeader", "Input Header Names with ','")
        if result == True:
            result1 = header.split(',')
            self.ui.query_table.setHorizontalHeaderLabels(result1)

    #----------------------------------------------------

    #-----------------EmployeePage-----------------------

    def EmployeePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_employee)
        self.EmployeePageAll()

    def EmployeePageAll(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select * from Employee''')
            row = cursor.fetchall()
            self.ui.tableWidget_7.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_7.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_7.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def EmployeeTableSorting(self):
        if self.ui.Employee_RadioBtn.isChecked():
            self.ui.tableWidget_7.setSortingEnabled(True)
        else:
            self.ui.tableWidget_7.setSortingEnabled(False)

    #----------------------------------------------------

    #---------------------Users--------------------------

    def UserPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_users)
        self.UserPageAll()

    def UserPageAll(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select * from USERS''')
            row = cursor.fetchall()
            self.ui.tableWidget_5.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_5.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_5.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

    def UserAdd(self):
        name = self.ui.users_contact_no.text()
        username = self.ui.users_username.text()
        password = self.ui.users_password.text()
        Type = self.ui.users_id_type_combo.currentText()
        query1 = '''insert into USERS(Name,Username,Password,Type) values(?,?,?,?)'''

        if (name != "" and username != "" and password != "" and Type != "" ):
            try:
                conn = sql.connect('IDMS.db')
                cursor = conn.cursor()
                cursor.execute(query1, (name, username, password,Type,))
                conn.commit()
                QMessageBox.information(self, "Succesfull", "Successfully Added")
                self.UserPageAll()
                self.UserClear()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the inputs again ")

    def UserClear(self):
        self.ui.users_contact_no.setText('')
        self.ui.users_username.setText('')
        self.ui.users_password.setText('')
        self.ui.users_id_type_combo.setCurrentIndex(0)


    def UserDel(self):
        userID = self.ui.users_user_name.text()
        query1 = '''select * from USERS where ID = ?'''
        query2 = '''Delete from USERS where ID = ?'''
        if userID != '' and userID.isdigit():
            userID = int(userID)
            try:
                conn = sql.connect('IDMS.db')
                cursor = conn.cursor()
                cursor.execute(query1, (userID,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid User ID\nPlease check the inputs again ")
                else:
                    cursor.execute(query2, (userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
                    self.UserClear()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the inputs again ")

    def UserUpdate(self):
        userID = self.ui.users_user_name.text()
        userName = self.ui.users_current_password.text()
        userPassword = self.ui.users_new_password.text()
        query1 = '''select * from USERS where ID = ?'''
        query2 = '''update USERS set Username = ? where ID = ?'''
        query3 = '''update USERS set Username = ?, Password = ? where ID = ? '''
        query4 = '''update USERS set Password = ? where ID = ? '''
        if userID != '' and userID.isdigit():
            userID = int(userID)
            try:
                conn = sql.connect('IDMS.db')
                cursor = conn.cursor()
                cursor.execute(query1, (userID,))
                row = cursor.fetchone()
                if row is None:
                    QMessageBox.warning(self, "Invalid", "Invalid User ID\nPlease check the inputs again ")
                elif userName != '' and userPassword == '':
                    cursor.execute(query2, (userName,userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
                elif userName != '' and userPassword != '':
                    cursor.execute(query3, (userName,userPassword,userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
                elif userName == '' and userPassword != '':
                    cursor.execute(query4, (userPassword,userID,))
                    conn.commit()
                    QMessageBox.information(self, "Succesfull", "Successfully Added")
                    self.UserPageAll()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))
        else:
            QMessageBox.warning(self, "Error", "Please check the User ID")

    def UserTableSorting(self):
        if self.ui.User_RadioBtn.isChecked():
            self.ui.tableWidget_5.setSortingEnabled(True)
        else:
            self.ui.tableWidget_5.setSortingEnabled(False)

    #----------------------------------------------------


#---------------------main----------------------------
def main():
    app = QApplication.instance()
    if app is None: 
        app = QApplication(sys.argv)
        DataBase_Connection()
        login = Login()
        if login.exec_() == QDialog.Accepted:
            window = SplashScreen()
            window.show()
            sys.exit(app.exec_())

#------------------------------------------------------




#------------------mainDemo-----------------------------
def main2():
    app = QApplication(sys.argv)
    DataBase_Connection()
    window = Main()
    window.show()
    sys.exit(app.exec_())    

#-----------------------------------------------------




if __name__ == "__main__":
    main()



    
