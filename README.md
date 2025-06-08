🖼️ Background Remover Web App
A simple web app that allows users to upload an image and remove its background using a Python Flask API and the rembg package.

✨ Features
Upload any image (PNG, JPG, etc.)
Automatically removes the background
Shows the result instantly
Powered by rembg (AI background remover)
Built with Flask, HTML, CSS, JavaScript

🛠️ Technologies Used
Python 3
Flask
rembg
Pillow (PIL)
HTML + CSS + JavaScript

Install dependencies:
pip install -r requirements.txt

Run the Flask server:
python app.py

🧠 How It Works
The frontend (index.html) allows the user to upload an image.
On clicking "Remove Background", JavaScript sends the image to the Flask backend.
The backend uses rembg to remove the background and returns a new image.
The result is displayed in the browser.



