from unittest import TestCase
from unittest.mock import patch

import bitcoin_current_usd


class TestBitcoin(TestCase):
    """had issues with getting example response to work without a fully spoofed
    response from the API, will look into this further but wanted to get this
    test working so i could focus on project 4"""
    @patch('bitcoin_current_usd.get_json')
    def test_bitcoin_to_dollar(self, mock_rates):
        mock_rate = 1138.666
        example_api_response = {'time': {'updated': 'Mar 1, 2021 06:56:00 UTC',
                                         'updatedISO': '2021-03-01T06:56:00+00:00',
                                         'updateduk': 'Mar 1, 2021 at 06:56 GMT'},
                                'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). '
                                              'Non-USD currency data converted using hourly conversion rate from '
                                              'openexchangerates.org', 'chartName': 'Bitcoin',
                                'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '45,940.4947',
                                                'description': 'United States Dollar', 'rate_float': mock_rate},
                                        'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '32,853.8854',
                                                'description': 'British Pound Sterling', 'rate_float': 32853.8854},
                                        'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '38,014.7946',
                                                'description': 'Euro', 'rate_float': 38463.7442}}}

        mock_rates.side_effect = [example_api_response]
        converted = bitcoin_current_usd.determine_value_usd(10.0)
        self.assertEqual(11386.66, converted, mock_rate)
