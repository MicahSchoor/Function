def main():
    billFirstName=raw_input("Billing Address First Name:")
    billLastName=raw_input("Billing Address Last Name:")
    shipFirstName=raw_input("Ship First Name:")
    shipLastName=raw_input("Ship Last Name:")
    billNameOnCard=raw_input("Bill Name on Card:")
    print countUniqueNames(billFirstName.lower(),billLastName.lower(),shipFirstName.lower(),shipLastName.lower(),billNameOnCard.lower())
def countUniqueNames(billFirstName,billLastName,shipFirstName,shipLastName,billNameOnCard):
    if " " in billFirstName:
        billFirstName=billFirstName.split(" ")[0]
    else:
        pass
    if " " in shipFirstName:
        shipFirstName=shipFirstName.split(" ")[0]
    else:
        pass
    if checkFirstName(shipFirstName,billFirstName) and checkLastName(shipLastName,billLastName):
        if checkFullName(billNameOnCard,billFirstName,billLastName):
            return 1
        else:
            return 2
    else:
        if checkFullName(billNameOnCard,billFirstName,billLastName):
            return 2
        else:
            if checkFullName(billNameOnCard,shipFirstName,shipLastName):
                return 2
            else:
                return 3
def checkFirstName(name1,name2):
    if name1 in name2 or compareFirstName(name1,name2) or name2 in name1:
        return 1
    else:
        if ("k" or "c" )in (name1 or name2) :##odds are most likley that c or k arent in persons name
            if "k" in name1:
                name1Rep=name1.replace("k","c")
            if "c" in name1:
                name1Rep=name1.replace("c","k")
            if name1Rep in name2 or compareFirstName(name1Rep,name2) or name2 in name1Rep:
                return 1
            if "k" in name1:
                name2Rep=name2.replace("k","c")
            if "c" in name1:
                name2Rep=name2.replace("c","k")
            if name1 in name2Rep or compareFirstName(name1,name2Rep) or name2Rep in name1:
                return 1
            if name1Rep in name2Rep or compareFirstName(name1Rep,name2Rep) or name2Rep in name1Rep:
                return 1
        return 0
def checkFullName(fullName1,name2,last2):
    fullName1=fullName1.split(" ")
    name1=fullName1[0]
    last1=fullName1[-1]##in case of middle name
    if checkFirstName(name1,name2) and checkLastName(last1,last2) or checkFirstName(last1,name2) and checkLastName(name1,last2):##in case of first name and last name switched
        return 1
    else:
        return 0
def checkLastName(last1,last2):
    if last1 in last2 or spellcheck(last1,last2):
        return 1
    else:
        return 0
def compareFirstName(name1,name2):
    counter=0
    name2Temp=name2
    for letter in list(name1):
        if letter in name2Temp:
            name2Temp=name2Temp[name2Temp.index(letter):]
            counter=counter+1
            if counter is 3:#three is the amount of simular letters in a row from the example given
                return 1

        else:
            counter=0##needs three in a row

    return 0
def spellcheck(name1,name2):
    counter=0
    name2Temp=name2
    for letter in list(name1):
        if letter in name2Temp:
            name2Temp=name2Temp[name2Temp.index(letter):]
            counter=counter+1
    return not (len(name1)-counter-1)

main()
