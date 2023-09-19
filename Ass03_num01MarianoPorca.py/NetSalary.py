# loan
# insurance

import SalaryDeductions as SalaryDeductions
import GrossSalary as GrossSalary

def NetSalary(ot, rate, hours, loan, insurance):
    netSalary = (((GrossSalary.GrossSalary(ot, rate, hours) - SalaryDeductions.SalaryDeductions(ot, rate, hours) ) - loan ) - insurance)
    return netSalary

def TotalDeduction(ot, rate, hours, loan, insurance):
    totalDeduction = (((SalaryDeductions.SalaryDeductions(ot, rate, hours) + loan) + insurance))
    return totalDeduction