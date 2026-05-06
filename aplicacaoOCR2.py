from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Procure a imagem na mesma pasta do script
image_path = 'cartao.jpg'

# Aumentar contraste da imagem para corrigir 'ç':
import cv2
import numpy as np

image_path = r'C:\Users\AMD\Documents\UFG\PDI\APLICACAO\cartao.jpg'

# Abrir a imagem com OpenCV
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Aplicar limiarização adaptativa
image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Salvar imagem processada temporariamente
cv2.imwrite('processed_image.cartao.png', image)

# Aplicar OCR na imagem processada
text = pytesseract.image_to_string('processed_image.png', lang='por')
print(text)


# Ajustando o 'psm':
text = pytesseract.image_to_string(
    Image.open(image_path),
    lang='por',
    config='--psm 6 --oem 3'
)
print(text)


# Extração de texto da imagem:
try:
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Texto extraído da imagem:")
    print(text)
except FileNotFoundError:
    print(f"Erro: A imagem '{image_path}' não foi encontrada.")
except RuntimeError as e:
    print(f"Erro no processamento do Tesseract: {e}")

# Idiomas disponíveis no Tesseract:
available_languages = pytesseract.get_languages(config='')
print("\nIdiomas disponíveis no Tesseract:")
print(available_languages)

# Obtendo informações de bounding boxes:
try:
    boxes = pytesseract.image_to_boxes(Image.open(image_path))
    print("\nBounding boxes extraídos:")
    print(boxes)
except RuntimeError as e:
    print(f"Erro ao obter bounding boxes: {e}")

# Gerando PDF pesquisável apartir da imagem carregada
try:
    pdf = pytesseract.image_to_pdf_or_hocr(image_path, lang='por', extension='pdf')
    pdf_path = r'C:\Users\AMD\Documents\UFG\PDI\APLICACAO\cartao.pdf'
    with open(pdf_path, 'w+b') as f:
        f.write(pdf)
    print(f"\nPDF pesquisável gerado em: {pdf_path}")
except RuntimeError as e:
    print(f"Erro ao gerar o PDF: {e}")

text = pytesseract.image_to_string(
    Image.open(image_path),
    lang='por',
    config='--psm 6'
)

