import pulp
import matplotlib.pyplot as plt
import numpy as np
prob = pulp.LpProblem("practice1", sense=pulp.LpMinimize)

x = pulp.LpVariable("x", cat = "Continuous")
y = pulp.LpVariable("y", cat = "Continuous")

prob += x - y + 1 == 0
prob += 3 * x - y + 3 == 0

status = prob.solve()

print(f"演算結果:{pulp.LpStatus[status]}")
print(f"x={x.value()}")
print(f"y={y.value()}")


a = np.linspace(-5,5,20)
b = a + 1
plt.plot(a,b)
b = 3 * a + 3
plt.plot(a,b)
plt.show()







