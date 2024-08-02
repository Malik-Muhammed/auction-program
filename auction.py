import os

def clear_console():
    # Clear the console depending on the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        _ = os.system('clear')

print("Welcome to the secret auction program")

biddersDeterminant = True
biddersList = {}

while biddersDeterminant:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    biddersList[name] = bid

    anyOtherBidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    if anyOtherBidders == "yes":
        clear_console()
    elif anyOtherBidders == "no":
        biddersDeterminant = False

highestBid = 0
winner = ""
for bidder in biddersList:
    if biddersList[bidder] > highestBid:
        highestBid = biddersList[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of {highestBid}")
