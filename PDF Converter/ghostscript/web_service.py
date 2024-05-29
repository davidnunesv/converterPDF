from flask import Flask, request, send_file
import subprocess
import requests  
app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_to_txt():
    pdf_file = request.files['file']
    output_file = f"/data/{pdf_file.filename}.txt"
    pdf_file.save("/data/input.pdf")
    
    subprocess.run(['pdftotext', '/data/input.pdf', output_file])
    
    # Registrar no serviço de log
    log_data = {"operation": "convert_to_txt", "file": pdf_file.filename}
    requests.post('http://log_service:8083/log', json=log_data, headers={"Authorization": "token-david-kaue-moises-vitor"})
    
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
