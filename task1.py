from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total Production"

model += (2 * lemonade + 1 * fruit_juice <= 100), "Water Constraint"
model += (1 * lemonade <= 50), "Sugar Constraint"
model += (1 * lemonade <= 30), "Lemon Juice Constraint"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

model.solve()

print(f"Оптимальна кількість Лимонаду: {lemonade.varValue}")
print(f"Оптимальна кількість Фруктового соку: {fruit_juice.varValue}")
