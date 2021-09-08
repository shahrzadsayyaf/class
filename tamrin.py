#shahrzad sayyafzadeh thursday 14 ta 18
#bmi function
def bmi_info(mass,height):
	bmi=mass / (height**2)
	if bmi<16.5:
		return "you have lack of issues with mass"
	elif bmi >=16.5 and bmi<18.5:
		return"you still suffering from weight loss"
	elif 25<= bmi <30:
		return"you are fat "
	elif 30<= bmi <35:
		return"fat in categorical number1"
	elif bmi >=35 and bmi<40:
		return "you are fat in categorical number2"
	else:
		return "you are definityly too fat in categorical number3"
