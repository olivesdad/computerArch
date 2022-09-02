
def main(number):
    hex=''
    hexMap = {
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

    while number > 0:
        hex =  hexMap[number%16] + hex
        number = int(number / 16)
    return hex
    

if __name__ == "__main__":
    print(main(450))

