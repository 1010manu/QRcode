import qrcode
img=qrcode.make('https://www.youtube.com/')
img.save('QR.jpg')
