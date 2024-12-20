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
        amount = 5000  # Установите сумму в центах, например 5000 = $50.00
        customer = stripe.Customer.create(
            email=request.form['stripeEmail'],
            source=request.form['stripeToken']
        )

        # Создаём платёж
        charge = stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='Product payment'
        )

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
    @app.route('/refund', methods=['POST'])
    def refund():
        try:
            # Получаем идентификатор платежа из запроса
            charge_id = request.form['charge_id']
            
            # Создаём возврат
            refund = stripe.Refund.create(
                charge=charge_id
            )
            
            return jsonify({'status': 'success', 'refund': refund})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})