numbersToWord = {
        1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
        11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",
        20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",
    }

def convertNumToWord(n):
    n=str(n)
    if n=='':
        return "Please Enter Amount"
    for i in n:
        if(i.isalpha()):
            return "Not a Valid Amount!"

    if float(n)>999999.99 or float(n)<0:
        return "Only Amount Between 00 to 999999.99 Supported!"

    if float(n)==0:
        return "Rs. Zero ONLY"

    # splitting Whole and Decimal Number
    wholeNumber = str(int(n.split(".")[0])+1000000)
    wholeNumber = wholeNumber[1:]
    

    # Converting Int to Word
    wholeNumberToWord = ''
            
    def convertTwoDigit(number):
        word = ''
        if int(number[0])!=0:
            if int(number) in numbersToWord:
                word+=" "+numbersToWord[int(number)]
                return word
            key=int(number[0]+'0')
            word+=" "+numbersToWord[key]
        if int(number[1])!=0:
            word += " " + numbersToWord[int(number[1])]
        return word


    # to check if number in Lakh
    if(int(wholeNumber)>99999):
            wholeNumberToWord+=" "+numbersToWord[int(wholeNumber[0])]+" Lakh"
            wholeNumberToWord+=convertTwoDigit(wholeNumber[1:3])+" Thousand"
            if int(wholeNumber[3])!=0:
                wholeNumberToWord+=" "+numbersToWord[int(wholeNumber[3])]+" Hundred"

    elif(int(wholeNumber)>999):
            wholeNumberToWord+=convertTwoDigit(wholeNumber[1:3])+" Thousand"
            if int(wholeNumber[3])!=0:
                wholeNumberToWord+=" "+numbersToWord[int(wholeNumber[3])]+" Hundred"
    
    elif(int(wholeNumber)>99):
            if int(wholeNumber[3])!=0:
                wholeNumberToWord+=" "+numbersToWord[int(wholeNumber[3])]+" Hundred"
    wholeNumberToWord+=convertTwoDigit(wholeNumber[4:])

    # decimal Fraction conversion
    decimalFractionToWord = ''
    if len(n.split("."))==2:
        decimalFraction = n.split(".")[1][:2]
        if int(decimalFraction)!=0:
            decimalFractionToWord += " "+decimalFraction+"/100"
    
    NumberToWord = 'Rs.' + wholeNumberToWord + decimalFractionToWord + ' ONLY'
    return NumberToWord

