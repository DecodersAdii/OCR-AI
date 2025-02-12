import requests



# Your API key
api_key = "d41f34e4922249fe8d1e0da290bcaea3"

# OCR Request
ocr_url = "https://api.aimlapi.com/vision/ocr"
image_path = r'C:\Users\Aditya\Desktop\ocr 3\sample_image.png'

try:
    # Open image file
    with open(image_path, 'rb') as img:
        ocr_response = requests.post(
            ocr_url,
            headers={"Authorization": f"Bearer {api_key}"},
            files={"image": img}
        )
    
    # Check OCR response status
    if ocr_response.status_code != 200:
        print(f"OCR API Error: {ocr_response.status_code} - {ocr_response.text}")
        exit()

    # Extract text
    ocr_result = ocr_response.json()
    extracted_text = ocr_result.get("text", "")
    print("Extracted Text:", extracted_text)

    if not extracted_text:
        print("No text found in the image.")
        exit()

    # AI Text Completion Request
    chat_url = "https://api.aimlapi.com/text/completion"
    chat_payload = {
        "prompt": extracted_text,
        "max_tokens": 100,
        "model": "gpt-4"
    }
    chat_response = requests.post(
        chat_url,
        headers={"Authorization": f"Bearer {api_key}"},
        json=chat_payload
    )

    # Check Chat API response status
    if chat_response.status_code != 200:
        print(f"Chat API Error: {chat_response.status_code} - {chat_response.text}")
        exit()

    # Output AI response
    chat_result = chat_response.json()
    ai_response = chat_result.get("choices", [{}])[0].get("text", "No response from AI.")
    print("AI Response:", ai_response)

except FileNotFoundError:
    print(f"Error: File not found at {image_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
