def calc_amount(principal,rate,duration):
    result = (principal + principal*rate)*duration
    return result

print(calc_amount(100,0.25,2))