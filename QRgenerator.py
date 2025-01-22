import qrcode

img = qrcode.make('https://docs-python.ru/packages/generator-qr-kodov/')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")