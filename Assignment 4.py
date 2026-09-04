rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

X = []
Y = []

print("Enter elements of first matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input()))
    X.append(row)

print("Enter elements of second matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input()))
    Y.append(row)

Z = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(X[i][j] + Y[i][j])
    Z.append(row)

print("Addition of two matrices:")
for row in Z:
    print(row)
