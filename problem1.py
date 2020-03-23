
 nodd, neven =0,1
 total=0
 while True:
	nodd= nodd + neven
	neven= nodd +neven
	if neven < 4000000:
		total += neven
	else:
	     break
