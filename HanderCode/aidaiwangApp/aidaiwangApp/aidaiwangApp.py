# coding: utf-8
# encoding = utf-8

import shutil
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import All_OF_aidaiwang
import Login_aidaiwangApp
import Register_aidaiwangApp
import BuyObject_from_aidaiwangApp
import ChangePassword_from_aidaiwangApp
import RealName_Auth_from_aidaiwangApp
import Band_BankCard_from_aidaiwangApp
import Recharge_from_aidaiwangApp
import Deposit_from_aidaiwangApp
import Change_BankCard_from_aidaiwangApp
import LogOut_aidiawangApp

datasDir = 'C:/Users/aidai_TEC_QA/Documents/UserData.xls'

# noinspection PyTypeChecker
class FontPropertiesDlg(QDialog):

    def __init__(self, parent=None):

        self.filename = datasDir

        super(FontPropertiesDlg, self).__init__(parent)
        self.ObjectImg = QImage
        self.ObjectLabel = QLabel(u'爱贷网app(Android端)')
        self.ObjectLabel.setFixedSize(500, 60)
        self.ObjectLabel.setFont(QFont("Roman times", 20, QFont.Bold))
        self.ObjectLabel.setAlignment(Qt.AlignCenter)

        self.FunctionLabel = QLabel(u'测试用例')
        self.FunctionsComboBox = QComboBox()
        self.FunctionsComboBox.addItems(['All_Of_aidaiwang',
                                         'Log_In_aidaiwang',
                                         'Register_aidaiwang',
                                         'Buy_Object_aidaiwang',
                                         'Change_Password_aidaiwang',
                                         'RealName_Auth_aidaiwang',
                                         'Band_BankCard_aidaiwang',
                                         'Recharge_aidaiwang',
                                         'Deposit_aidaiwang',
                                         'Change_BankCard_aidaiwang',
                                         'Log_Out_aidaiwang'])

        self.UserDataFileLabel = QLabel(u'用例数据')
        self.UserDataFileAddress = QLineEdit(datasDir)
        self.UserDataFileDownload = QPushButton(u'下载数据样例')
        self.UserDataFileDownload.clicked.connect(self.createDataExcle)
        self.UserDataFileChangeButton = QPushButton(u'选择测试数据')
        self.UserDataFileChangeButton.clicked.connect(self.openExplorer)

        self.SaveLabel = QLabel(u'测试报告')
        self.ReportAddressLabel = QLineEdit(u'C:/Users/aidai_TEC_QA/Documents/report.xls')
        self.ChangeAddressButton = QPushButton(u'更改')
        self.ChangeAddressButton.setToolTip(u'更改报告目录')
        self.ChangeAddressButton.clicked.connect(self.saveReport)

        self.showInfoTextEdit = QTextEdit(u'【logging】测试环境连接成功……')
        self.showInfoTextEdit.append(u'【logging】请选择测试用例或者直接进行全局测试并选择用户数据(为保护账户隐私，请不要放到项目文件夹)及测试报告存放地址')
        self.showInfoTextEdit.append(u'【logging】请<下载数据样例>，并按照模板填写测试数据，填写完成后请<选择测试数据>，以所编辑的数据作为测试数据')

        self.okButton = QPushButton(u"确定")
        self.okButton.clicked.connect(self.start_to_test)
        self.cancelButton = QPushButton(u"取消")
        self.cancelButton.clicked.connect(self.quit_testTask)

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.okButton)
        buttonLayout.addWidget(self.cancelButton)
        layout = QGridLayout()
        layout.addWidget(self.ObjectLabel, 0, 1)


        layout.addWidget(self.FunctionLabel, 1, 0)
        layout.addWidget(self.FunctionsComboBox, 1, 1)

        layout.addWidget(self.UserDataFileLabel, 2, 0)
        layout.addWidget(self.UserDataFileAddress, 2, 1)
        layout.addWidget(self.UserDataFileDownload, 2, 2)
        layout.addWidget(self.UserDataFileChangeButton, 2, 3)

        layout.addWidget(self.SaveLabel, 3, 0)
        layout.addWidget(self.ReportAddressLabel, 3, 1)
        layout.addWidget(self.ChangeAddressButton, 3, 2)

        layout.addWidget(self.showInfoTextEdit, 4, 1)

        layout.addLayout(buttonLayout, 5, 2, 5, 3)
        self.setLayout(layout)
        # 窗口的标题
        self.setWindowTitle(u"爱贷网App测试用例")
        self.resize(640, 400)

    def openExplorer(self):
        print('open')

        dlg = QFileDialog(self)
        filename = dlg.getOpenFileName()[0]
        self.filename = filename
        self.UserDataFileAddress.setText(filename)
        self.showInfoTextEdit.append(u'【logging】使用(%s)文件作为测试数据' % filename)
        return filename

    def saveReport(self):
        print('save')

        #  获取报告保存的目录（弹窗选择）
        dlg = QFileDialog(self)
        filename = dlg.getSaveFileName(self, u'测试报告保存', 'AidaiwangReport.xlsx')
        self.ReportAddressLabel.setText(filename)
        self.showInfoTextEdit.append(u'【logging】测试报告保存至: %s' % filename)
        print(filename)

    def createDataExcle(self):

        #  获取数据保存的目录（弹窗选择）
        dlg = QFileDialog(self)
        fileName = dlg.getSaveFileName(self, u'测试数据保存目录', 'AidaiwangUserData.xlsx')

        filename = fileName[0]
        print(filename)
        #  复制样板表格到指定目录
        shutil.copy('./DataFile/UsersData.xlsx', filename)
        self.showInfoTextEdit.append(u'【logging】账户数据模板已存放至: %s' % filename)

    def start_to_test(self):

        testText = self.FunctionsComboBox.currentText()
        if testText == 'All_Of_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            All_OF_aidaiwang.test_all_of_aidaiwangApp(self.filename)
        elif testText == 'Log_In_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = Login_aidaiwangApp.start_to_login(self.filename)
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Register_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = Register_aidaiwangApp.start_to_register(self.filename)
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Buy_Object_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = BuyObject_from_aidaiwangApp.start_to_buyobject(self.filename)
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Change_Password_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = ChangePassword_from_aidaiwangApp.start_to_changepassword()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'RealName_Auth_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = RealName_Auth_from_aidaiwangApp.start_to_realnameauth()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Band_BankCard_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = Band_BankCard_from_aidaiwangApp.start_to_band_bankcard()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Recharge_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = Recharge_from_aidaiwangApp.start_to_recharge()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Deposit_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = Deposit_from_aidaiwangApp.start_to_deposit()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Change_BankCard_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = Change_BankCard_from_aidaiwangApp.start_to_changebankcard()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)
        elif testText == 'Log_Out_aidaiwang':
            self.showInfoTextEdit.append(u'【logging】开始测试-- %s ……' % testText)
            QApplication.processEvents()
            print(testText)
            resultCode = LogOut_aidiawangApp.start_to_logout()
            self.showInfoTextEdit.append(u'【logging】测试结束，结果：%s' % resultCode)

    def quit_testTask(self):
        self.cancelButton.connect(QCoreApplication.quit)

app = QApplication(sys.argv)
font = FontPropertiesDlg()
font.show()
app.exec_()
