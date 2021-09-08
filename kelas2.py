def calculator(req,a,b):
    if req=="etehad do jomleii":
        return a**2+b**2+2*a*b
    elif req=="etehad se jomleii":
        return a**3+b**3+3*a**2*b+3*a*b**2
    elif req=="etehad chahar jomleii":
        return a**2+b**2+c**2+2*a*b+2*a*c+2*b*c
    elif req=="etehad mozdavaj":
        return a**2-b**2
    elif req=="etehad chagho laghar":
        return a+b*a**2-a*b+b**2
