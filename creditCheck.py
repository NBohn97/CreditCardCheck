
# main function
def main():
    checker()


# check validity and credit institution
def checker():
    c = 1
    z = 0
    o = 0
    b = 0
    reversedlist = []
    normallist = []
    joinedreverse = ""
    sumreverse = 0
    sumnormal = 0
    check = 0

    creditnum = input("Enter Credit Card number: ")





    creditnum = creditnum.strip()
    creditreverse = creditnum[::-1]

    # this turns credit num into a list with integers
    for i in creditreverse:
        try:
            reversedlist.append(int(creditreverse[c]) * 2)
            # print(creditreverse[c])
            c = c + 2
        except IndexError:
            break

    # turns the reversedlist which consists of integers back to a string so that you can extract the single digits
    # for sumreverse
    reversedlist = list(map(str, reversedlist))
    joinedreverse = joinedreverse.join(reversedlist)

    for k in joinedreverse:
        sumreverse = sumreverse + int(joinedreverse[o])
        o = o + 1

    # here begins the process for non reversed normal credit num

    for p in creditreverse:
        try:
            normallist.append(int(creditreverse[z]))
            # print(creditreverse[c])
            z = z + 2
        except IndexError:
            break

    for nums in normallist:
        sumnormal = sumnormal + normallist[b]
        b = b + 1

    # checking validity now
    check = sumnormal + sumreverse
    check = str(check)

    # just for testing sums
    print(sumnormal)
    print(sumreverse)

    if check[1] == "0" and creditnum[0] == "3":
        print("AMEX")
    elif check[1] == "0" and creditnum[0] == "5":
        print("MASTERCARD")
    elif check[1] == "0" and creditnum[0] == "4":
        print("VISA")
    else:
        print("INVALID")


main()
