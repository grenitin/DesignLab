from flask import Flask, request, jsonify, render_template
import os
import subprocess
import pandas as pd
from urllib.parse import urlparse
import time

app = Flask(__name__)
AUDIT_FOLDER = 'UX Audit'

@app.route('/')
def index():
    audits = []
    if os.path.exists(AUDIT_FOLDER):
        for f in os.listdir(AUDIT_FOLDER):
            if f.endswith('.csv'):
                brand = f.split('_')[0]
                audits.append({'brand': brand, 'file': f})
                
    # Sort them alphabetically
    audits = sorted(audits, key=lambda d: d['brand'])
    return render_template('index.html', audits=audits)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    url = data.get('url')
    if not url: return jsonify({'error': 'URL is required'}), 400
    
    if not url.startswith('http'):
        url = 'https://' + url
        
    # Extract brand name
    parsed = urlparse(url)
    domain = parsed.netloc if parsed.netloc else parsed.path
    brand = domain.replace('www.', '').split('.')[0].capitalize()
    
    if not os.path.exists(AUDIT_FOLDER):
        os.makedirs(AUDIT_FOLDER)
        
    filename = f"{brand}_UX_Audit_-_Heuristic_Evaluation.csv"
    filepath = os.path.join(AUDIT_FOLDER, filename)
    
    # 1. Create a dummy evaluation for demonstration
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write("Index,Heuristic,Screenshot,Page URL,Page Name,Issue Description,Behavioral Insight,Attitudinal Insight,Cognitive Load,Severity,Priority,Recommendation\n")
            f.write(f'1,Visibility of System Status,,{url},Home Page,Mock evaluation generated for {brand} homepage during automation sequence.,Users are unable to see background loaders.,Feeling of uncertainty.,Medium,3,P2,Add prominent skeletal loaders.\n')
            
    # 2. Call sync_ux_audits.py to update only this specific sheet
    try:
        import sys
        subprocess.run([sys.executable, 'sync_ux_audits.py', filename], check=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
    return jsonify({'success': True, 'brand': brand})

@app.route('/view/<brand>')
def view(brand):
    # Find matching file
    filename = None
    if os.path.exists(AUDIT_FOLDER):
        for f in os.listdir(AUDIT_FOLDER):
            if f.startswith(brand) and f.endswith('.csv'):
                filename = f
                break
                
    if not filename:
        return "Audit not found", 404
        
    filepath = os.path.join(AUDIT_FOLDER, filename)
    df = pd.read_csv(filepath)
    df = df.fillna('')
    data = df.to_dict('records')
    
    return render_template('view.html', brand=brand, data=data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
