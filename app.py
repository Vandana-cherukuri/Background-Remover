from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    uploaded_file = request.files['image']
    input_bytes = uploaded_file.read()
    output_bytes = remove(input_bytes)
    output_image = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
    output_io = io.BytesIO()
    output_image.save(output_io, format='PNG')
    output_io.seek(0)
    return send_file(output_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

 