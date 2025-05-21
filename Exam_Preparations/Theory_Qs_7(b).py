def calculate_total(prices,discount,tax):
    tot=sum(prices)
    dis=(tot*discount)/100
    tx=(tot*tax)/100
    return tot-dis+tx
prices=[100,200,300]
discount=10
tax=5
total=calculate_total(prices,discount,tax)
print(f"Total amount after discount and tax is: {total}")