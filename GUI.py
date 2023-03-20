import sys #Importing everything needed
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QDialog,
    QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

import qrcode
from PIL import Image
from web3 import Web3


class QRethApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def generateQRCode(self):
        address = self.addressEdit.text()
        w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/8471a36e96334a3c918afd7107692b11"))
        is_address_valid = w3.isAddress(address)

        if is_address_valid:
            # Generate QR code image
            logo_link = 'eth.png'
            logo = Image.open(logo_link)
            basewidth = 100
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(address)
            qr.make()
            
            img = qr.make_image(fill_color="#716b94", back_color="black") 
            position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            
            img.paste(logo, position)
            img.save("QReth.png")

            # Qreth text
            dialog = QDialog(self)
            dialog.setWindowTitle("QReth - Ethereum Wallet QR Code")
            dialog.setFixedSize(350, 350)
            
            vbox = QVBoxLayout()
            dialog.setLayout(vbox)

            # Add image label
            qr_pixmap = QPixmap("QReth.png")
            qr_label = QLabel()
            qr_label.setPixmap(qr_pixmap)
            vbox.addWidget(qr_label)
            qr_label.setScaledContents(True)

            # Display 
            dialog.exec_()

        else:
          self.qrCodeLabel.setText("Invalid Ethereum Wallet Address!")

    def initUI(self):
        self.setWindowTitle("QReth - Ethereum Wallet QR Code Generator")
        self.setGeometry(100, 100, 600, 500)
        self.setFixedSize(500, 400)
        
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        # QReth top left
        self.titleLabel = QLabel("QReth", self)
        self.titleLabel.setStyleSheet('color: #716b94; font-size: 20px; font-weight: bold')
        vbox.addWidget(self.titleLabel, 0, Qt.AlignTop|Qt.AlignLeft)

        # wallet addr input
        self.addressLabel = QLabel("", self)
        self.addressLabel.setText("Enter your Ethereum Wallet Address:")
        self.addressLabel.setStyleSheet('color: #716b94; font-size: 18px;')
        vbox.addWidget(self.addressLabel, 0, Qt.AlignTop|Qt.AlignHCenter)
        self.addressLabel.show()

        # 0x00000000.....
        self.addressEdit = QLineEdit(self)
        self.addressEdit.setMinimumWidth(200)
        self.addressEdit.setMaximumWidth(200)
        self.addressEdit.setStyleSheet('border-radius: 8px; padding: 10px; font-size: 15px;')
        vbox.addWidget(self.addressEdit,0, Qt.AlignTop|Qt.AlignHCenter)
        self.addressEdit.setPlaceholderText("Example, 0xF9e82768a7ED3f08b27EF11083B3BCF0A7E8A69e")
    
        # Button to generate qr
        self.generateQRCodeBtn = QPushButton("Generate QR Code", self)
        self.generateQRCodeBtn.setMinimumWidth(200)
        self.generateQRCodeBtn.setMaximumWidth(200)
        self.generateQRCodeBtn.setStyleSheet('background-color: #716b94; color: white; font-size: 18px; padding: 10px;')
        self.generateQRCodeBtn.clicked.connect(self.generateQRCode)
        vbox.addWidget(self.generateQRCodeBtn, 0, Qt.AlignTop|Qt.AlignHCenter)

        # QR Code label
        self.qrCodeLabel = QLabel(self)
        vbox.addWidget(self.qrCodeLabel, 0, Qt.AlignTop|Qt.AlignHCenter)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    qreth_app = QRethApp()
    sys.exit(app.exec_())


#0xF9e82768a7ED3f08b27EF11083B3BCF0A7E8A69e
