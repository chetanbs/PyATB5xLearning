# Lambda | lambda arguments: expression
# A lambda is an anonymous function that returns some form of data
# Syntax: lambda parameters: expression
# parameters - Separated by commas and expression - An operation that returns something
# Syntax: The Syntax to create a lambda function is lambda arguments:epression. The lambda keyword
# is used to define the anonymous function, followed by a list of arguments, a colon, and an epression
# Arguments: Like a normal functio, a lambda function can accept any umber of arguments but must have
# only one expression. The arguments are specified before the colon.
# Expression: The expression is executed and the result is returned when the lambda function
# is called. This expression is written after the colon.



#def triple_me(num):
#    return num ** 3

#result = triple_me(2)
#print(result)


result_l = lambda num:num ** 3
print(result_l(2))

