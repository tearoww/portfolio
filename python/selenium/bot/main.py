from booking.booking import Booking

print('Which currency do you want to see? (e.g. EUR, USD)')
currency = input('> ')

print('\nWhere do you want to go?')
destination = input('> ')

print('\nWhen do you want to check in? (e.g. 2022-05-06)')
check_in = input('> ')

print('\nWhen do you want to check out?')
check_out = input('> ')

print('\nHow many adults are staying?')
adults = input('> ')

print('\nHow many rooms do you want?')
rooms = input('> ')

print('\nThanks! Results will be here shortly.')

with Booking() as bot:
    bot.main_page()
    bot.deny_cookies()
    bot.change_currency(desired_currency=currency)
    bot.select_destination(destination=destination)
    bot.set_dates(check_in=check_in, check_out=check_out)
    bot.set_guests(adults, rooms)
    bot.search_for_hotels()
    bot.filter_results()
    bot.refresh()  # This makes the bot wait for the sorting
    bot.report_results()
