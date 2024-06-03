import requests
import random
import time
import json


BASE_URL = 'https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults'

SUPER_LOTTO_URL_NUMBER = 8
DAILY_THREE_URL_NUMBER = 9
FANTASY_FIVE_URL_NUMBER = 10
DAILY_DERBY_URL_NUMBER = 11
POWERBALL_URL_NUMBER = 12
DAILY_FOUR_URL_NUMBER = 14
MEGAMILLIONS_URL_NUMBER = 15


def collectLottoDrawData(game):
    """Generate file with drawing data for specific lotto games
    """
    url = f"{BASE_URL}/{game}/{1}/20"
    response = requests.get(url).json()
    time.sleep(random.randint(0, 3))

    print(response)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)


collectLottoDrawData(MEGAMILLIONS_URL_NUMBER)

# for page in range(1, 19):
#     try:
#         r = requests.get(
#             f"https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/15/{page}/20").json()
#         print(f"{'*' * 20}Extracting Page# {page}{'*' * 21}")
#         for item in r['PreviousDraws']:
#             winning_numbers = item['WinningNumbers']
#             print("Date: {} Draw#: {} Win#: {:>2} {:>2} {:>2} {:>2} {:>2} Mega# {}".format(
#                 item['DrawDate'][0:10], item['DrawNumber'], * [winning_numbers[num]['Number'] for num in '01234'], winning_numbers['5']['Number']))
#         print('*' * 60)
#     except KeyboardInterrupt:
#         print("Good Bye!")
#         break

# TODO: build parser for Lotto results
# TODO: build some data samples to build seed
# TODO: finish the models for the dbs
# TODO: research how to use json type in relational db
