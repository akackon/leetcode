def romanToInt(s: str) -> int:
        romanInt = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        converted = 0
        s = s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
        for symbol in s:
            converted += romanInt[symbol]
        return converted

print(romanToInt('LVIII'))