import os
from art import logo


print(logo)
def clear_console():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        os.system('clear')



cont = True
bids={}


def highest_bidder(bids):
    winning_bid = 0
    winner = None
    for bidder, bid in bids.items():
        if bid > winning_bid:
            winning_bid=bid
            winner=bidder
    
    print(f"The winner is {winner} with a bid of ${winning_bid}")




    #take in the bidders name and auction 
    #add them to the di'ctionary
    #if there are other bidders, clear the console and go again
    #if not,  return the bidder and their highest bid


while cont:
    name= input("what is your name? ")
    bid = int(input("How much would you wish to bid? "))

    bids[name]=bid

    other_bidders=input("Are there any other bidders? (yes/no) ")

    if other_bidders.lower()=="yes":
        clear_console()
    elif other_bidders.lower()=="no":
        cont=False
        highest_bidder(bids)
