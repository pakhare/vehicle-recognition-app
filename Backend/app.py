import os
import base64
from flask import Flask, request, jsonify, send_file, redirect, flash
from image_processing import detect
from flask_cors import CORS

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

path = ''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		global path
	
		if 'image' not in request.files:
			return "Fail", 400
		file = request.files['image']
		
		if file.filename == '':
			return "No file", 400
		
		if not allowed_file(file.filename):
			return "Fail: Invalid file extension", 400

		
		path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
		file.save(path)
		return jsonify({'imageUrl': f'{path}'})
		
	if request.method == 'GET':
		procImage = detect(path)
		return jsonify({'processedUrl': f'{procImage}'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
