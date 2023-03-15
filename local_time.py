from datetime import datetime
import pytz


def get_time():
    # Create a timezone object for Minnesota (Central Time Zone)
    minnesota_tz = pytz.timezone('America/Chicago')
    # Get the current time in Minnesota
    minnesota_time = datetime.now(minnesota_tz)
    # Return the formatted time
    return minnesota_time.strftime("%H:%M %Z")


# # Call the get_time() function and print the returned value
# current_time = get_time()
# print("Current time in Minnesota:", current_time)
