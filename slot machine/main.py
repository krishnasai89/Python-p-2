def spin_row():
    pass
def print_row():
    pass
def get_payout():
    pass
def main():
    balance = 100

    print("*****************************")
    print("Welcome to python Slots")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*****************************")

    while balance >0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
if __name__ == '__main___':
    main()