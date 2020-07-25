# Gardener v1.0 This program is made for holding user data on mongodb.my goal was making a really fast  data
# searcher. searching for exact data it's god damn fast (you need make text indexes) but regex search take 30 seconds
# for 2 gb dummy data. you can load datas from txt and you can search with mail or password. don't use for illegal
# things. this is just  fun programing for learning mongodb and python. and also some assholes stole my  dominos
# pizza account. not cool. always look is your passwords pawned and don't steal peoples accounts. you can choice best
# longest passwords but if this application database hacked. your pass will leake so don't use same pass on every
# account.
#
# example txt file(there is function for normalize data belove.it's basic but you can change for your data):
#  mail1;pass1
#  mail2;pass2
#
# created by sabrey

import pymongo
import os
from pyfiglet import Figlet
import pyutil


client = pymongo.MongoClient(
    "mongodb://localhost:27017/")

db = client.testdb # client . your db name
posts = db.testcollection  # db . your colection Name

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def load_data_from_directory():
    your_path = input("Path? :")
    files = os.listdir(your_path)
    for file in files:
        tempFile = open(os.path.join(your_path, file), "r", encoding="utf8")

        for line in tempFile:
            try:
                pair = line.split(";")
                post = {"mail": pair[0],
                        "pass": pair[1][:-1], }
                post_id = posts.insert_one(post).inserted_id
            except:
                print("exception occured!!!")
                continue
        print(os.path.join(your_path, file) + '  ✓')
    input("")

def load_data_from_file():
    your_path = input("Path? :")
    tempFile = open(your_path, "r", encoding="utf8")
    for line in tempFile:
        try:
            pair = line.split(";")
            post = {"mail": pair[0],
                    "pass": pair[1][:-1], }
            post_id = posts.insert_one(post).inserted_id
        except:
            print("exception occured!!!")
            continue
    print(your_path + '  ✓')
    input("")



def find_from_db(mail,type,exact):
    # print(mail," password:",posts.find_one({"mail": mail})['pass'])
    if(exact):
        filter = {type: mail}
    else:
        filter = {type: {"$regex": mail}}

    sort = [("abc", pymongo.DESCENDING)]
    skip = 0
    limit = 10000

    if(len(mail)<5):
        results = posts.find(filter).sort(sort).skip(skip).limit(limit)
        print("\ndon't search too short next time.i didn't add pagination.\nyou are seeing 10000 result only.am ı look like Terry Davis?? he is the best programmer btw.\n")
    else:
        results = posts.find(filter).sort(sort).skip(skip)
    doc_count = posts.count_documents(filter, skip=skip)


    if(doc_count==0):
        print("no data founded.")
        input("")
        return

    print(" _______________________________________________________________\n results:\n")
    for documento in results:
        print(documento["mail"],":",documento["pass"])
    input("")

# normalize(":",";") this function replace characters in files in directory .
def normalizer(this,tothis):
    your_path = input("Path? :")
    files = os.listdir(your_path)
    print(files)
    for file in files:
        pyutil.filereplace(os.path.join(your_path, file), this, tothis)
        print(os.path.join(your_path, file) + '  ✓')


def menu():
    cls()
    custom_fig = Figlet(font='slant')
    print(custom_fig.renderText('gardener '))
    print("by sabrey")
    print("_______________________________________________")
    print("1-Search mail in branches \n2-Search password in branch\n3-Fast mail search(really fast.exact value) \n4-Fast pass search(really fast.exact value)\n5-Load branch file to database \n6-Load branch to database from directory \n7-exit")
    choice = input("choice : ")

    if choice == '1':
        find_from_db(input("mail ?:"),"mail",False)
        menu()
    elif choice == '2':
        find_from_db(input("pass ?:"),"pass",False)
        menu()
    elif choice == '3':
        find_from_db(input("mail ?:"), "mail",True)
        menu()
    elif choice == '4':
        find_from_db(input("pass ?:"), "pass",True)
        menu()
    elif choice == '5':
        load_data_from_file()
        menu()
    elif choice == '6':
        load_data_from_directory()
        menu()
    elif choice =='7':
        exit()
    else:

        print("wrong choice")
        menu()




def main():
    menu()

if __name__ == "__main__":
    main()