from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Initialize Stripe with your API key
stripe.api_key = "YOUR_STRIPE_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charge', methods=['POST'])
def charge():
    amount = int(request.form['amount']) * 100  # Convert amount to cents
    try:
        # Create a Stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            description='Payment for services'
        )
        return jsonify(client_secret=intent.client_secret)
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(debug=True)
