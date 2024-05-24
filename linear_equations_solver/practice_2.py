import pulp
# モデル作成
prob = pulp.LpProblem("practice2",sense = pulp.LpMaximize)

# 変数定義
x = pulp.LpVariable("x", lowBound=0, cat="continuous")
y = pulp.LpVariable("y", lowBound=0, cat="continuous")

#目的関数
prob += 100 * x + 150 * y

# 制約条件
prob += x + 2 * y <= 6
prob += 2 * x + y <= 9 

#　ソルバーの実行

status = prob.solve()
print(f"{pulp.LpStatus[status]}")
print(f"x={x.value()}")
print(f"y={y.value()}")