import re
def validate_roman_numeral(num_str):
    thousand = "(?:(M){0,3})?"
    hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
    ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
    unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"
    regex_pattern = ("^{}{}{}{}$".format(thousand, hundred, ten, unit))	# Do not delete 'r'.
    return bool(re.match(regex_pattern, num_str))

if __name__ == "__main__":
    print(validate_roman_numeral("CDXXI"))