from flask import Flask, render_template, request
import os
from ml_model import predict  # Import the prediction function

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        # Save the file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Use the predict function
        result = predict(file_path)  # This calls the function in ml_model.py
        
        return f'File uploaded successfully. Prediction: {result}'
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
