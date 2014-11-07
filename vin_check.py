
##check vin number for north-american market vehicles

letters = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
           'j':1, 'k':2, 'l':3, 'm':4, 'n':5, 'p':7, 'r':9,
           's':2, 't':3, 'u':4, 'v':5, 'w':6, 'x':7, 'y':8, 'z':9}

koef = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]

def vinIsValid(vin):
    if len(vin) != 17:
        print 'Length != 17'
        return 
    vin = vin.lower()
    ninth_symbol = vin[8]

    total = 0
    for i, letter in enumerate(vin):
        
        if letter in letters:
            total += koef[i]*letters[letter]
        else:
            total += koef[i]*int(letter)
            
    modulo = total%11
    result = str(modulo) == ninth_symbol \
                or (modulo == 10 and ninth_symbol == 'x')
    print str(total%11), " = ",  ninth_symbol, " = ", result


#vinIsValid('KNEJC524585810962')
#vinIsValid('JHMCM56557C404453')
vinIsValid('JTHCE96S770008889')

