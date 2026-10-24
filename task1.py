
# ATM Transaction Sequence Simulation

balance = float(input("Enter initial account balance: "))
withdrawal_limit = float(input("Enter maximum withdrawal per transaction: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0
successful_transactions = 0
rejected_transactions = 0

for i in range(n):
    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdraw")

    choice = input("Enter your choice (1 or 2): ")
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        print("Invalid transaction amount!")
        rejected_transactions += 1

    elif choice == "1":
        balance += amount
        deposits += amount
        successful_transactions += 1
        print("Deposit successful.")

    elif choice == "2":
        if amount > withdrawal_limit:
            print("Transaction rejected: Withdrawal limit exceeded.")
            rejected_transactions += 1

        elif amount > balance:
            print("Transaction rejected: Insufficient balance.")
            rejected_transactions += 1

        else:
            balance -= amount
            withdrawals += amount
            successful_transactions += 1
            print("Withdrawal successful.")

    else:
        print("Invalid transaction type!")
        rejected_transactions += 1

    print("Current balance: Rs.", round(balance, 2))

# Transaction summary
print("\n===== ATM TRANSACTION SUMMARY =====")
print("Total deposits: Rs.", round(deposits, 2))
print("Total withdrawals: Rs.", round(withdrawals, 2))
print("Successful transactions:", successful_transactions)
print("Rejected transactions:", rejected_transactions)
print("Final account balance: Rs.", round(balance, 2))
