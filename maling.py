# 4 semester exam
# Created Juni 2022 by DK1Gruppe3

import pymongo
def insertmaling():
    # Her skrives mongodb altsa url til at connecte python til mongodb ved brug af pymongo
    CONNECTION_STRING = "clienturl"
    cluster = pymongo.MongoClient(CONNECTION_STRING)

    # Opret database
    db = cluster["Kundemåle"]

    # Opret collection
    collection = db["Målinger"]

    kundeid = input("Hvad er dit kundeid?")  # Et input fra brugeren.
    måling1 = input("Måling 1:")  # Et input fra brugeren.
    måling2 = input("Måling 2:")  # Et input fra brugeren.
    måling3 = input("Måling 3:")  # Et input fra brugeren.
    måling4 = input("Måling 4:")  # Et input fra brugeren.

    # Indsæt et dokument
    firstrow = {"Kundeid": kundeid, "mål1": måling1, "mål2": måling2, "mål3": måling3, "mål4": måling4}
    x = collection.insert_one(firstrow)

    print("Måling tilføjet se id:", x.inserted_id)