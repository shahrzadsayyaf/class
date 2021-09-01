#shahrzad sayyafzade thursday 14-18
#tamrine 3
def calculator(width,height,shape,req):
	if shape=='mosalas' and req=='mohit':
		print(height*3)
	elif shape=='mosalas' and req=='masahat':
		print(width*height/2)
	elif shape=='moraba' and req=='mohit':
		print(width*4)
	elif shape=='moraba' and req=='masahat':
		print(width*width)
	elif shape=='mostatil' and req=='mohit':
		print(width+height)*2
	else:
         print(width*height)
calculator(10,20,'mosalas','mohit')
