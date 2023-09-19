name = input("Name: ")
rate = int(input("Rate: "))
hours = int(input("Number of Hours: "))
ot = int(input("Overtime Hours: "))
loan = int(input("Loan: "))
insurance = int(input("Health Insurance: "))

import OvertimePay as OvertimePay
import GrossSalary as GrossSalary
import SalaryDeductions as SalaryDeductions
import NetSalary as NetSalary

grossSalary = GrossSalary.GrossSalary(ot, rate, hours)
overtime = OvertimePay.OvertimePay(ot, rate)
salaryDeductions = SalaryDeductions.SalaryDeductions(ot, rate, hours)
totalDeduction = NetSalary.TotalDeduction(ot, rate, hours, loan, insurance)
netSalary = NetSalary.NetSalary(ot, rate, hours, loan, insurance)

print(f"\nName: {name}")
print(f"Rate: {rate}")
print(f"Number of Hours: {hours}")
print(f"Overtime Hours: {ot}")
print(f"Gross Salary: {grossSalary} \n")

print(f"Tax: {salaryDeductions}")
print(f"Loan: {loan}")
print(f"Insurance: {insurance} \n")

print(f"Total Deductions: {totalDeduction} \n")

print(f"Net Salary: {netSalary}")