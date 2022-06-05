# 4 semester exam
# Created Juni 2022 by DK1Gruppe3

import mysql.connector # Importere et module som gør det muligt at oprette forbindelse til en MySQL server.
import Connect_server as connection # En funktion bliver importeret.

def Createprofil():
    try:
        thisConn = connection.connect() # En variabel bliver defineret til at være databaseforbindelsen
        print("Opret en profil:")

        Fornavn = input("Indtast fornavn:") # Et input fra brugeren.
        Efternavn = input("Indtast efternavn:") # Et input fra brugeren.
        Email = input("Indtast email:") # Et input fra brugeren.

        # Denne kommando producere en markør som kan eksekvere en forspørgsel på MySQL serveren.
        # "cur" bliver sat til at være en markør på "connection" som er forbindelsen til serveren.
        cur = thisConn.cursor()
        sql = "insert into Delivery5.Kundedata(Fornavn, Efternavn, Email) values(%s, %s, %s)"
        val = (Fornavn, Efternavn, Email)

        # Kommandoen "execute" er den funktion som eksekverer forspørgselen på MySQL serveren.
        cur.execute(sql, val)

        # Denne kommando får eksekveringen til at træde i kraft på MySQL serveren.
        thisConn.commit()

        print("Dit kunde_id nr: ", cur.lastrowid)

        # Denne kommando lukker for forbindelsen.
        thisConn.close()
    except mysql.connector.Error as error:
        print("Profilen blev ikke oprettet {}".format(error))