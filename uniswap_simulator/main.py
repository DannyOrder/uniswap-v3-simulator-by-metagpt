from flask import Flask, request, render_template
from uniswap import UniswapV3
from calculator import Calculator

app = Flask(__name__)
uniswap = UniswapV3("address", "private_key")
calculator = Calculator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/pool_data', methods=['GET'])
def get_pool_data():
    pool_id = request.args.get('pool_id')
    pool_data = uniswap.get_pool_data(pool_id)
    return pool_data

@app.route('/api/v1/calculate_apy_roi', methods=['POST'])
def calculate_apy_roi():
    pool_data = request.json.get('pool_data')
    price_range = request.json.get('price_range')
    apy, roi = calculator.calculate_apy_roi(pool_data, price_range)
    return {'apy': apy, 'roi': roi}

if __name__ == '__main__':
    app.run(debug=True)
