"""
* @author: Awwal Mohammed
* date: 12-11-21
* program title: test_utils.py

description:
\t A shadow of the utils.py file for testing purposes.
"""
import inspect
import logging
import math
from typing import Union


class MinSterlingUtils:

    def __init__(self):
        pass

    @staticmethod
    def get_coins(cur_val: Union[int, float], signal: str):
        """get_coins(cur_val, signal) -> [minimum coins, coins map]

        Return an array containing a string describing the minimum coins that represents cur_val,
        and a dictionary that indexes the number of coins produced.
        The signal parameter allows pound coins and pennies to be treated uniquely.

        :param cur_val: numeric monetary value corresponding with the user input,
            usually int or float, formatted by the calling program.
        :param signal: pound coin or pennies symbol, allows for specialized arithmetic.
        :return: a list containing a string (e.g.: "£1 x 1, 1 x 50p, 1 x 20p, 1 x 5p"),
            and a dictionary (e.g.: {'£1':1, '50p':1, '20p':1, '5p':1}), both describing the minimum coins.
        """

        cur_val = round(cur_val * 100, 2) if signal is '£' else cur_val

        two_pounds = cur_val / 200
        cur_val %= 200
        one_pound = cur_val / 100
        cur_val %= 100
        fifty_pennies = cur_val / 50
        cur_val %= 50
        twenty_pennies = cur_val / 20
        cur_val %= 20
        ten_pennies = cur_val / 10
        cur_val %= 10
        five_pennies = cur_val / 5
        cur_val %= 5
        two_pennies = cur_val / 2
        cur_val %= 2
        one_pennie = math.ceil(cur_val)

        coins = {"£2": int(two_pounds), "£1": int(one_pound),
                 "50p": int(fifty_pennies), "20p": int(twenty_pennies),
                 "10p": int(ten_pennies), "5p": int(five_pennies),
                 "2p": int(two_pennies), "1p": int(one_pennie)}

        result = str()
        for c in coins:
            if coins[c] != 0:
                result += str(coins[c]) + ' x ' + c + ', '
        result = result[:-1] if result.endswith(', ') or result.endswith(',') else result
        results = [result, coins]

        return results

    @staticmethod
    def validate_input(user_input):
        """Return boolean variables describing the validity of the user input.

        :param user_input: User input string immediately after it has been received.
        :return : a dictionary containing a series of boolean signals describing the validity of user_input.
        """

        is_pennies = is_pounds = is_pound_pence = is_sing_or_doub = \
            is_pound_decimal = is_missing_pence = is_sing_dig_pound = False

        is_pennies = True if \
            user_input.endswith('p') and '.' not in user_input and \
            '£' not in user_input and user_input.count('p') <= 1 else False
        is_pound_pence = True if \
            not is_pennies and user_input.endswith('p') and \
            user_input.count('p') == 1 and user_input.count('.') == 1 else False
        is_pound_decimal = True if \
            '.' in user_input and '£' not in user_input and 'p' not in user_input else False
        try:
            if '.' in user_input or '£' in user_input:
                float(user_input.replace('£', ''))
                is_pounds = True
        except Exception as e:
            logging.debug(e,
                          f": {__file__} > line {inspect.currentframe().f_lineno} > encountered while testing for pounds.")
            is_pounds = False
        try:
            int(user_input.replace('£', ''))
            is_sing_or_doub = True if not is_pennies and '£' not in user_input and not is_pounds else False
        except Exception as e:
            logging.debug(e,
                          f": {__file__} > line {inspect.currentframe().f_lineno} > encountered while testing for single/double.")
            is_sing_or_doub = False
        is_missing_pence = True if '£' in user_input and 'p' in user_input and '.' not in user_input else False
        if is_missing_pence:
            is_pennies = is_pounds = is_pound_pence = is_sing_or_doub = is_pound_decimal = False

        validations = {
            "is_pennies": is_pennies, "is_pounds": is_pounds, "is_pound_pence": is_pound_pence,
            "is_sing_or_doub": is_sing_or_doub, "is_pound_decimal": is_pound_decimal,
            "is_missing_pence": is_missing_pence, "is_sing_dig_pound": is_sing_dig_pound
        }

        return validations
