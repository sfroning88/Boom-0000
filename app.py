import os, sys
from flask import Flask, render_template, jsonify

# create a Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

# set up Vapi secret key
vapi_token = os.environ.get('VAPI_API_KEY')

# set up Twilio secret key
twilio_token = os.environ.get('TWILIO_API_KEY')

# set up Twilio account number
twilio_account = os.environ.get('TWILIO_ACCOUNT_NUMBER')

# set up SendGrid secret key
sendgrid_token = os.environ.get('SENDGRID_API_KEY')

@app.route('/')
def home():
    return render_template('chat.html')

# function to generate outbound call
@app.route('/generate_outbound_call', methods=['POST'])
def generate_outbound_call():
    try:
        ############################################################
        # Hardcoded agent for testing
        from agents.savannah import agent

        # Hardcoded business phone number
        # business_phone = "d4437aa7-12b0-49ce-b612-6165578a35e1"
        # free vapi trial number: +1 (206) 231 6331

        # Hardcoded business phone number
        business_phone = "+18554581967"
        # free twilio trial number

        # Hardcoded business email address
        business_email = "seanf@thewealthboom.com"

        # Hardcoded customer phone number
        customer_phone = "+17737240301"

        # Hardcoded Calendly booking link
        booking_link = "https://calendly.com/seanf-boom/new-meeting"   
        ############################################################ 

        from api.payload import load_payload
        from api.vapi import outbound_call
        response = outbound_call(load_payload(agent, business_phone, customer_phone, twilio_token, twilio_account), vapi_token)
        #response = {'follow_up': True, 'preferred_contact': 'email', 'phone_contact': '+17737240301', 'email_contact': 'skdf2012@gmail.com'}
        print(f"\nResponse: \n{response}\n")
        
        # Check if follow_up is True and send message if needed
        if response.get("follow_up"):
            result = False
            preferred_contact = response.get("preferred_contact")
            
            if preferred_contact == "phone":
                from api.message import send_text
                sender = business_phone

                from functions.cleaning import clean_phone
                receiver = clean_phone(response.get("phone_contact"))
                
                print(f"\nSending text from {sender} to {receiver}.\n")
                result = send_text(booking_link, twilio_token, twilio_account, sender, receiver)
            
            elif preferred_contact == "email":
                from api.message import send_email
                sender = business_email

                from functions.cleaning import clean_email
                receiver = clean_email(response.get("email_contact"))

                print(f"\nSending email from {sender} to {receiver}.\n")
                result = send_email(booking_link, sendgrid_token, sender, receiver)
            
            if result:
                return jsonify({'success': True, 'message': f'Call initiated successfully. Follow up {preferred_contact} successful.'}), 200
                
            return jsonify({'success': True, 'message': f'Call initiated successfully. Follow-up {preferred_contact} unsuccessful.'}), 200
        
        return jsonify({'success': True, 'message': 'Call initiated successfully. No follow-up needed.'}), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 app.py")
        sys.exit(1)

    # run the app
    app.run()
