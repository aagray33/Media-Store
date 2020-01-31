#### Import Modules
import inventory



'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
maxPrice=100.0
media_list=inventory.initialize()


print("Welcome to BestMedia\n====================\n")

while True:
    inventory.display_menu()
    choice=str(input("Enter Command: "))
    
    if choice == '0':
        break
    
    elif choice =='1':
        print("\nReference/Media/Title/Price (max=$"+str(maxPrice)+")\n---------------------------")
        inventory.display(media_list,"choice_1",maxPrice)
        
    elif choice =='2':
        inventory.info(media_list)
        
    elif choice =='3':
        print("\nReference/Media/Title/Price (max=$"+str(maxPrice)+")\n---------------------------")
        inventory.display(media_list,"choice_3",maxPrice)
        
    elif choice =='4':
        print("\nReference/Media/Title/Price (max=$"+str(maxPrice)+")\n---------------------------")
        inventory.display(media_list,"choice_4",maxPrice)
        
    elif choice =='5':
        inventory.display_item()
        
    elif choice =='6':
        media_list = inventory.delete_index_item(media_list)
        
    elif choice =='7':
        inventory.create_item(media_list)
        
    elif choice =='8':
        maxPrice = float(input("Enter maximum price (current=$"+str(maxPrice)+"): "))
        
print("Goodbye!")

