from flask import Flask, render_template, jsonify
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

app = Flask(__name__)

# Sample list of approved maintenance providers
providers = [
    {"name": "Provider A", "cost": random.randint(70, 150), "speed": random.randint(1, 5)},
    {"name": "Provider B", "cost": random.randint(70, 150), "speed": random.randint(1, 5)},
    {"name": "Provider C", "cost": random.randint(70, 150), "speed": random.randint(1, 5)},
    {"name": "Provider D", "cost": random.randint(70, 150), "speed": random.randint(1, 5)},
    {"name": "Provider E", "cost": random.randint(70, 150), "speed": random.randint(1, 5)},
]

class ContractNegotiator:
    def find_best_provider(self):
        best_provider = min(providers, key=lambda x: (x['cost'], x['speed']))
        return best_provider

    def negotiate(self, provider):
        responses = [
            f"EOGuard: What is the price for your services?",
            f"Contractor: The price is ${provider['cost']}.",
        ]

        # Randomly decide whether to negotiate for a lower price
        if random.choice([True, False]):
            lower_price = provider['cost'] - random.randint(5, 20)
            responses.append(f"EOGuard: Can you lower the price to ${lower_price}?")
            responses.append(f"Contractor: I can lower it to ${lower_price + random.randint(0, 10)}.")
        else:
            responses.append(f"EOGuard: That sounds good to me.");

        responses.append(f"EOGuard: Can you provide details about your services?")
        responses.append(f"Contractor: Provider Name: {provider['name']}, Cost: ${provider['cost']}, Speed: {provider['speed']} hours.")
        responses.append(f"EOGuard: Let's finalize the deal.")
        responses.append(f"Contractor: Deal finalized with {provider['name']} for ${provider['cost']}.")

        return responses

    def execute_contract(self, provider):
        return f"Contract executed with {provider['name']} for ${provider['cost']}."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_chat', methods=['POST'])
def start_chat():
    negotiator = ContractNegotiator()
    provider = negotiator.find_best_provider()
    responses = negotiator.negotiate(provider)

    # Simulate the conversation
    messages = []
    for response in responses:
        messages.append(response)
        time.sleep(2)  # Simulate delay for conversation

    contract_response = negotiator.execute_contract(provider)
    messages.append(contract_response)

    # Send confirmation email after the chat discussion
    send_email(provider, contract_response)

    return jsonify({'messages': messages})

def send_email(provider, contract_response):
    sender_email = "yashwanthalluri26@gmail.com"
    receiver_email = "yashalluri26@gmail.com"
    password = "vcez eamv kkfl gomu"

    subject = "Contract Confirmation"
    body = f"""
    Dear User,

    EOGuard has successfully executed a contract with {provider['name']} for ${provider['cost']}.
    Details:
    - Speed: {provider['speed']} hours
    - Status: {contract_response}

    Thank you!
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to send email: Authentication error. Check your email and password.")
    except smtplib.SMTPConnectError:
        print("Failed to send email: Unable to connect to the SMTP server.")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == '__main__':
    app.run(debug=True) 