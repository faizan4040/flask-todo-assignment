# app/app.py
from flask import Flask, jsonify, request, render_template
from uuid import uuid4

app = Flask(__name__, static_folder='static', template_folder='templates')

# simple /api JSON route (will be updated in later steps)
@app.route('/api')
def api():
    data = {"message": "hello from api", "status": "ok"}
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
