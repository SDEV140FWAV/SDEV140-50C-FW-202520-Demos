import random

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

username = last_name.lower()[0:5:2] + first_name.lower()[0] + str(random.randint(10,10000))
print(username)
last_name[::3]

card_corner = "+"
card_horizontal = '-'
card_vertical = "|"
card_rank = "A"
card_space = ""
card_suit="♣"
print(f"{card_corner:-<6}{card_horizontal}{card_corner:->6}")
print(f"{card_vertical:2}{card_rank:9}{card_vertical:>2}")
print(f"{card_vertical:2}{card_space:9}{card_vertical:>2}")
print(f"{card_vertical:2}{card_suit:^9}{card_vertical:>2}")
print(f"{card_vertical:2}{card_space:9}{card_vertical:>2}")
print(f"{card_vertical:2}{card_rank:>9}{card_vertical:>2}")
print(f"{card_corner:-<6}{card_horizontal}{card_corner:->6}")


