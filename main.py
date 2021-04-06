import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
from base64 import b64encode, b64decode

# import qrtools
# import qrdecode

# 1. TEXT to QR code IMAGE (qr1.png) and it's encoded version stored in QR code IMAGE (qr2.png)

text = 'hello world'
# text to QR code
img = qrcode.make(text)
img.save('qr1.png')
print('1. Created PNG Image with QR Code: ' + text + '.')

# base64 encode the data in file
with open('qr1.png', 'rb') as file1:
 data = file1.read()
 file1.close()

byte = bytes(data)
encoded = b64encode(byte)
print('2. Created PNG Image were encoded.')

# write encoded data with the QR code
img2 = qrcode.make(encoded)
img2.save('qr2.png')
print('3. Created other PNG Image with previous encoded data.')

# 2.A. QR code IMAGE (qr2.png) to decoding data and creating from it another QR code IMAGE (qr3.png)
# pyzbar, Pillow modules needed

print('4. Now vica versa.')

data = decode(Image.open('qr2.png'))
data1 = str(data[0][0]).replace("b'",'').replace("'","")
# type1 = str(data[0][1])
print('5. Reading PNG Image with QR Code - getting encoded data.')
print('Current data: ' + data1)

# base64 decode data and write to the file
decoded = b64decode(data1)
print('6. Encoded data are being decoded.')

with open('qr3.png', 'wb') as file2:
 file2.write(decoded)
 file2.close()
print('7. Created another PNG Image with previous decoded data.')

data = decode(Image.open('qr3.png'))
data1 = str(data[0][0]).replace("b'",'').replace("'","")
# type1 = str(data[0][1])
print('8. Reading PNG Image with QR Code - getting decoded data.')
print('Final data: ' + data1)

'''
# 2.B. QR code IMAGE (qr2.png) to decoding data and creating from it another QR code IMAGE (qr3.png)
# qrtools dependent on C lang
# PyPNG, ZBar and Pillow modules needed

# get qr1.png data from qr2.png
img3 = qrtools.QR()
img3.decode('qr2.png')

# base64 decode data and write to the file
decoded = b64decode(img3.data)

with open('qr3.png', 'wb') as file2:
 file2.write(decoded)
 file2.close()

img4 = qrtools.QR()
img4.decode('qr3.png')
print(img4.data)
'''

'''
# 2.C. QR code IMAGE (qr2.png) to decoding data and creating from it another QR code IMAGE (qr3.png)
# qrdecode - uses distance online tool for getting all the answers
# qrdecode author has specified additional modules for it to work

ans = qrdecode.is_correct_file_format('qr2.png', ['png','jpg'])
if (ans == True):
 res = qrdecode.decode('qr2.png')
 print(res)
 # base64 decode data and write to the file
 decoded = b64decode(res)

 with open('qr3.png', 'wb') as file2:
     file2.write(decoded)
     file2.close()

 res2 = qrdecode.decode('qr3.png')
 print(res2)
else:
 print('Wrong file format')
'''
