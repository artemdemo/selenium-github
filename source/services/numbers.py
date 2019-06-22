import re


# Convert number to human readable format
# @source https://stackoverflow.com/a/45846841
#
def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


def human_format_to_num(_num_str):
    suffix = ['', 'K', 'M', 'B', 'T']
    regex = r"^([\d\.]+)([a-zA-Z]*)$"

    num_str = _num_str.strip().upper()
    matches = re.search(regex, num_str)
    if matches and len(matches.groups()) == 2:
        amount = float(matches.group(1))
        amount_suffix = matches.group(2)
        magnitude = suffix.index(amount_suffix)

        return amount * (1000 * magnitude)
    else:
        raise ValueError("Given number is not in the right format. Received: %s" % _num_str)

