#before getting started please run:  pip intsall qr[pil] in the cmd/shell, otherwise you wont see the QR image

import qrcode
from web3 import Web3  # To interact with Ethereum blockchain using the web3.py library

# With Infura, we have instant access to the Ethereum network via the HTTP and WebSocket protocols.

infura_url = ("https://mainnet.infura.io/v3/8471a36e96334a3c918afd7107692b11")
w3 = Web3(Web3.HTTPProvider(infura_url))

address = input("Enter the Eth wallet address: \n")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#Now To generate QR code specific to Ethereum wallet address

is_address_valid = w3.isAddress(address)

if is_address_valid == True:

    qr.add_data(address)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#716b94", back_color="black")
    img.save("QReth.png")
    print("Grats your QReth created")

else:
    print("Enter *Only* Ethereum wallet address")
