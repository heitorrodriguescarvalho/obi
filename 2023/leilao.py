bids = int(input())

current_winner = None
biggest_amount = 0

for _ in range(bids):
    name = input()
    amount = int(input())
    
    if amount > biggest_amount:
        current_winner = name
        biggest_amount = amount
        
print(current_winner)
print(biggest_amount)