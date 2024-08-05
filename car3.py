import os.path
import os
import pathlib
import json
import re
import mysql.connector #MYSQL

#CONNECTION to DATABASE MYSQL
#the name of the database is "CAR"
db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="car")
############################


#filePath = "OneDrive\Desktop\python\car\list.txt"
#filePath = "list.txt"
#show the principal menu
def principal_menu_1():
    print("\n")
    print("--► PRINCIPAL MENU ◄--")
    print("1) Enter the car") #works
    print("2) Delete car") 
    print("3) Edit the car") #working in progress.....
    print("4) Show the complete list") #works
    print("5) Exit") #works
    #i call the logical menu
    logic_menu_1()

##########################################################
##################  MENU 1 ###############################
##########################################################
#LOGICAL MENU
def logic_menu_1():
    choose = input("►....")
    if choose == "1":
        enter_car_menu() # menu for add the new car
    elif choose == "2":
        delete_car() #menu for delete the car
    elif choose == "3":
        choose_car() # menu for edit the car
    elif choose == "4":
        show_the_list() #menu for show the entire list
    elif choose == "5":
        print("--► Exit ◄--")
        pass
    else:
        print("Wrong value...\ntry again...\n")
        logic_menu_1()
#################################################

def enter_car_menu():

    print("--►Enter the new car ◄--")
    #All characteristics about the car
    print("Brand..")
    brand=input("►....")

    #Function to check if the value has numbers
    print("Year..")
    flag=0
    check=0
    while flag == 0:
        year=input("Write the year...")
        if ctrl_year(year,1):
            flag=1
        else:
            print("The year is not write in the right way...\nTry again...")

    print("kilometers..")
    flag=0
    while flag == 0:
        km=input("Write the KM...")
        if ctrl_year(km,2):
            flag=1
        else:
            print("The KM is not write in the right way...\nTry again...")

    print("Color..")
    color=input("►....")

    print("Plate..")
    plate=input("►....")

    print("Fuel..")
    fuel=input("►....")

    #function for record all characteristics of the car
    record_new_car(brand,year,km,color,plate,fuel)

def record_new_car(brand,year,km,color,plate,fuel):
    
    #redord the datas in the database
    data=db.cursor()
    data.execute("INSERT INTO car (brand,year,km,color,plate,fuel) VALUES (%s,%s,%s,%s,%s,%s)",(brand,year,km,color,plate,fuel))
    db.commit()
    #############
    #To come back in the principal menu
    principal_menu_1()


##########################################################
##################  MENU 2 ###############################
##########################################################
def delete_car(): #FUNCTION for delete a car
    data=db.cursor()
    print("----------------------------------------------------")
    print("--► LIST OF THE CARS ◄--")
    data.execute("SELECT * FROM car") #SHOW THE LIST    
    for x in data:
        print(x)
    print("----------------------------------------------------\n")

    print("Select which car do you want delete it")
    delete=int(input("Select the ID..."))

    data.execute("DELETE FROM car WHERE id = {delete2}".format(delete2=delete)) #DELEET A CAR
    db.commit()

    print("--► The car was delete  ◄--\n")

    principal_menu_1()


##########################################################
##################  MENU 3 ###############################
##########################################################
def choose_car():
    data=db.cursor()
    print("----------------------------------------------------")
    print("--► LIST OF THE CARS ◄--")
    data.execute("SELECT * FROM car") #SHOW THE LIST    
    for x in data:
        print(x)
    print("----------------------------------------------------\n")

    print("Select which car do you want Edit")
   
    value=int(input("Select the ID...")) #you choose the value, the valie is the ID in MYSQL
    
    data.execute("SELECT * FROM car WHERE id = {value2}".format(value2=value))#
    for y in data:
        print("--► ",y," ◄--")
    #Enter in the VISUAL MENU to edit the values in MYSQL
    look_car_menu()
    look_logic(value) #Value is ID of the TABLE
 


def look_car_menu(): #SHOW THE MENU FOR EDIT THE VALUES IN MYSQL
    print("--► Edit an item ◄--")
    print("Choose what do you want edit..")
    print("1) brand")
    print("2) year")
    print("3) km")
    print("4) color")
    print("5) plate")
    print("6) fuel")
    print("0) exit")
    #Enter in the logic menu..
    

    #Logic menu
def look_logic(id): #LOGIC MENU FOR EDIT THE VALUES IN MYSQL
    print("Choose what do you want EDIT in your data")
    data=db.cursor()
    flag=0
    while flag == 0:
        option=input("►....")
        if option == "1":
            table="brand"
            new_value=input("►....")
            flag=1
        elif option == "2":
            table="year"
            new_value=input("►....")
            flag=1
        elif option == "3":
            table="km"
            new_value=input("►....")
            flag=1
        elif option == "4":
            new_value=input("►....")
            table="color"
            flag=1
        elif option == "5":
            table="plate"
            new_value=input("►....")
            flag=1
        elif option == "6":
            table="fuel"
            new_value=input("►....")
            flag=1
        elif option == "0":
            flag=1
            print("--► Come back in the menu ◄--")
            principal_menu_1()
        else:
            print("Wrong value...\nTry again...")

        
    #UPDATE THE DATA INSIDE THE TABLE
    data.execute("UPDATE car SET {table2} = '{new_value2}' WHERE id = {id2} ".format(table2=table,new_value2=new_value,id2=id))
    db.commit()
    print("The Editing has been done")
    
    #Come back in the Principal menu
    principal_menu_1()
    


##########################################################
##################  MENU 4 ###############################
##########################################################

def show_the_list():# SHOW THE LIST 
    data=db.cursor()

    print("----------------------------------------------------")
    print("--► LIST OF THE CARS ◄--")
    data.execute("SELECT * FROM car") #SHOW THE LIST    
    for x in data:
        print(x)
    print("----------------------------------------------------")
    #To come back in the principal menu
    principal_menu_1()

##########################
#FUNCTION TO CHECK THE YEAR AND KM
def ctrl_year(number,check):
    if check == 1:
        number_regex = re.compile(r'^\d{4}$')
        return bool(number_regex.match(number))
    elif check == 2:
        number_regex = re.compile(r'^\d{1,6}$')
        return bool(number_regex.match(number))

###################################### 


#RICFAS - forse questo ti da errore? Toglilo secondo me
principal_menu_1()