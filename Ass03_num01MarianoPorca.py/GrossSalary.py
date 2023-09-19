# ot 
# rate
# hours

import OvertimePay as OvertimePay

def GrossSalary(ot, rate, hours):
    grossSalary = ((rate * hours) + OvertimePay.OvertimePay(ot, rate))
    return grossSalary