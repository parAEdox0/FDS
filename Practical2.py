# Write a Python program that computes the net amount of a bank account based
# a transaction log from console input. The transaction log format is shown as following: D
# 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
# withdraw and deposit) D means deposit while W means withdrawal.

net_amount = 0

while(True):

    transaction_str = input("Enter Transaction (D/W amount) : ")
    transaction = transaction_str.split(" ")

    if transaction[0].upper() in ('D' , 'W') and transaction[1].isdigit():

        input_str = transaction[0].upper()
        input_amount = int(transaction[1])

        if transaction[0] == 'D':
            net_amount += input_amount
        else:
            if input_amount > net_amount:
                print("ERROR! Value entered is greater than available balance")
            else:
                net_amount -= input_amount
        stop = input("Do You want to continue (Y/N): ")
        if stop == 'Y':
            continue
        elif stop == 'N':
            print(f"Net Amount = {net_amount}")
            exit(1)
        else:
            print("Entered wrong input")
            print(f"Net Amount = {net_amount}")
            exit(1)
    else:
        print("Entered wrong input please enter in format (D/W amoumt)")
