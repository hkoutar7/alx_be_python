INTEREST = 0.05

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses:"))

mothly_savings = monthly_income - monthly_expenses

yearly_savings = int(mothly_savings * 12 * (1 + INTEREST))

print(f"Your monthly savings are ${mothly_savings}.")
print(f"Projected savings after one year, with interest, is: ${yearly_savings}.")