#variables
variable_in_type_bool = "True"
boolean = type(bool(variable_in_type_bool))
int_variable = 5
int_variable_2 = 2
int_variable_3 = 1
int_variable_4 = 17
float_variable = float("15.5")
text_bool = "True"
text_first = "Hello"
text_2_variable = "Jiro jan"
text_3_variable = "here is"
text_4_variable = "my homework"
t_break = " "

#Operators that we have passed

operator_pl = "+"
operator_min = "-"
operator_div = "/"
operator_mult = "*"
operator_2div = "//"
operator_2mult = "**"
operator_equal = "="
operator_2equal = "=="

#functions that we have passed
function_print = "print()"
function_type = "type()"
function_str = "str()"
function_int = "int()"
function_float = "float()"

#other variables
result_0 = 5**2+2-5/1*5+(15.5//1)
result_2_div = result_0 == int_variable_4
result_1_div = 5**2+2-5/1*5+(15.5/1) == int_variable_4
result_of_actions_2_div = str(int_variable) + operator_2mult + str(int_variable_2) + operator_pl + str(int_variable_2) + operator_min + str(int_variable) + operator_div + str(int_variable_3) + operator_mult + str(int_variable) + operator_pl + "(" + str(float_variable) + operator_2div + str(int_variable_3) + ")" + operator_2equal + str(int_variable_4)
result_of_actions_div = str(int_variable) + operator_2mult + str(int_variable_2) + operator_pl + str(int_variable_2) + operator_min + str(int_variable) + operator_div + str(int_variable_3) + operator_mult + str(int_variable) + operator_pl + "(" + str(float_variable) + operator_2div + str(int_variable_3) + ")"
type_of_int_variable = type(int_variable)

print(text_first + t_break + text_2_variable + t_break + text_3_variable + t_break + text_4_variable) 
print("We have learned about operators and some functions of Python, bellow is an example, hope you'll enjoy it")

print(t_break + t_break + result_of_actions_2_div + t_break + t_break + "=>" + t_break + str(result_2_div)) 
print("  If we use / instead of //, the result would be :" + t_break + str(result_1_div) + " as " + result_of_actions_div + operator_equal + "17.5" + ",  a way to change the value is to change " + str(type(float_variable)) + " format with " + str(type_of_int_variable))
print("like : int(" + result_of_actions_div + ")") 









