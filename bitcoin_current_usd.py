import requests
"""url for api"""
coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    coins = get_bitcoin_number()
    value = determine_value_usd(coins)
    print(f'At the current rate the value of {coins} Bitcoins is {value:.2f}')


def get_json():
    """api call isolated for mocking ease"""
    response = requests.get(coindesk_url).json()
    return response


def get_exchange_rate(data):
    """drills down to current rate as a float"""
    rate = data['bpi']['USD']['rate_float']
    return rate


def get_bitcoin_number():
    """gets the number of coins to convert value to usd"""
    number_of_coins = input('How many bitcoins do you own? ')
    return float(number_of_coins)


def determine_value_usd(coins):
    """does the conversion"""
    data = get_json()
    rate = get_exchange_rate(data)
    value = coins * rate
    return value


if __name__ == '__main__':
    main()