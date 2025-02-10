from PIL import Image
import pytesseract

'


# Update the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = r'C:\Users\Aditya\Desktop\ocr 3\sample_image.png'  # Replace with your image path
image = Image.open(image_path)

# Perform OCR
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)
