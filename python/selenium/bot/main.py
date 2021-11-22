from booking.booking import Booking
from booking.input_handling import *


with Booking() as bot:
    bot.main_page()
    bot.deny_cookies()
    bot.change_currency(desired_currency=handle_currency())
    bot.select_destination(destination=handle_destination())
    bot.set_dates(handle_dates())
    bot.set_guests(handle_adults(), handle_rooms())
    bot.search_for_hotels()
    bot.filter_results()
    bot.refresh()  # This makes the bot wait for the sorting
    bot.report_results()
