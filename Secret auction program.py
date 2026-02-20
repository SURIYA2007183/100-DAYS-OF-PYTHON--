
def find_highest_bid(bidding_dictionary):
    highest_bid=0
    winner=""
    for bidder in bidding_dictionary:
        bidding_amount=bidding_dictionary[bidder]
        if bidding_amount>highest_bid:
            highest_bid=bidding_amount
            winner=bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")        
    
        
      
 
bids={}
continue_bidding=True
while continue_bidding:
 name=input("what is your name?:")
 price=int(input("what's your bid amount? $ "))
 bids[name]=price
 should_continue=input("Are any other bidders there? type yes or no.\n ").lower()
 if should_continue =="no":
  continue_bidding=False
  find_highest_bid(bids)
 elif should_continue=="yes":
   print("\n"*20)








 