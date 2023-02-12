import json
from collections import deque

with open('mylist.json') as json_file:
    data = json.load(json_file)

with open('watchlist.json') as json_file:
    toWatch = json.load(json_file)

#============================================================================================================================================

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = BinarySearchTree(data)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        
        return elements

    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        
        return elements

    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)

        return elements
    
    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
        else: 
            return True

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            minVal = self.right.findMin()
            self.data = minVal
            self.right = self.right.delete(minVal)
        return self
        
def buildTree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.addNode(elements[i])

    return root

#============================================================================================================================================

def randomPicker():
    while True:
        #RANDOM PICKER FOR ANIMEs TO BINGE
        from random import choice
        animelists = []

        print()
        print('======================================')
        print('||     WHAT GENRE DO YOU WANT?      ||')
        print('======================================')
        print('  Input "0" to go back to main menu!')
        print('--------------------------------------')
            
        while True:

            genre = input('Type here: ')
            if genre == "0":
                input('press enter to go back to main menu')
                mainMenu()
            result = any(genre in d.values() for d in data.values())
            if result:
                break
            else:
                print("Genre currently does not exist!")
                print()

            
        print()
        print('======================================')
        print('||      DO YOU WANT TO WATCH A      ||')
        print('||     "SHORT" OR "LONG" ANIME?     ||')
        print('======================================')
        print('  Input "0" to go back to main menu!')
        print('--------------------------------------')
        print()

        #add input validation
        while True:
            length = input('Type short/long: ')
            if length == "0":
                input('press enter to go back to main menu')
                mainMenu()
            length = length.lower()
            if length == 'short' or length == 'long':
                break
            else:
                print('Wrong input! Try again!')
                continue
            
        print()


        print('======================================')
        print('||   WHAT DO YOU WANT TO WATCH A    ||')
        print('||       SERIES OR A MOVIE?         ||')
        print('======================================')
        print('  Input "0" to go back to main menu!')
        print('--------------------------------------')
        print()

        while True:
            movieSeries = input('Type series/movie: ')
            if movieSeries == "0":
                input('press enter to go back to main menu')
                mainMenu()
            movieSeries = movieSeries.lower()
            if movieSeries == 'series' or  movieSeries == 'movie':
                if length == 'long' and movieSeries == 'movie':
                    print()
                    print('------------------------------------')
                    print('ERROR: There are only "SHORT" movies!')
                    print('------------------------------------')
                    print()
                    continue
                else:
                    break
            else:
                print('Wrong input! Try again!')
                continue

        print()

        for p_id, p_info in data.items():
            if p_info == {'Genre': genre, 'Length': length, 'Type': movieSeries}:
                animelists.append(p_id)
            else:
                animelists = []      

        print(animelists)
        if animelists == []:
            print('--------------------------------------')
            print("||    SORRY, NOTHING FOUND WITH     ||")
            print("||      THOSE COMBINATIONS :(       ||")
            print('--------------------------------------')
            tryAgain = input('Press any key to leave and "Y" to try again...')
            if tryAgain == "Y" or tryAgain == "y":
                continue
            else:
                input('press enter to go back to main menu...')
                break
        else:
            recommend = str(choice(animelists))
            recommend.upper()
            print('======================================')
            print('||   THE ANIME YOU WILL WATCH IS... ||')
            print('======================================')
            print()
            print("           '" + recommend +"'")
            print()
            print('======================================')
            print()
            addToQueue(recommend)
            break

#============================================================================================================================================

def addNewAnime():

    with open('mylist.json') as json_file:
        data = json.load(json_file)
    newLists = {}

    print('------------------------------------')
    print("Type '0' to go back to the main menu")
    print('------------------------------------')

    while True:

        size = (input("How many anime/s will you add: "))
        print('------------------------------------')

        if size == "0":
            input("press enter to proceed.")
            break
            
        else:     
            try:
                for i in range(int(size)):
                    dict_name = input("Enter the name of the anime: ")

                    newLists[dict_name] = {}
                    genre = input("Enter genre: ")
                    length = input("Is the anime short or long: ")
                    episodes = int(input("Enter number of episodes: "))
                    type = input("Enter type: ")
                    newLists[dict_name]["Genre"] = genre
                    newLists[dict_name]["Episodes"] = episodes
                    newLists[dict_name]["Type"] = type
                    newLists[dict_name]["Length"] = length

                    data.update(newLists)

                    print()
                    print("Anime Successfully Added!")
                    print('----------------------------------')
                    #print(sorted(data))

                    with open("mylist.json", "w") as write_file:
                        json.dump(data, write_file, indent=4, sort_keys=True)
                    doYouWant = input('Do you want to add it to watch queue? Y/N')
                    doYouWant = doYouWant.lower()
                    if doYouWant == "y":
                        addToQueue(dict_name)
                    else:
                        input("press enter to proceed")
                        mainMenu()
                break
            except:
                continue

#============================================================================================================================================

def findAnime():
    print('-----------------------------------')
    print("Type '0' to go back to main menu.")
    print('-----------------------------------')
    print("        Find anime by... ")
    print()
    print("| Title | Genre | Length | Type |")
    print("-----------------------------------")

    while True:
        howSearch = input("Input here: ")
        howSearch = howSearch.lower()
        print('---------------------------------')
        if howSearch == "title":
            title = input("What is the title of the anime? ")
            myList = list(data.keys())
            treeList = buildTree(myList)
            if (treeList.find(title)):
                print("The anime exists in your list")
                print('-----------------------------------')
                while True:
                    if title in toWatch:
                        print('but the anime is already in the queue!')
                        print('-------------------------------------')
                        input('press enter to go back to main menu')
                        mainMenu()
                    else:
                        break
            else:
                print('That anime does not exist')
                print('------------------------------')
                while True:
                    doYou = input('Do you want to add that anime? Y/N: ')
                    doYou = doYou.lower()
                    if doYou == "y":
                        print()
                        print()
                        addNewAnime()
                    elif doYou == "n":
                        print('-------------------------------')
                        input('press enter to go back to main menu...')
                        mainMenu()
                        break
                    else:
                        print('-------------------------------')
                        print("wrong input!")
                        continue
            break
        elif howSearch == "genre":
            genre = input("What is the genre? ")           
            genreList = []
            for x in data:
                for i in data[x].values():
                    if i == genre:
                        genreList.append(x)
            for genres in genreList:
                print(genres)
            print('-------------------------------')
            input("press enter to proceed...")
            break
        elif howSearch == "length":
            length = input("Is the anime short or long? ")
            lengthList = []
            for x in data:
                for i in data[x].values():
                    if i == length:
                        lengthList.append(x)
            for lengths in lengthList:
                print(lengths)
            print('-------------------------------')
            input("press enter to proceed...")
            break
        elif howSearch == "type":
            type = input("Is the anime a movie or a series? ")
            typeList = []
            for x in data:
                for i in data[x].values():
                    if i == type:
                        typeList.append(x)
            for types in typeList:
                print(types)
            print('-------------------------------')
            input("press enter to proceed...")
            break
        elif howSearch == "0":
            print('-------------------------------')
            input("press enter to proceed...")
            mainMenu()
            break
        else:
            print("Wrong input!")
            print()
            continue        

#============================================================================================================================================                

def mainMenu():
    while True:
        print()
        print("------------------------------------")
        print("            MAIN MENU")
        print("     What do you want to do?")
        print()
        print("  Add a new anime to the list = 1")
        print("   Find an anime in the list = 2")
        print("Pick a random anime in the list = 3")
        print("   Add anime to watch queue = 4")
        print("       Show watch queue = 5")
        print('      Dequeue watchlist = 6')
        print("------------------------------------")
        print("             LEAVE = 0")
        print("------------------------------------")
        print()
        choice = input("What is your choice: ")
        print()
        if choice == "0":
            break
        while True:
            if choice == "1":
                addNewAnime()
                break
            elif choice == "2":
                findAnime()
                break
            elif choice == "3":
                input('press enter to proceed...')
                randomPicker()
                break
            elif choice == "4":
                print("Find the anime you want to add?")
                print()
                quitSure = input("Type 'Y' to proceed and press enter to quit... ")
                if quitSure == "Y" or quitSure == "y":
                    addQueue1()
                else:
                    input('press enter to go back to main menu...')
                    break
            elif choice == "5":
                print('---------------------------------------')
                print('This is/are your current watch queue')
                iter = 0
                for i in toWatch:
                    iter += 1
                    iter = iter
                    print(str(iter) + ". " + str(i))
                print('---------------------------------------')
                input('press enter to proceed: ')
                break
            elif choice == "6":
                dequeue()
            else:
                print("Wrong input!")
                break
        
    heya = input("press enter to proceed: ")

#============================================================================================================================================

def addToQueue(anime):
    anime = anime.lower()
    print('Add anime to queue?')
    while True:
        yesNo = input('Y/N: ')
        yesNo = yesNo.lower()
        if yesNo == "y":
            toWatch.append(anime)
            with open("watchlist.json", "w") as write_file:
                json.dump(toWatch, write_file, indent=4)
            print(toWatch)
            print("Anime added")
            mainMenu
        else:
            print('OK')
            print(toWatch)
            break

#============================================================================================================================================

def dequeue():
    origList = []
    for x in toWatch:
        origList.append(x)
    print('---------------------------')
    print('   "Current Watchlist"')
    print('---------------------------')
    x = 0
    for i in toWatch:
        x += 1
        print(str(x) + ". " + i)
    removeHaha = deque(origList)

    while True:
        print('---------------------------')
        lolHow = input('Are you done with ' + origList[0] + '? Y/N: ')
        lolHow = lolHow.lower()
        print('---------------------------')        
        if lolHow == 'y':
            removeHaha.popleft()
            break
        elif lolHow == 'n':
            input('press enter to go back to main menu...')
            mainMenu()
        else:
            print("wrong input!")
            continue
    print('This is the new list!')
    n = 0
    toWrite = []
    for i in removeHaha:
        toWrite.append(i)
        n += 1
        print(str(n) + ". " + i)
    with open("watchlist.json", "w") as write_file:
        json.dump(toWrite, write_file, indent=4)
    print('--------------------------------------')
    input('press enter to go back to main menu...')
    mainMenu()
    
#============================================================================================================================================

def addQueue1():
    print('-----------------------------------')
    print("Type '0' to go back to main menu.")
    print('-----------------------------------')
    while True:
        title = input("What is the title of the anime? ")
        myList = list(data.keys())
        treeList = buildTree(myList)
        if (treeList.find(title)):
            print("The anime exists in your list")
            print('-----------------------------------')
            while True:
                if title in toWatch:
                    print('but the anime is already in the queue!')
                    print('-------------------------------------')
                    input('press enter to go back to main menu')
                    mainMenu()
                else:
                    break
        elif title == "0":
            input('press enter to proceed...')
            mainMenu()
        else:
            print('That anime does not exist')
            print('------------------------------')
            while True:
                doYou = input('Do you want to add that anime? Y/N: ')
                doYou = doYou.lower()
                if doYou == "y":
                    print()
                    print()
                    addNewAnime()
                elif doYou == "n":
                    print('-------------------------------')
                    input('press enter to go back to main menu...')
                    mainMenu()
                    break
                else:
                    print('-------------------------------')
                    print("wrong input!")
                    continue
        break