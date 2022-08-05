import math
 

# math for the powerball lottery
# five_nums = math.comb(69, 5)
# powerball_num = math.comb(26, 1)
# full_powerball_winning = five_nums * powerball_num


# first_term = math.comb(5, 5)
# second_term = math.comb(64, 0)
# third_term = math.comb(1, 0)
# fourth_term = math.comb(25, 0)
# first_term_bot = math.comb(69, 5)
# second_term_bot = math.comb(26, 1)
# top_fraction = first_term * second_term * third_term * fourth_term
# bot_fraction = first_term_bot * second_term_bot
# total_fraction = math.ceil(bot_fraction/top_fraction)

# print(total_fraction, 'odds of winning powerball')

# first_term = math.comb(5, 5)
# second_term = math.comb(64, 0)
# third_term = math.comb(1, 0)
# fourth_term = math.comb(25, 1)
# first_term_bot = math.comb(69, 5)
# second_term_bot = math.comb(26, 1)
# top_fraction = first_term * second_term * third_term * fourth_term
# bot_fraction = first_term_bot * second_term_bot

# total_fraction = math.ceil(bot_fraction/top_fraction)
# print(total_fraction, 'odds of matching only five numbers and not the powerball number')



import requests
url = "https://www.calottery.com/draw-games/powerball#section-content-1-3"
r = requests.get(url)
print(r.status_code)

