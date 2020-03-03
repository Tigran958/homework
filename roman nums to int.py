# class PySolution:
	
# 	def roman_to_int(self,s):
# 		roman_val = {"I":1, "V":5, "X":10, "L":50,
# 					 "C":100, "D":500, "M":1000}
# 		int_val = 0

# 		for i in range(len(s)):
# 			if i > 0 and roman_val[s[i]] > roman_val[s[i - 1]]:
# 				int_val += roman_val[s[i]] - 2 * roman_val[s[i - 1]]
# 			else:
# 				int_val += roman_val[s[i]]
# 		return int_val

# print(PySolution().roman_to_int("IX"))#9
# print(PySolution().roman_to_int("MDCL"))#1650
# print(PySolution().roman_to_int("MMMM"))#4000
		
class PyRoman:
	def roman_to_int1(self,rom):
		roman_v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

		value_rom = 0

		for i in range(len(rom)):
			if i > 0 and roman_v[rom[i - 1]] < roman_v[rom[i]]:
				value_rom += roman_v[rom[i]] - 2 * roman_v[rom[i - 1]]

			else:
				value_rom += roman_v[rom[i]]
		return value_rom

roman_func = PyRoman()
print(roman_func.roman_to_int1("IX"))