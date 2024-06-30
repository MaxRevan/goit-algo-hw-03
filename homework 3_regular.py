import re


def normalize_phone(phone_number: str) -> list:

    format_phone = re.sub(r'\D', '', phone_number)
    if format_phone.startswith('380'):
        normalized_number = '+' + format_phone
    else:
        normalized_number = '+38' + format_phone
    return normalized_number


numbers_phone = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]
    
for phone_number in numbers_phone:
    normalized_number = normalize_phone(phone_number)
    
    print(normalized_number)

#

    