# lambda_1 = lambda x, y=(lambda y, z: y ** z): x ** y
#
# print(lambda_1(3, y(3, 2))) y is not defined

lambda_1 = lambda x, y: x ** y
lambda_2 = lambda y, z: y ** z

print(lambda_1(3, lambda_2(3, 2)))
