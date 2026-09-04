pn = input("Enter PAN number: ")

if len(pn) == 10:
    if (pn[:5].isalpha() and pn[:5].isupper() and
        pn[5:9].isdigit() and
        pn[9].isalpha() and pn[9].isupper()):
        
        print("PAN Number is Valid")
    else:
        print("PAN Number is Invalid")
else:
    print("PAN Number is Invalid")
