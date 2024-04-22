import re
import long_responses as long

def get_response(user_input):
    split_message = re.split(r'\s+I[,;?!.-]\s*', user_input.lower)
    response = check_all_messages(split_message)
    return response

#testing response syste
while True:
    print('Bot ' + get_response(input('You:')))