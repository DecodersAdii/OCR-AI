from PIL import Image
import pytesseract
import openai

# Set up Tesseract path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# OpenAI API Key
openai.api_key ="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"

# Load image and extract text
image_path = r'C:\Users\Aditya\Desktop\ocr 3\sample_image.png' # Replace with your image path
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)

# Use the extracted text as a query to ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": extracted_text},
    ]
)

# Print the response from ChatGPT
print("Extracted Text:\n", extracted_text)
print("\nChatGPT Response:\n", response['choices'][0]['message']['content'])
