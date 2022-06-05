# 4 semester exam
# Created Juni 2022 by DK1Gruppe3

from beautifultable import BeautifulTable # Et module som gør det mere overskueligt at se en tabel.
import Connect_server as connection # En funktion bliver importeret.

# En funktion bliver oprettet.
def Seecustomer():
    thisConn = connection.connect() # En variabel bliver defineret til at være databaseforbindelsen
    # Denne kommando producere en markør som kan eksekvere en forspørgsel på MySQL serveren.
    # "mycursor" bliver sat til at være en markør på "connection" som er forbindelsen til serveren.
    mycursor = thisConn.cursor()

    # Kommandoen "execute" er den funktion som eksekverer forspørgselen på MySQL serveren.
    mycursor.execute("SELECT Kunde_id, Fornavn, Efternavn, Email FROM Delivery5.Kundedata;")

    # mycursor.fetchall() er en kommando for at oprette en tabel med dataen fra forspørgslen.
    result = mycursor.fetchall()

    # Denne kommando komprimerer outputtet af forspørgslen til en mere overskuelig tabel.
    table = BeautifulTable(maxwidth=140, precision=10)
    # Kommandoen skal vide hvilke overskrifter som tablen har og kan efter de oplysninger lave den færdige tabel.
    table.columns.header = ["Kunde_id", "Fornavn", "Efternavn", "Email"]
    # I dette for loop skriver den hver linje ind på den overskuelige tabel.
    for row in result:
        # Nu tilføjes rækkerne til tablen.
        table.rows.append(row)
    # Nu printes tablen.
    print(table)

