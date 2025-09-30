from os.path import join, exists
import sys
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
        total_str = f"${total:.2f}"
        output = f"|{product:^15}|"
        if quantity != None:
            output += f"{quantity:15d}|"
        else:
            output += f"{' ':15}|"
        output += f"{total_str:>15}|"
        print(output)
        print(f"+{fill*15}+{fill*15}+{fill*15}+")

def create_invoice_file(invoice, file):
    filename = join("invoiceFiles",f"inv{file}")
    with open(filename,'w') as f:
        fill = '-'
        product_heading = "Product"
        quantity_heading = "Quantity"
        total_heading = "Total"

        f.write(f"+{fill*15}+{fill*15}+{fill*15}+\n")
        f.write(f"|{product_heading:<15}|{quantity_heading:<15}|{total_heading:<15}|\n")
        f.write(f"+{fill*15}+{fill*15}+{fill*15}+\n")
        for row in invoice:
            product = row["product"]
            quantity = row["quantity"]
            total = row["total"]
            total_str = f"${total:.2f}"
            output = f"|{product:^15}|"
            if quantity != None:
                output += f"{quantity:15d}|"
            else:
                output += f"{' ':15}|"
            output += f"{total_str:>15}|\n"
            f.write(output)
            f.write(f"+{fill*15}+{fill*15}+{fill*15}+\n")
    
    


def process_file(file):
    invoice = []
    total = 0.0
    filename = join("orderFiles",file)
    f = open(filename)
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
    if len(sys.argv) != 2:
        filename = "order.txt"
    else:
        filename = sys.argv[1]
    if not exists(join("orderFiles",filename)):
        print("File does not exist.")
        sys.exit(1)  # 1 indicates error
    invoice = process_file(filename)
    display_invoice(invoice)
    create_invoice_file(invoice, filename)