def romanToInt( s: str) -> int:
        romanNumerals = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            currentChar = s[i]
            if i < len(s) - 1:
                nextChar = s[i+1]
                if romanNumerals[currentChar] < romanNumerals[nextChar]:
                    num -= romanNumerals[currentChar]
                else:
                    num += romanNumerals[currentChar]
            else:
                num += romanNumerals[currentChar]
        return num

print (romanToInt('XV'))