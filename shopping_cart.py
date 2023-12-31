global products
products=[]
def shopping_cart_display_menu():
    print("="*50)
    print("\tShopping-Cart ")
    print("="*50)
    print("1.Create Products")
    print("2.Add to cart")
    print("3.View cart")
    print("4.Edit cart")
    print("5.Remove cart")
    print("6.Clear cart")
    print("7.Apply Discount")
    print("8.Get the Bill ")
    print("9.Exit from the Application")
    print("="*50)
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

def main():
    loopstatus=True
    while loopstatus:
        shopping_cart_display_menu()
        choice=int(input("Enter your choice:"))
        if choice==1:
            pass
        elif choice==2:
            add_to_cart()
        elif choice==3:
            view_to_products()
        elif choice==4:
            edit_to_products()
        elif choice== 5:
            remove_to_products()
        elif choice==6:
            clear_to_products()
        elif choice==7:
            discount_apply_on_products()
        elif choice==8:
            get_the_products_bill()
        elif choice==9:
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
