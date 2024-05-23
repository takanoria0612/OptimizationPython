import pulp

prob = pulp.LpProblem("practice1", sense=pulp.LpMinimize)

x = pulp.LpVariable("x", cat = "Continuous")
y = pulp.LpVariable("y", cat = "Continuous")

prob += x - y + 1 == 0
prob += 3 * x - y + 3 == 0

status = prob.solve()

print(pulp.LpStatus[status])
print(x.value())
print(y.value())








