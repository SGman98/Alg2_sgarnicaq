def change_dp(amount):
    coins = [1, 3, 4] # Coins to use
    table = [float('inf')] * max(coins) # Create a table of size of maximum coin value
    table[-1] = 0

    for _ in range(1, amount + 1): # iterate over amount
        table.append(min(table[-coin] + 1 for coin in coins)) # iterate over coins and find the minimum and add 1 to it
        table.pop(0) # remove the first element to keep the size of the table
    return table[-1] # return the last element of the table it is the minimum number of coins needed to make the amount

def main():
    money = int(input())
    print(change_dp(money))

if __name__ == "__main__":
    main()
