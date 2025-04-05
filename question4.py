

grand_total = 0
sales_data = []

num_salesmen = 10
for i in range(num_salesmen):
    print("\nEnter details for Salesman", i + 1)
    name = input("  Name: ")

    print("  Enter sales for 5 items:")
    item1 = int(input("    Item 1: "))
    item2 = int(input("    Item 2: "))
    item3 = int(input("    Item 3: "))
    item4 = int(input("    Item 4: "))
    item5 = int(input("    Item 5: "))

    total = item1 + item2 + item3 + item4 + item5
    grand_total += total

    # 
    sales_data.append([name, item1, item2, item3, item4, item5, total])

# Print results
print("\nSales Report:")
print("------------------------------------------------------------")
print("Name      Item1  Item2  Item3  Item4  Item5  Total")
print("------------------------------------------------------------")

for data in sales_data:
    print(data[0], "   ", data[1], "   ", data[2], "   ", data[3], "   ", data[4], "   ", data[5], "   ", data[6])
print("------------------------------------------------------------")
print("Grand Total:", grand_total)
