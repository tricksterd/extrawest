
WAGER_TYPES = {
    'LOTTO_WAGER': 'Lucky Numbers',
    'WAGER': 'Sports',
    'LIVE_WAGER': 'Live Sports',
    'BETGAMES_WAGER': 'Betgames',
    'EVOLUTION_WAGER': 'Evolution Games',
    'EZUGI_WAGER': 'Ezugi Games',
    'PRAGMATIC_WAGER': 'Pragmatic Play Games'
}

PURCHASE_SETTINGS_ORDER = [
    'LOTTO_WAGER',
    'WAGER',
    'LIVE_WAGER',
    'BETGAMES_WAGER',
    'EVOLUTION_WAGER',
    'EZUGI_WAGER',
    'PRAGMATIC_WAGER'
]

purchase_settings = [
    {
        'wagerType': 'PRAGMATIC_WAGER',
        'minTotalOdds': '',
        'wageredPercent': '15',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'BETGAMES_WAGER',
        'minTotalOdds': '2',
        'wageredPercent': '100',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'LIVE_WAGER',
        'minTotalOdds': '3',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'LOTTO_WAGER',
        'minTotalOdds': '4',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'WAGER',
        'minTotalOdds': '',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
]

result = [
    'Lucky Numbers',
    'Sports',
    'Live Sports',
    'Betgames',
    'Pragmatic Play Games'
]


def get_data_from_json(json):
    temp_list = list()
    for i in purchase_settings:
        temp_list.append(i['wagerType'])
    return temp_list


def sorted_data(data):
    temp_list = list()
    for i in data:
        if i in PURCHASE_SETTINGS_ORDER:
            temp_list.append(PURCHASE_SETTINGS_ORDER.index(i))
    temp_list.sort()
    second_temp_list = list()
    for i in temp_list:
        second_temp_list.append(PURCHASE_SETTINGS_ORDER[i])
    return second_temp_list


def form_result(data):
    temp_list = list()
    for i in data:
        temp_list.append(WAGER_TYPES[i])
    return temp_list


def test_data():
    wager_list = get_data_from_json(purchase_settings)
    sort_data = sorted_data(wager_list)
    result_1 = form_result(sort_data)
    return result_1


