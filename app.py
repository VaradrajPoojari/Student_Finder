from model import final_function
from model import get_research_interests
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/response', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        text = get_research_interests(data['guid'])
        k = data['k']
        return jsonify(final_function(text,k)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)