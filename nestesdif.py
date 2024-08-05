pizza=60
samosa=30
cutlet=25
burger=100
shawarma=120
fingers=90
hotchocolate=120
milkshake=110
coffee=50
print('-----Welcome to JUPITER CINEMAS😄-----')
print('Menu is listed below')
food=int(input('Your food type: \nPRESS 1- VEG \nPRESS 2- NONVEG  \nPRESS 3- VEGAN \nPRESS 4- DRINKS \n'))
print(food)
if(food==1):
    print('your choice is VEG')
    print('your menu :\npress 1- Pizza \npress 2- Samosa \npress 3- Cutlet')
    yourOrder=int(input('enter your choice: '))
    print(yourOrder)
    if(yourOrder==1):
        print('your ordered a pizza')
        print('The price is 60/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Ketchup \npress 6- Chilly sauce')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',pizza+20)
            elif(addendum==6):print('your amount is',pizza+10)
            else:print('INVALID')
        else:print('no addendums needed')    
    elif(yourOrder==2):
        print('you ordered a samosa') 
        print('The price is 30/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Ketchup \npress 6- Chilly sauce')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',samosa+20)
            elif(addendum==6):print('your amount is',samosa+10)
            else:print('INVALID')
        else:print('no addendums needed')    
    elif(yourOrder==3):
        print('you ordered a cutlet')   
        print('The price is 25/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Ketchup \npress 6- Chilly sauce')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',cutlet+20)
            elif(addendum==6):print('your amount is',cutlet+10)
            else:print('INVALID')
        else:print('no addendums needed')    
elif(food==2):
    print('your choice is NON-VEG')
    print('your menu : \npress 1- Burger \npress 2- Shawarma \npress 3- Fingers')
    yourOrder=int(input('enter your choice: '))
    print(yourOrder)
    if(yourOrder==1):
        print('your ordered a burger ')
        print('The price is 100/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Ketchup \npress 6- Mayonaisse')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',burger+20)
            elif(addendum==6):print('your amount is',burger+30)
            else:print('INVALID')
        else:print('no addendums needed')    
    elif(yourOrder==2):
        print('you ordered a shawarma') 
        print('The price is 100/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Ketchup \npress 6- Mayonaisse')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',shawarma+20)
            elif(addendum==6):print('your amount is',shawarma+30)
            else:print('INVALID')
        else:print('no addendums needed')    
    elif(yourOrder==3):
        print('you ordered a fingers')    
        print('The price is 100/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Ketchup \npress 6- Mayonaisse')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',fingers+20)
            elif(addendum==6):print('your amount is',fingers+30)
            else:print('INVALID')
    else:print('no addendums needed')    
elif(food==3):
    print('your choice is VEGAN')
    print('your menu : \npress 1- Salad \npress 2- Veganyoghurt \npress 3- Seaweedbites')
    yourOrder=int(input('enter your choice: '))
    print(yourOrder)
    if(yourOrder==1):
         print('your ordered a salad ')
         print('The price is 80/-')
    elif(yourOrder==2):
        print('you ordered a veganyoghurt') 
        print('The price is 110/-')
    elif(yourOrder==3):
        print('you ordered a seaweedbites')    
        print('The price is 90/-')
elif(food==4):
    print('enter your choice of DRINKS')
    print('your menu : \npress 1- Hotchocolate \npress 2- Milkshake \npress 3- Coffee')
    yourOrder=int(input('enter your choice: '))
    print(yourOrder)
    if(yourOrder==1):
        print('your ordered a hot chocolate ')
        print('The price is 120/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- chocochips \npress 6- cream')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',hotchocolate+30)
            elif(addendum==6):print('your amount is',hotchocolate+20)
            else:print('INVALID')
        else:print('no addendums needed')    
    elif(yourOrder==2):
        print('you ordered a milkshake') 
        print('The price is 110/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- Nuts \npress 6- icecream')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',milkshake+30)
            elif(addendum==6):print('your amount is',milkshake+40)
            else:print('INVALID')
        else:print('no addendums needed')    
    elif(yourOrder==3):
        print('you ordered a coffee')    
        print('The price is 50/-')
        print('Do you need an addendum???')
        addendum=(input("enter yes or no: "))
        if(addendum=='yes'):
            print('choose your :\npress 5- sugar \npress 6- milk')
            addendum=(int(input("enter your choice: ")))
            if(addendum==5):print('your amount is',coffee+20)
            elif(addendum==6):print('your amount is',coffee+10)
            else:print('INVALID')
        else:print('no addendums needed')    
else:print('no order given')
    
    



        





        


        



