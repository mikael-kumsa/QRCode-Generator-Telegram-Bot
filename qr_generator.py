import qrcode
import os

def generateQR(content, path):
    qr = qrcode.QRCode()
    qr.add_data(content)
    qr_img = qr.make_image(fill_color="blue", back_color="white")
    qr_name = path
    qr_img.save(qr_name)
    qr_path = os.path.abspath(qr_name)
    return qr_path
    
