from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
@app.route('/healthz')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    # Start Hermes in background
    subprocess.Popen(['hermes', 'gateway', 'run'])
    # Start Flask server for Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
