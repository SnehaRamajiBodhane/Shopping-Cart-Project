"""
ProjectName:Shopping Cart project Using List and Dictionaries and Exception Handling.
Developer:Sneha
Date:2023-12-28
Description:: In this project we are Capturing the Activities of the Products like Add To Cart,View Cart,Edit Cart etc.
          1.Creating User 
          2.Login into the app
          3.Create Products
          4.Add To Cart
          5.View Cart
          6.Edit Cart 
          7.No of visitors to the product
          8.Clear Cart
          9.Apply Discount
          10.Generate the Bill
          11.Purchased date of the product
          12.Return The Product
          13.Exchange The Product
          14.Delivery
          15.Exit The Shopping Cart
"""

global products
products=[]
def shopping_cart_display_menu():
    print("="*50)
    print("\tShopping-Cart ")
    print("="*50)
    print("1.Create user")
    print("2.login  into the app ")
    print("3.Create Products")
    print("4.Add to cart")
    print("5.View cart")
    print("6.Edit cart")
    print("7.No of visitors to the product")
    print("8.Remove cart")
    print("9.Clear cart")
    print("10.Apply Discount")
    print("11.Get the Bill ")
    print("12.Return The Product ")
    print("13.Exchange The Product")
    print("14.Delivery")
    print("15.Exit from the Application")
    print("="*50)
def create_user():
    login_app(users)
    full_name=input("Enter your full name:")
    email_id=input("Enter your email id:")
    contact_no=int(input("Enter your contact"))
    address=input("Enter your address:")
    print("Your all details submitted!")
def login_app(users):
    username=input("Please enter a username:")
    password=input("Please enter a password:")

    for u in users:
        if username == u[0]:
            if password == u[1]:
                return username
            
    print("Username or password is incorrect. Please try again!")

users =[["sneha",'abc123'],["gaurav",'xyz123'],["samu",'pqr123'],["ram","abc123"]]
username = login_app(users)
print(username,"has logged in")
def create_product():
    print("Store the Products like below:")
    products={
            "Product1": { 
                          "Quantity":"1",
                          "Discount":"5%",
                          "Total":"664",
                          "Total Discount":"44",
                          "Total Price":"664",
                          "Product code":"P1",
                          "ProdName":"SriSri Ghee",
                          "Category":"Ghee",
                          "Brand":"Srisri",                           
                          "ExpTime":"11:30",
                          "ExPlace":"Mumbai",
                          "ExpDate": "28-Dec-2023",
                          "Qty": "Good"
            },
           "Product2": { 
                        "Quantity":"1",
                        "ProdName":"Running shoes",
                        "Price":"564",
                        "Discount":"5%",
                        "Total":"564",
                        "Total Discount":"44",
                        "Total Price":"564",
                        "Product code":"P1",
                        "Category":"Shoes",
                        "Brand":"Nike",
                        "PruchaseDate":"20-Dec-2023",
                        "ExpTime":"11:30",
                        "ExPlace":"Pune",
                        "ExpDate": "22-Dec-2023",
                        "Qty": "Good"
            },
           "Product3": { 
                        "Quantity":"1",
                        "ProdName":"Water Bottle",
                        "Price":"21",
                        "Discount":"3%",
                        "Total":"21",
                        "Total Discount":"44",
                        "Total Price":"21",
                        "Product code":"P3",
                        "Category":"Water Bottle",
                        "Brand":"Milton",
                        "PruchaseDate":"10-Dec-2023",
                        "ExpTime":"12:30",
                        "ExPlace":"Nagpur",
                        "ExpDate": "12-Dec-2023",
                        "Qty": "Good"

           },
           "Product4": { 
                        "Quantity":"1",
                        "ProdName":"Smart watch",
                        "Price":"1564",
                        "Discount":"5%",
                        "Total":"1564",
                        "Total Discount":"44",
                        "Total Price":"1564",
                        "Product code":"P4",
                        "Category":"watch",
                        "Brand":"sony",
                        "PruchaseDate":"10-Nov-2023",
                        "ExpTime":"1:30",
                        "ExPlace":"Kalmeshwar",
                        "ExpDate": "12-Nov-2023",
                        "Qty": "Good"
           },
           "Product5": { 
                      "Quantity":"1",
                      "ProdName":"School Bag",
                      "Price":"1064",
                      "Discount":"5%",
                      "Total":"1064",
                      "Total Discount":"44",
                      "Total Price":"1064",
                      "Product code":"P5",
                      "Category":"Bag",
                      "Brand":"Hp",
                      "PruchaseDate":"21-Dec-2023",
                      "ExpTime":"11:30",
                      "ExPlace":"Pune",
                      "ExpDate": "24-Dec-2023",
                      "Qty": "Good"
           },
           "Product6": { 
                       "Quantity":"1",
                       "ProdName":"Hearphone",
                       "Price":"1864",
                       "Discount":"5%",
                       "Total":"1864",
                       "Total Discount":"44",
                       "Total Price":"1864",
                       "Product code":"P6",
                       "Category":"Hearphone",
                       "Brand":"Boats",
                       "PruchaseDate":"12-Jan-2024",
                       "ExpTime":"11:30",
                       "ExPlace":"Pune",
                       "ExpDate": "14-Jan-2024",
                       "Qty": "Good"
           },
           "Product7": { 
                        "Quantity":"1",
                        "ProdName":"Spiral Book",
                        "Price":"150",
                        "Discount":"5%",
                        "Total":"150",
                        "Total Discount":"44",
                        "Total Price":"150",
                        "Product code":"P7",
                        "Category":"Spiral",
                        "Brand":"Classmate",
                        "PruchaseDate":"10-Jan-2024",
                        "ExpTime":"11:30",
                        "ExPlace":"Ubali",
                        "ExpDate": "11-Jan-2024",
                        "Qty": "Good"

           },       
           "Product8": { 
                        "Quantity":"1",
                        "ProdName":"Dongle",
                        "Price":"2799",
                        "Discount":"5%",
                        "Total":"2799",
                        "Total Discount":"44",
                        "Total Price":"2799",
                        "Product code":"P8",
                        "Category":"Dongle",
                        "Brand":"Airtel",
                        "PruchaseDate":"1-Jan-2024",
                        "ExpTime":"11:30",
                        "ExPlace":"Kalmeshwar",
                        "ExpDate": "4-Jan-2024",
                        "Qty": "Good"
             

         },
         "Product9": { 
                      "Quantity":"1",
                      "ProdName":"Khan Saree",
                      "Price":"1864",
                      "Discount":"5%",
                      "Total":"1864",
                      "Total Discount":"44",
                      "Total Price":"1864",
                      "Product code":"P9",
                      "Category":"Saree",
                      "Brand":"Swanini Pathani",
                      "PruchaseDate":"30-Dec-2023",
                      "ExpTime":"11:30",
                      "ExPlace":"Nagpur",
                      "ExpDate": "2-Jan-2024",
                      "Qty": "Good"

         },
         "Product10": { 
                      "Quantity":"1",
                      "ProdName":"Vivo Y200",
                      "Price":"22,564",
                      "Discount":"5%",
                      "Total":"22,564",
                      "Total Discount":"44",
                      "Total Price":"22,564",
                      "Product code":"P1",
                      "Category":"Mobile",
                      "Brand":"Vivo",
                      "PruchaseDate":"26-Dec-2023",
                      "ExpTime":"11:30",
                      "ExPlace":"Nagpur",
                      "ExpDate": "28-Dec-2023",
                      "Qty": "Good"

                }
    }
def add_to_cart():
  try:
    print("="*30)
    print("*****Add to Cart*****")
    print("-"*30)
    Product=input("Enter the Product Name:")
    Quantity=input("Enter the quantity:")
    price=input("Enter the price:")
    ExpDate=input("Enter the ExpDate:")
    Qty=input("Enter the Qty:")
    ExpTime=input("Enter the ExpTime:")
    EXPlace=input("Enter the ExPlace:")
    PurchaseDate=input("Enter the PruchaseDate:")
    Discount=input("Enter the Discount:")
    Category=input("Enter the Category:")
    Brand=input("Enter the Brand:")
    ProductCode=input("Enter the Product code:")
    products.append({"Product":Product,"Quantity":Quantity,
"Price":price,"ExpDate":ExpDate,"Qty":'Good',"ExpTime":ExpTime,"EXPlace":EXPlace,"PurchaseDate":PurchaseDate,"Discount":Discount,"Category":Category,"Brand":Brand,"ProductCode":ProductCode})
     
    check=input("Do you need to verify the Product Details:")
    if check.lower()=='yes' or "y":
        print("Product has been added successfully")
    else:
        print("Product not added successfully")
    #   view_to_products()
  except ValueError:
    print("Please Enter the Valid Information")
    print("="*50)
    # ProdName=input("Enter the Product Name:")
    # Price=int(input("Enter the Price:"))
    # ExpDate=input("Enter the ExpDate [YYYY-MM-DD]:")
    # products.append({"ProdName":ProdName,"Price":Price,"ExpDate":ExpDate,"Qty":'Good'})#Very Important
    # Qty=input("Enter the Qty:")
    # print("Product has been added successfully")
    # check=input("Do you need to verify the Product Details:")
    # if check.lower()=='yes':
    #     #print(tasks)
    #     view_to_cart()
def view_to_products():
  print("="*30)
  print("*****View To Products*****")
  print("-"*30)
  i=1
  if not products:
        print("There is No Product Available")
  else:
    for prod in products:
      print("-----------------------------")
      print("prod",i,"Details")
      print("-----------------------------")
      for key,value in prod.items():
        print(f"{key}-{value}")
    i+=1
    print("="*50)
      
def edit_to_products():
    view_to_products()
    try:
        product_index=int(input("Enter the Index of the Product to the update:"))
        if 0<=product_index<=len(products):
            products[product_index]["Update"]='ProductUpdated'
            print("Product has been Updated")
        check=input("Do you need to verify the Product Details:")
        if check.lower()=='yes':
            view_to_products()
    except ValueError:
        print("Please Enter the Valid Index Position")
def remove_to_products():
    index = int(input("What product would you like to remove?"))
    # pop will remove the items in the list.
    products.pop(index-1)
    print()
# Global variable to store the visit count
visit_count = 0

def increment_visit_to_the_Product():
    global visit_count
    visit_count += 1


def clear_to_products():
    print("Do you want remove the all products")
    products.clear()
    print("Product is clear")
    print("")
def discount_apply_on_products():
    print("="*50)
    print("****Discount of the Product****")
    print("="*50)
    #Caluclate discount based on the ammount and given discount rate in python
    amount=int(input("Enter Sale Price:"))
    #Calculating discount based on sales condition
    if(amount>0):
        if amount<=2000:
            dis=amount*0.07
        elif amount<=5000:
            dis=amount*0.15
        elif amount<=10000:
            dis=0.25*amount
        else:
            dis=0.3*amount
        print("Price Details")
        print("Total Discount :",dis)
        print("Yay!Your total discount is:",dis)
        print("Total Product Price :",amount-dis)
        
    else:
        print("Invalid Amount")
    print("")
def get_the_products_bill():
    print("="*30)
    print("******Product Bill*******")
    print("="*30)
    item1 = 0
    item2 = 0
    sum = 0
    while True:
        item = input("Enter the Product Name:")
        unit = input("Enter the Unit :")
        item1 = int(unit)
        price = input("Enter the Price:")
        item2 = int(price)
        sum += item1 * item2
        next_item= input("Is there another items?")
        if next_item != 'Yes':
            print("Please choose between Yes or No")
        if next_item == "NO":
            break
        print("Price Details")
        print("Total Product Price :",sum)
        print("="*30)

def return_item(self, product, quantity=1):
        self.items = {}
        product =input("Enter product name:")
        quantity=int(input("Enter quantity of product:"))
        # Check if the product is in the cart before returning
        if product in self.items:
            # Subtract the returned quantity, ensuring it doesn't go below zero
            self.items[product] = max(0, self.items[product] - quantity)

def exchange_product(self, old_product, new_product, quantity=1):
        self.items = {}
        old_product=input("Enter the old product name:")
        new_product=input("Enter the new_product name:")
        quantity=int(input("Enter quantity of product:"))
        # Check if the old product is in the cart before exchanging
        if old_product in self.items:
            # Remove the old product
            self.remove_item(old_product, quantity)
            # Add the new product
            self.add_item(new_product, quantity)
def deliver(self):
        self.items = {}
        print("Delivering products:")
        for product, quantity in self.items.items():
            print(f"{quantity}x {product}")
        print("Products delivered successfully!")
    
def main():
    loopstatus=True
    while loopstatus:
        shopping_cart_display_menu()
        choice=int(input("Enter your choice:"))
        if choice==1:
            login_app()
            # create_user()
        elif choice==2:
            # login_app()
            create_user()
        if choice==3:
            create_product()
        elif choice==4:
            add_to_cart()
        elif choice==5:
            view_to_products()
        elif choice==6:
            edit_to_products()
        elif choice==7:
            increment_visit_to_the_Product()
        elif choice== 8:
            remove_to_products()
        elif choice==9:
            clear_to_products()
        elif choice==10:
            discount_apply_on_products()
        elif choice==11:
            get_the_products_bill()
        elif choice==12:
            return_item()
        elif choice==13:
            exchange_product()
        elif choice==14:
            deliver()
        elif choice==15:
            loopstatus=False
            print("Exiting from the Shopping cart Application..GoodBye!")
            break
        else:
            print("Invalid choice,please enter your choice between[1-4]:")
            continueState=input("\nDo You Want To Continue Again(Y Or N):")
            print(' ')
            if continueState == 'N' or continueState == 'n':
                print("\nYou Requested For Process Termination...Thank You")
                loopstatus=False
if "__init__"==main():
   main()
