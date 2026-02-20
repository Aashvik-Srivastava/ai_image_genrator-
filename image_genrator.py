

import os
import requests
from PIL import Image
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
API_TOKEN = os.getenv(" cant put api token here due to rules voilation ")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image(prompt):
    print("Generating image..")

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code != 200:
        print("Error:", response.text)
        return

    img = Image.open(BytesIO(response.content))
    img.save("generated_image.png")
    img.show()
    print("The Image is saved as generated_image.png ")

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    generate_image(user_prompt)


