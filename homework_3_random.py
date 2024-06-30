import random


def get_numbers_ticket(min, max, quantity):
    if (quantity < min or quantity > max) or not (1 <= min <= max <= 1000):
        return [] 

    lottery_numbers = set()

    while len(lottery_numbers) < quantity:
        random_number = random.randint(min, max)
        lottery_numbers.add(random_number)

    sorted_numbers = sorted(lottery_numbers)
    return sorted_numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

#