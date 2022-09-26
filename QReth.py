import qrcode
from PIL import Image
from web3 import Web3  # To interact with Ethereum blockchain using the web3.py library

# With Infura, we have instant access to the Ethereum network via the HTTP and WebSocket protocols.

infura_url = ("https://mainnet.infura.io/v3/8471a36e96334a3c918afd7107692b11")
w3 = Web3(Web3.HTTPProvider(infura_url))


# Add Logo In the Center
Logo_link = 'eth.png'
logo = Image.open(Logo_link)
basewidth = 100
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

address = input("Enter the Eth wallet address: \n")

#Now To generate QR code specific to Ethereum wallet address

is_address_valid = w3.isAddress(address)

if is_address_valid == True:

  qr.add_data(address)
  qr.make()
  img = qr.make_image(fill_color="#716b94", back_color="black") 

  position = ((img.size[0] - logo.size[0]) // 2,
         (img.size[1] - logo.size[1]) // 2)
  img.paste(logo, position)

  img.save("QReth.png")


  print("Grats your QReth is created")

else:
 print("Enter *Only* Ethereum wallet address! Ex: 0xF9e82768a7ED3f08b27EF11083B3BCF0A7E8A69e")

