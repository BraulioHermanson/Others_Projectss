# pip install qrcode
# pip install Pillow

# simples
import qrcode

imagem = qrcode.make("https://www.google.com/")
imagem.save("qrcode.png")

# com imagem
import qrcode 
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  # para poder adicionar uma imagem
qr.add_data("https://www.youtube.com/")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="logo.png",
)

imagem.save("qrcode_logo.png")

# Diversos qrcode

redes_sociais = {
    "Facebook": "https://www.facebook.com/empresa",
    "Instagram": "https://www.instagram.com/empresa",
    "YouTube": "https://www.youtube.com/@empresa",
    "TikTok": "https://www.tiktok.com/@empresa",
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="logo.png",
    )

    imagem.save(f"sociais_{rede_social}.png")