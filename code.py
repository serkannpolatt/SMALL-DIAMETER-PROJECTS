import qrcode

code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=4)

code.add_data("https://github.com/serkannpolatt")

code.make(fit=True)

image=code.make_image(fill_color=(8,153,206),back_color="black")

image.save("qrcode.png")
