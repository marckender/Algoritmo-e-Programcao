def vocal(txt):
	txt=txt.upper()
	if (txt=='a' or txt =='e' or txt =='i' or txt== 'u' or txt== 'o'):
		return 1
	else:
		return 0

print(vocal(input("Digite algo: "))) 

