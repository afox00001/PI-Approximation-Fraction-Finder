import decimal
from decimal import Decimal

decimal.setcontext(decimal.Context(prec=1000))

def calculate(minPresc):
    # Saving the first 759 digits of PI in a string for comparision. Why 759??? No particular reason, I just copied some arbitray number of digits from: https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt
    piDigits = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211"
    numerators = []
    denomenators = []
    numerator = 4
    while True:
        #I am deviding the numerator by Pi to the 19 digits to get a more accurate approximation for PI, to make the code faster, and not show us soultions like: PI ~ 3.1978 or whatever
        denomenator = numerator//3.1415926535897932384
        endingDenomenator = numerator//3.1415926535897932386

        for i in reversed(range(int(endingDenomenator), int(denomenator)+1)):
            if i <= 0:
                continue
            number = Decimal(numerator)/Decimal(i)
            precision = -1
            printNumber = ""
            z = 0
            for digit in str(number):
                if digit == piDigits[z]:
                    precision += 1
                    printNumber += digit
                else:
                    break
                z += 1
            if precision > minPresc:
                print(str(numerator) + " / " + str(i) + " Precision: " + str(precision) + " Digits ~ " + str(printNumber))
                yield {"numerator": numerator, "denomenator": i, "prescision": precision, "value": printNumber}
                numerators.append(numerator)
                denomenators.append(i)
        numerator += 1
for i in calculate(4):
    with open("PiFractions.txt", "a") as fractionsFile:
        fractionsFile.write(str(i["numerator"]) + " / " + str(i["denomenator"]) + " Precision: " + str(i["prescision"]) + " Digits ~ " + str(i["value"]) + "\n")
