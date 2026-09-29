sum = 0 
for i in range(1,1001):
	sum = i ** 100 + sum 

sum = str(sum)
let = ""
print(sum)
#sum = "1000"
n  = len(sum)
print(f'\033[32mNumber of digits {n}\033[0m')

for i in range(n,n % 3,-3):
    let =  "," +  sum[i-3:i]  + let 

let = sum[0:n % 3] + let

	
print(let)
for i in range(0,len(let)):
    print(f'\033[{5 + i % 2 }m{let[i]}\033[0m',end = "")
"""
for i in range(300,1600):
    print(f'\033[{i}m{i}\033[0m')
"""

#Ascii color codes
# 0 : default or reset
# 1 : Black
# 2 : grey 
# 3 : italic
# 4 : underlined
# 5 : blinking
# 6 : blinking
# 7 : backgorund white
# 8 : disappear
# 9 : strikethough
# 20: doubleunderline
# 30 - 37 : foreground color
# 40 - 47 : background color
#52 : underline
#90 - 97 : softer foreground color
#100 - 107: softer background color



    
