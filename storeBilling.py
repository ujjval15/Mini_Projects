print("Welcome to My Cart")

#Create the Empty data structure
grocery_item={}
grocery_history=[]

#Variable used to check if the while loop condition is met 
stop = False

while not stop:
  name= input("Item name: ")
  Quantity= input("Quantity purchesed: ")
  cost= input("Price per Item: ")

  # create a dictionary entry which contain a name, quantity & cost
  grocery_item= {'item_name': name, 'quantity':int(Quantity), 'cost':float(cost)}

  grocery_history.append(grocery_item)

  response= input("Would you like to enter another item?\nType 'c' to continue 'q' to quit: ")

  if response == "q":
    stop= True

grand_total = 0

for item in grocery_history:
      
  #Calculate the total cost for the grocery item 
  item_total = item['quantity'] * item['cost']

  #Add the item total to the grand total
  grand_total += item_total

  print("%d %s @ ₹%.2f : ₹%.2f" %(item['quantity'], item['item_name'], item['cost'], item_total))

  item_total=0


print("\nGrand_total: ₹%.2f" % grand_total)