'''
Product	Unit Price
A	17.46
B	10.13
C	2.11
D	23.13
E	74.56
F	1.11
G	9.34
H	3.45
'''

product_prices = {'A':17.46,'B':10.13,'C':2.11,'D':23.13,'E':74.56,'F':1.11,'G':9.34,'H':3.45}

def display_invoice(invoice):
    fill = '-'
    product_heading = "Product"
    quantity_heading = "Quantity"
    total_heading = "Total"

    print(f"+{fill*15}+{fill*15}+{fill*15}+")
    print(f"|{product_heading:<15}|{quantity_heading:<15}|{total_heading:<15}|")
    print(f"+{fill*15}+{fill*15}+{fill*15}+")
    for row in invoice:
        product = row["product"]
        quantity = row["quantity"]
        total = row["total"]
        output = f"|{product:^15}|{quantity:15d}|{total:15.2f}|"
        print(output)


def process_file():
    invoice = []
    total = 0.0
    f = open("order.txt")
    for line in f:
        token_list = line.split()
        product = token_list[0]
        quantity = int(token_list[1])
        line_total = quantity * product_prices[product]
        total += line_total
        line_dict = {"product":product, "quantity":quantity, "total":line_total}
        invoice.append(line_dict)
        print(product, quantity)
    invoice.append({"product":"Subtotal", "quantity":None, "total":total})
    tax = total * .17
    invoice.append({"product":"Tax", "quantity":None, "total":tax})
    invoice.append({"product":"Shipping", "quantity":None, "total":14.95})
    invoice.append({"product":"Grand Total", "quantity":None, "total":total + 14.95 + tax})
    f.close()
    return invoice
    

if __name__ == "__main__":
    invoice = process_file()
    display_invoice(invoice)