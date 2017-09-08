from numpy.linalg import inv
from numpy import dot, transpose

X = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
y = [[6], [9], [8]]

# result = dot(inv(dot(transpose(x), x)), dot(transpose(x), y))
# print(result)
#
# from numpy.linalg import lstsq
# print(lstsq(x, y)[0])

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
x2 = [[1, 3, 5]]
y2 = model.predict(x2)
print(y2)
