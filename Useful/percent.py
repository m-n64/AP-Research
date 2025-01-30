def percent(num: float, den: float, dec: int = None):
    value = 100 * (num/den)

    if type(dec) == int:
        value = round(value, dec)
    
    return value

    