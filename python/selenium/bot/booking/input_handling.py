from datetime import date, timedelta
import re


def handle_currency(currency_not_found=False):
    if currency_not_found:
        print('\nCurrency was not found! Try another abbreviation or currency.')
        user_input = str(input('> '))
    else:
        print('Which currency do you want to see? (e.g. EUR, USD)')
        user_input = str(input('> '))

    while len(user_input) != 3 or bool(re.search(r'\d', user_input)):
        print('\nGive currency in three letters!')
        user_input = str(input('> '))

    return user_input.upper()


def handle_destination(destination_not_found=False):
    if destination_not_found:
        print('\nDestination was not found! Maybe there was a typo. Try again.')
        user_input = str(input('> '))
    else:
        print('\nWhere do you want to go?')
        user_input = input('> ')

    return user_input


def handle_dates():
    question = 1
    check_in = None
    check_out = None
    first_question = True

    while question < 3:
        try:
            if first_question:
                if question == 1:
                    print('\nWhen do you want to check in? (e.g. 2022-02-02)')
                elif question == 2:
                    print('\nWhen do you want to check out?')

            if question == 1:
                check_in = date.fromisoformat(input('> '))
            elif question == 2:
                check_out = date.fromisoformat(input('> '))

            first_question = False

            if question == 1:
                if check_in < date.today():
                    print('\nYou can\'t book a hotel in the past! Try again.')
                elif check_in > date.today() + timedelta(days=460):
                    print('\nThis site can\'t book that far!')
                elif check_in is None:
                    raise ValueError('Check in date was accidentally none.')
                else:
                    first_question = True
                    question += 1
            elif question == 2:
                if check_out < date.today():
                    print('\nYou can\'t book a hotel in the past! Try again.')
                elif check_out < check_in:
                    print('\nYou can\'t check out before you\'ve checked in! Try again.')
                elif check_out > check_in + timedelta(days=45):
                    print('\nThis site cannot book a stay longer than 45 days!')
                elif check_out is None:
                    raise ValueError('Check out date was accidentally none.')
                else:
                    question += 1
        except ValueError:
            print('\nPlease give date in ISO format (YYYY-MM-DD)!')

    return check_in.isoformat(), check_out.isoformat()


def handle_adults():
    user_not_compliant = True

    print('\nHow many adults are staying?')

    while user_not_compliant:
        try:
            user_input = int(input('> '))

            if user_input > 30:
                print('\nThis site can\'t book more than 30 adults!')
            elif user_input < 1:
                print('\nDo you want to book a hotel or not? Try again.')
            else:
                user_not_compliant = False

                return user_input
        except ValueError:
            print('\nGive the amount of adults as a number!')


def handle_rooms():
    user_not_compliant = True

    print('\nHow many rooms do you want?')

    while user_not_compliant:
        try:
            user_input = int(input('> '))

            if user_input > 30:
                print('\nThis site can\'t book more than 30 rooms!')
            elif user_input < 1:
                print('\nYou want to book at least one room, right? Try again.')
            else:
                print('\nThanks! Results will be here shortly.')

                user_not_compliant = False

                return user_input
        except ValueError:
            print('\nGive the amount of rooms as a number!')
