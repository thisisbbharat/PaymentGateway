from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Initialize Stripe with your API key
stripe.api_key = "pk_test_51OouD1SEeO14Os1OyYa7h9Y7BMh2Cbzp3YCgLOkKkygAGgk4N6LlduLCjB1cIq8ERQIUqWRmRn3F9nEyWMMQ9E0S00Xyk66yAO"

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
