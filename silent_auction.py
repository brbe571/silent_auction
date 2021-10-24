from replit import clear
from art import logo

print(logo)

bidders = {}
other_bidders = True


def highest_bid(bidding_records):
  winning_bid = 0
  winner = ""
  for bidder in bidding_records:
    bid_amount = int(bidding_records[bidder])
    if bid_amount > winning_bid:
      winning_bid = bid_amount
      winner = bidder
  print(f"{winner} is the winner with a bid of {winning_bid}")
    


while other_bidders == True:
  name = input("Please enter your name: ")
  bidder_price = input("Please enter your bid: $")
  bidders[name] = bidder_price
  new_bidder = input("Are there other users who want to bid, please type yes / no: ").lower()
  if new_bidder == 'no':
    other_bidders = False 
    highest_bid(bidders)
  else:
    clear()