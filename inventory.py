from MediaItem import MediaItem


def display_menu():
    print("\nMenu");
    print("====");
    print("1-List Inventory");
    print("2-Info Inventory");
    print("3-List of All Books");
    print("4-List of All Movies");
    print("5-Item Description");
    print("6-Remove Item");
    print("7-Add Item");
    print("8-Set Maximum Price");
    print("0-Exit\n");


    
######## All other functions listed below

def initialize(): #list of all media items
    o1=MediaItem("Movie","2001: A Space Odyssey","11.99","TU2RL012","Stanley Kubrick","Keir Dullea",None)
    o2=MediaItem("Book","A Brief History of Time","10.17","GV5N32M9",None,None,"Stephen Hawking")
    o3=MediaItem("Movie","North by Northwest","8.99","1DB6HK3L","Alfred Hichcock","Cary Grant",None)
    o4=MediaItem("Movie","The Good, The Bad and The Ugly","9.99","PO5T7Y89","Sergio Leone","Clint Eastwood",None)
    o5=MediaItem("Book","The Alchemist","6.99","TR3FL0EW",None,None,"Paulo Coelho")
    o6=MediaItem("Book","Thus Spoke Zarathustra","7.81","F2O9PIE9",None,None,"Friedrich Nietzsche")
    o7=MediaItem("Book","Jonathan Livingston Seagull","6.97","R399CED1",None,None,"Richard Bach")
    o8=MediaItem("Movie","Gone with the Wind","4.99","2FG6B3N9","Victor Fleming","Vivien Leigh",None)
    o9=MediaItem("Book","Gone with the Wind","7.99","6Y9OPL87",None,None,"Margarett Mitchell")
    media_list=[o1,o2,o3,o4,o5,o6,o7,o8,o9]
    return media_list

def display(l,display,maxPrice): #display takes in the list, which display (entire/movie/book), and the maximum price
    if display == "choice_1":
        for i in l:
            price = float(i.p)#choice 8
            if price <= maxPrice:
                print(i.r,i.m,i.t,'$' + i.p)
    #choice 4 is selected, display only movies
    elif display == "choice_4":
        for i in l:
            if i.m == "Movie":
                price = float(i.p)#choice 8
                if price <= maxPrice:
                    print(i.r,i.m,i.t,'$' + i.p)
    #choice 3 is selected, display only books
    elif display == "choice_3":
        for i in l:
            if i.m == "Book":
                price = float(i.p)#choice 8
                if price <= maxPrice:
                    print(i.r,i.m,i.t,'$' + i.p)
#Option 2
def info(l):
    sum = 0
    max = 0
    book=0
    movie=0
    for i in l:
        p= float(i.p)
        sum +=p
        if i.m == "Book":
            book = book + 1
        elif i.m == "Movie":
            movie = movie + 1
        if p > max:
            max=p
    print("\nInventory is worth $"+str(sum)+"\nMost expensive item at $"+str(max)+"\nThere are "+str(book)+" Book(s), and "+str(movie)+" Movie(s)")

#option 5
def search_item(item):
    for i in initialize():
        if i.r == item:
            return i #gives the number in the list of the media item
    return None

def display_item():
    item_reference = input("Enter item reference: ")
    search = search_item(item_reference)
    if search is None:
        print("No such item found!")
    else:
        if search.m=="Movie":
            print("Title: "+str(search.t)+" (Ref: "+str(search.r)+", Price: $"+str(search.p)+");\nMovie Director: "+str(search.d)+"; Lead Actor: "+str(search.l))
        elif search.m=="Book":
            print("Title: "+str(search.t)+" (Ref: "+str(search.r)+", Price: $"+str(search.p)+");\nAuthor: "+str(search.a))

#Option 6
def search_index_item(name): #searches for item within the list and gives its list value
    x=0
    for i in initialize():
        if i.r == name:
            return x
        x = x+1
    return None

def delete_index_item(l): #Removes item from the list and returns the list
    item_reference = input("Enter item reference: ")
    search = search_index_item(item_reference)
    if search is None:
        print("Item does not exist")
    else:
        del l[search]
    return l

#Option 7
def create_item(l):
    bm = input("Book or Movie? ")
    author = ''
    director = ''
    lead = ''
    if bm == "Book":
        title = input("Enter Book Title: ")
        reference = input("Enter Book Reference: ")
        price = input("Enter Book Price: ")
        author = input("Enter Author Name: ")
        new_item = MediaItem(bm,title,price,reference,director,lead,author)
        l.append(new_item)
    elif bm == "Movie":
        title = input("Enter Movie Title: ")
        reference = input("Enter Movie Reference: ")
        price = input("Enter Movie Price: ")
        director = input("Enter Director Name: ")
        lead = input("Enter Lead Actor Name: ")
        new_item = MediaItem(bm,title,price,reference,director,lead,author)
        l.append(new_item)
    else:
        print("Wrong input!")
    return l



