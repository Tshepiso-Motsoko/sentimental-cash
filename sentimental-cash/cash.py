def main():
    # Prompt user for amount of change owed
    while True:
        change = input("Change owed: ")
        try:
            change = float(change)
            if change >= 0:
                break
        except ValueError:
            pass

    # Convert change to cents
    cents = round(change * 100)

    # Initialize coin counter
    coins = 0

    # Use quarters
    coins += cents // 25
    cents %= 25

    # Use dimes
    coins += cents // 10
    cents %= 10

    # Use nickels
    coins += cents // 5
    cents %= 5

    # Use pennies
    coins += cents

    print(coins)

if __name__ == "__main__":
    main()
