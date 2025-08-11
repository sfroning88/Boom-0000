import os, sys
from flask import Flask, render_template, request, jsonify
from ngrok import connect

# create a Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

# get the Ngrok token
ngrok_token = os.environ.get('NGROK_API_TOKEN')

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

@app.route('/BUTTON_FUNCTION_THREE', methods=['POST'])
def BUTTON_FUNCTION_THREE():
    try:
        return jsonify({'success': True, 'message': 'Button Function Three success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/BUTTON_FUNCTION_FOUR', methods=['POST'])
def BUTTON_FUNCTION_FOUR():
    try:
        return jsonify({'success': True, 'message': 'Button Function Four success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/BUTTON_FUNCTION_FIVE', methods=['POST'])
def BUTTON_FUNCTION_FIVE():
    try:
        return jsonify({'success': True, 'message': 'Button Function Five success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/BUTTON_FUNCTION_SIX', methods=['POST'])
def BUTTON_FUNCTION_SIX():
    try:
        return jsonify({'success': True, 'message': 'Button Function Six success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/BUTTON_FUNCTION_SEVEN', methods=['POST'])
def BUTTON_FUNCTION_SEVEN():
    try:
        return jsonify({'success': True, 'message': 'Button Function Seven success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/BUTTON_FUNCTION_EIGHT', methods=['POST'])
def BUTTON_FUNCTION_EIGHT():
    try:
        return jsonify({'success': True, 'message': 'Button Function Eight success.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 app.py")
        sys.exit(1)

    # ngrok tunnel URL (will be set when tunnel is created)
    ngrok_url = None

    # Check if ngrok is available and create tunnel
    import importlib.util
    ngrok_spec = importlib.util.find_spec("ngrok")
    
    if ngrok_spec is None:
        print("ERROR: ngrok package not available")
        sys.exit(1)

    # Authenticate with ngrok using environment token
    if ngrok_token is None:
        print("ERROR: Please set your ngrok token")
        sys.exit(1)
    
    from ngrok import set_auth_token
    set_auth_token(ngrok_token)

    from ngrok import connect
    tunnel = connect(5000, domain="guiding-needlessly-mallard.ngrok-free.app")

    if tunnel is None:
        print("ERROR: Failed to connect to ngrok tunnel, check active instances")
        sys.exit(1)

    print("##############################_APP_BEGIN_##############################")

    # Static domain is configured in api/connect.py
    print(f"CHECKPOINT: Using static domain: https://guiding-needlessly-mallard.ngrok-free.app/oauth/callback")

    print("##############################_APP_END_##############################")

    # run the app
    app.run(port=5000)
