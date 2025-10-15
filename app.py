from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from local_rag import LocalKnowledgeBase

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

kb = LocalKnowledgeBase()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        files = request.files.getlist('files')
        if not files or all(file.filename == '' for file in files):
            return jsonify({'error': 'No files selected'}), 400
        
        file_paths = []
        for file in files:
            if file and file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                file_paths.append(file_path)
                print(f"✓ Saved file: {filename}")
        
        if not file_paths:
            return jsonify({'error': 'No valid files to upload'}), 400
            
        print(f"Processing {len(file_paths)} files...")
        kb.add_documents(file_paths)
        print("✓ Documents processed successfully")
        return jsonify({'message': 'Documents uploaded and indexed successfully.'})
    except Exception as e:
        print(f"✗ Upload error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get('query')
    if not question:
        return jsonify({'error': 'No query provided.'}), 400
    try:
        answer = kb.query(question)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
