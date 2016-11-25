import string
import re
import FinanceAPI.Config as Config

rename_dict = Config.futures_rename_dict


def get_product_list(str_date):
    # return product_list
    pass


def get_product_info_dict(str_date):
    pass


# instrument_id = ME1412
# product_id = MA
# product_code = ME
def get_product_code_by_instrument_id(instrument_id):
    if not is_futures_instrument(instrument_id):
        raise Exception('invalid input instrument_id')
    return __letter_part(instrument_id)


def get_product_id_by_product_code(product_code):
    if product_code in rename_dict:
        return rename_dict[product_code]
    else:
        return product_code


def get_delivery_month_by_instrument_id(instrument_id):
    if not is_futures_instrument(instrument_id):
        raise Exception('invalid input instrument_id')
    return __digit_part(instrument_id)


def latter_futures_instrument(instrument_id_1, instrument_id_2):
    if not is_futures_instrument(instrument_id_1) or not is_futures_instrument(instrument_id_2):
        raise Exception('invalid input instrument_id')
    digit1 = __digit_part(instrument_id_1)
    digit2 = __digit_part(instrument_id_2)
    if digit1[0] == '9':
        digit1 = '19' + digit1
    else:
        digit1 = '20' + digit1
    if digit2[0] == '9':
        digit2 = '19' + digit2
    else:
        digit2 = '20' + digit2

    if digit1 >= digit2:
        return instrument_id_1
    else:
        return instrument_id_2


def is_futures_instrument(instrument_id):
    pattern = '^[a-zA-Z]{1,2}[0-9]{3,4}$'
    res = re.match(pattern, instrument_id)
    if res:
        return True
    else:
        return False


def patch_zce_futures_instrument(instrument_id, date):
    if not is_futures_instrument(instrument_id):
        raise Exception('invalid input instrument_id')
    if instrument_id[-4].isdigit():
        return instrument_id
    else:
        patch_instrument = instrument_id[:-3] + date[2] + instrument_id[-3:]
        return patch_instrument


def __letter_part(in_str):
    pattern = string.ascii_letters
    rtn_str = ''
    for char in in_str:
        if char in pattern:
            rtn_str += char
    return rtn_str


def __digit_part(in_str):
    rtn_str = ''
    for char in in_str:
        if char.isdigit():
            rtn_str += char
    return rtn_str


if __name__ == "__main__":
    test1 = is_futures_instrument('TA509')
    test2 = is_futures_instrument('TA1509')
    test3 = is_futures_instrument('A1509')
    test4 = is_futures_instrument('A509')
    test5 = not is_futures_instrument('TA15091')
    if test1 and test2 and test3 and test4 and test5:
        print('is_futures_instrument test passed')
    test6 = latter_futures_instrument('if1601', 'if1602') == 'if1602'
    test7 = latter_futures_instrument('if9501', 'if1602') == 'if1602'
    test8 = latter_futures_instrument('if1602', 'if1601') == 'if1602'
    test9 = latter_futures_instrument('if1602', 'if9501') == 'if1602'
    if test6 and test7 and test8 and test9:
        print('latter_futures_instrument test passed')