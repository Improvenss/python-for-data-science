"""
Allowed functions : time, datetime or any other library that allows to
receive the date.
"""
"""
Expected output:
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
"""
import time as time
import datetime as datetime

current_time = float(0.0)
formatted_time = str("")
scientific_notation = str("")

# Get the current time in seconds since the epoch.
current_time = time.time() # 1734906840.6811311 -> second.milisecond
# Format current time with commas and 4 decimal places
formatted_time = f"{current_time:,.4f}"
# Format current time to scientific notation.
scientific_notation = f"{current_time:.2e}"
# Format the current date.
current_time = datetime.datetime.now().strftime("%b %d %Y")
# Print the formatted output
print(f"Seconds since January 1, 1970: {formatted_time} or \
{scientific_notation} in scientific notation")
print(current_time)