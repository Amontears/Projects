from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Инициализируем Stripe с секретным ключом
stripe.api_key = "YOUR_SECRET_KEY"  # Замените на ваш секретный ключ Stripe

@app.route('/')
def index():
    return render_template('checkout.html', public_key="YOUR_PUBLIC_KEY")  # Замените на ваш публичный ключ Stripe

@app.route('/charge', methods=['POST'])
def charge():
    try:
        # Получаем данные из формы (например, токен Stripe)
        amount = 50000  # Установите сумму в центах, например 5000 = $50.00
        customer = stripe.Customer.create(
            email=request.form['stripeEmail'],
            source=request.form['stripeToken']
        )

        # Создаём платёж
        charge = stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='Оплата продукта'
        )

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
