# TODO-1: Ask the user for input
# bidder = input("What is your name?\n")
# bid_amount = int(input("What is your bid?\n"))

# TODO-2: Save data into dictionary {name: price}

# print(bid_details)
bid_details = {}
# bid_details[bidder] = bid_amount
# any_other_bidder = input("Are there any other bidders? type: yes or no\n").lower()

def auction():
    bidder = input("What is your name?\n")
    bid_amount = int(input("What is your bid?\n"))
    bid_details[bidder] = bid_amount
    any_other_bidder = input("Are there any other bidders? type: yes or no.\n").lower()



# TODO-3: Whether if new bids need to be added

while any_other_bidder == "yes":
    print("\n" * 30)
    auction()
    if any_other_bidder == "yes":
        print("\n" * 30)
        auction()
    elif any_other_bidder == "no":
        bid_details[bidder] = bid_amount
        print(bid_details)
    else:
        print("that wasn't part of the options, silly!")

# TODO-4: Compare bids in dictionary


