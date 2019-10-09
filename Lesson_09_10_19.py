
time_input = input('Enter the time in 24-our format: 00:00:00 \n')
check_f = time_input.count(':')
check_len = len(time_input)
check_hours = int(time_input[0:2]) <= 24
check_minutes = int(time_input[3:5]) <= 60
check_seconds = int(time_input[6:8]) <= 60

while check_f != 2 or check_len != 8 or not check_hours or not check_minutes or not check_seconds:
	time_input = input('Enter the time in form 00:00:00 ')
	check_f = time_input.count(':')
	check_len = len(time_input)
	check_hours = int(time_input[0:2]) <= 24
	check_minutes = int(time_input[3:5]) <= 60
	check_seconds = int(time_input[6:8]) <= 60
	

def time_form_converter(time):
	new_time_12 = '12:00:00'
	if time == '00:00:00':
		return new_time_12 + ' AM'
			
	elif int(time[0:2]) <= 12:
		if time[0:2] == '12':
			return time	+ ' PM'	
		else:
			return time + ' AM'	
	else:
		hour_t = int(time[0:2]) - 12
		new_time = '0' + str(hour_t) + time[2:8]
		return new_time	+ ' PM'
print(time_form_converter(time_input))
