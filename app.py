import os, sys
from flask import Flask, render_template, request, jsonify

# create a Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return render_template('chat.html')

# generic button function
@app.route('/BUTTON_FUNCTION_ONE', methods=['POST'])
def BUTTON_FUNCTION_ONE():
    try:
        return jsonify({'success': True, 'message': 'Button Function One success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

# generic button function
@app.route('/BUTTON_FUNCTION_TWO', methods=['POST'])
def BUTTON_FUNCTION_TWO():
    try:
        return jsonify({'success': True, 'message': 'Button Function Two success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 app.py")
        sys.exit(1)

    # run the app
    app.run(debug=True)
