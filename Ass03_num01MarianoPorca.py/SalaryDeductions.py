# rate
# hours

import GrossSalary as GrossSalary

def SalaryDeductions(ot, rate, hours):
    salaryDeductions = (GrossSalary.GrossSalary(ot, rate, hours) * .12)
    return salaryDeductions