import qrcode

def generate_qr_code(url, filename):
    """
    The function `generate_qr_code` generates a QR code image from a given URL and saves it to a
    specified filename.
    
    :param url: The `url` parameter is the URL or text that you want to encode into the QR code. It can
    be any valid URL or text string
    :param filename: The filename parameter is the name of the file where the generated QR code image
    will be saved. It should include the file extension, such as ".png" or ".jpg"
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)
    image.show(filename)
