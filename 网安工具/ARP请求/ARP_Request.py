# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from scapy.layers.l2 import ARP, getmacbyip, Ether
from scapy.all import *

def button_push(
        val_eth_src_mac, val_eth_dst_mac,
        val_arp_src_mac, val_arp_dst_mac,
        val_src_ip, val_dst_ip,
        op, val_ifname):
    """
    ARP 报文发送
    构造数据包目标，
    告诉192.168.38.1这台主机网关地址为192.168.38.111所在的主机：
    :param EtherSRCMAC val_eth_src_mac: 源MAC地址
    :param EtherDSTMAC val_eth_dst_mac: 目标MAC地址
    :param hwsrc val_arp_src_mac: ARP 中的源MAC地址
    :param hwdst val_arp_dst_mac: ARP 目标MAC地址
    :param psrc val_src_ip: 源 IP
    :param pdst val_dst_ip: 目标 IP
    :param op: 操作码  1代表请求，为2代表回应
    :param val_ifname: 接口名
    :return:
    """
    print(val_eth_src_mac,
          val_eth_dst_mac,
          val_arp_src_mac,
          val_arp_dst_mac,
          val_src_ip,
          val_dst_ip,
          op, val_ifname)
    if op == 'request':
        op = 1
    else:
        op = 2

    # 构造ARP包
    result_raw = Ether(
        src=val_eth_src_mac,
        dst=val_eth_dst_mac) / \
                 ARP(
                     hwsrc=val_arp_src_mac,
                     hwdst=val_arp_dst_mac,
                     psrc=val_src_ip,
                     pdst=val_dst_ip,
                     op=op,
                 )
    # inter 请求间隔
    # iface 网络接口
    sendp(
        result_raw,
        inter=2,
        iface=val_ifname
    )


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.val_eth_src_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.val_eth_src_mac.setGeometry(QtCore.QRect(100, 30, 161, 21))
        self.val_eth_src_mac.setObjectName("val_eth_src_mac")
        self.eth_src_mac = QtWidgets.QLabel(self.centralwidget)
        self.eth_src_mac.setGeometry(QtCore.QRect(20, 30, 91, 20))
        self.eth_src_mac.setObjectName("eth_src_mac")
        self.eth_dst_mac = QtWidgets.QLabel(self.centralwidget)
        self.eth_dst_mac.setGeometry(QtCore.QRect(280, 30, 71, 16))
        self.eth_dst_mac.setObjectName("eth_dst_mac")
        self.val_eth_dst_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.val_eth_dst_mac.setGeometry(QtCore.QRect(360, 30, 151, 20))
        self.val_eth_dst_mac.setObjectName("val_eth_dst_mac")
        self.arp_src_mac = QtWidgets.QLabel(self.centralwidget)
        self.arp_src_mac.setGeometry(QtCore.QRect(20, 80, 91, 20))
        self.arp_src_mac.setObjectName("arp_src_mac")
        self.arp_dst_mac = QtWidgets.QLabel(self.centralwidget)
        self.arp_dst_mac.setGeometry(QtCore.QRect(280, 80, 71, 16))
        self.arp_dst_mac.setObjectName("arp_dst_mac")
        self.val_arp_src_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.val_arp_src_mac.setGeometry(QtCore.QRect(100, 80, 161, 21))
        self.val_arp_src_mac.setObjectName("val_arp_src_mac")
        self.val_arp_dst_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.val_arp_dst_mac.setGeometry(QtCore.QRect(360, 80, 151, 20))
        self.val_arp_dst_mac.setObjectName("val_arp_dst_mac")
        self.arp_ip = QtWidgets.QLabel(self.centralwidget)
        self.arp_ip.setGeometry(QtCore.QRect(40, 120, 51, 20))
        self.arp_ip.setObjectName("arp_ip")
        self.dst_ip = QtWidgets.QLabel(self.centralwidget)
        self.dst_ip.setGeometry(QtCore.QRect(310, 120, 51, 20))
        self.dst_ip.setObjectName("dst_ip")
        self.val_src_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.val_src_ip.setGeometry(QtCore.QRect(100, 120, 161, 21))
        self.val_src_ip.setObjectName("val_src_ip")
        self.val_dst_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.val_dst_ip.setGeometry(QtCore.QRect(360, 120, 151, 20))
        self.val_dst_ip.setObjectName("val_dst_ip")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 160, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("1")
        self.comboBox.addItem("0")
        self.op = QtWidgets.QLabel(self.centralwidget)
        self.op.setGeometry(QtCore.QRect(60, 160, 21, 20))
        self.op.setObjectName("op")
        self.ifname = QtWidgets.QLabel(self.centralwidget)
        self.ifname.setGeometry(QtCore.QRect(310, 160, 51, 20))
        self.ifname.setObjectName("ifname")
        self.val_ifname = QtWidgets.QLineEdit(self.centralwidget)
        self.val_ifname.setGeometry(QtCore.QRect(360, 160, 151, 20))
        self.val_ifname.setObjectName("val_ifname")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 210, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip("Run")
        self.pushButton.clicked.connect(self.addNum)

        # self.pushButton.clicked()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARP Request"))
        self.eth_src_mac.setText(_translate("MainWindow", "eth_src_MAC:"))
        self.eth_dst_mac.setText(_translate("MainWindow", "eth_dst_mac:"))
        self.arp_src_mac.setText(_translate("MainWindow", "arp_src_MAC:"))
        self.arp_dst_mac.setText(_translate("MainWindow", "arp_dst_mac:"))
        self.arp_ip.setText(_translate("MainWindow", "src_IP:"))
        self.dst_ip.setText(_translate("MainWindow", "dst_IP:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "request"))
        self.comboBox.setItemText(1, _translate("MainWindow", "reply"))
        self.op.setText(_translate("MainWindow", "op:"))
        self.ifname.setText(_translate("MainWindow", "ifname:"))
        self.pushButton.setText(_translate("MainWindow", "Send"))

    def addNum(self):
        print(self.val_eth_src_mac.text())
        print(self.val_arp_src_mac.text())
        print(self.val_src_ip.text())

        print(self.val_eth_dst_mac.text())
        print(self.val_arp_dst_mac.text())
        print(self.val_dst_ip.text())

        print(self.comboBox.currentText())
        print(self.val_ifname.text())





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
