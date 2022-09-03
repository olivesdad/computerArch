
# Some dictionaries to convert between base 10 and base 16 digits   
hexMap = {
            0:'0',
            1:'1',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9',
            10:'A',
            11:'B',
            12:'C',
            13:'D',
            14:'E',
            15:'F'
            }
intMap = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15
            }

#This is the int2hex function it takes a single integer argument and returns the hexadecimal value...
def int2hex(number):
    hex=''
    while number > 0:
        hex =  hexMap[number%16] + hex
        number = int(number / 16)
    return hex
    
# This  is the addHex function. it accepts 2 hexadecimal numbers in the form of a string and returns a hexadecimal value of their sums
# WARNING: no regex or input checking! will throw key error if not a valid hex value
def addHex(hex1, hex2):
    #need to know which string is longer
    if len(hex1) > len(hex2):
        maxLength = len(hex1.upper())
        topHex = list(hex1.upper())
        bottomHex = list (hex2)
    else:
        maxLength = len(hex2)
        topHex = list(hex2.upper())
        bottomHex = list(hex1.upper())

    #output hex should be one greater than longest
    hexOut = []
    
    #pad bottomHex
    while len(bottomHex) < len(topHex):
        bottomHex.insert(0,'0')
   
    #add elements do the carry stuff
    i = maxLength -1
    carry = 0
    while i >= 0:
        sum = intMap[topHex[i]] + intMap[bottomHex[i]] + carry
        hexOut.insert(0, hexMap[sum %16])
        if sum >= 16:
            carry = 1
        else :
            carry = 0
        i-=1
    if carry == 1:
        hexOut.insert(0,'1')
    # Moosh the hexout list into a string to return
    return ''.join(hexOut)



if __name__ == "__main__":
   print(int2hex(177))

   print(addHex('fff', 'fff'))

