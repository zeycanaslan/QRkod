import pyqrcode

url=input("qr kodun gideceği url yi yaz: ")

qr_code=pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=5)  #genişlik