Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nodd, neven =0,1
>>> total=0
>>> while True:
	nodd= nodd + neven
	neven= nodd +neven
	if neven < 4000000:
		total += neven
	else:
	     break

	
>>> print(total)
5702886
>>> 
