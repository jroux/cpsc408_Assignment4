#Jessica Roux
#Student ID: 2317255
#Chapman Email: jroux@chapman.edu
#Course: 408-01
#Assignment 4


#Necessary imports to run program
import mysql.connector
from faker import Faker
import csv
import random as rand


#Connection to database
db = mysql.connector.connect(
    host="34.94.182.22",
    user="jroux@chapman.edu",
    passwd="FooBar!@#$",
    database="jroux_db"
)


#Function that will generate the data
def genData():
    fake = Faker()

    #Writing to csv file and generating data
    csv_file = open("./myscrdata.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["CoachName", "AlmaMater", "YearsCoached", "UniversityName", "Address", "TeamSize", "Wins",
                     "Losses", "Ties", "Name", "JerseyNumber", "Year", "Position", "Injured", "Major", "Gpa", "Goals",
                     "Assists", "MinutesPlayedTotal", "GamesPlayedIn"])

    #Lists with specific data created for columns in tables
    position = ["Goalie", "Defender", "Midfielder", "Forward"]
    major = ["Computer science", "Communications", "Business", "History", "Software Engineering", "Biology", "English",
             "Graphic Design", "Music", "Journalism"]
    sciac_teams = ["Chapman", "Redlands", "CalTech", "Whittier", "Cal Lutheran", "Pomona", "Claremont Mckenna",
                   "La Verne", "Occidental"]

    #Writing random data to file with Faker
    for x in range(0, 50):

        position_index = rand.randint(0, 3)
        major_index = rand.randint(0, 9)
        sciac_index = rand.randint(0, 8)
        gpaFloat = round(rand.uniform(1.0, 4.0),2) #Generating random float for gpa

        writer.writerow([fake.name(), fake.company(), fake.random_int(0, 30), sciac_teams[sciac_index],
                         fake.street_address(), fake.random_int(0, 35), fake.random_int(0, 10), fake.random_int(0, 10),
                         fake.random_int(0, 10), fake.name(), fake.random_int(0, 40), fake.random_int(1, 4),
                         position[position_index], fake.random_int(0, 1), major[major_index], gpaFloat,
                         fake.random_int(0, 30), fake.random_int(0, 30), fake.random_int(1000, 1800),
                         fake.random_int(0, 20)])


#Function that normalizes the data
def importData():
    mycursor = db.cursor()

    #Reading in data
    with open("./myscrdata.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:  #Row represents each row in file
            print("importing data")

            mycursor.execute("INSERT INTO Coach(CoachName, AlmaMater, YearsCoached) VALUES (%s, %s, %s);", (row["CoachName"], row["AlmaMater"], row["YearsCoached"]))
            db.commit()

            #Allows for reference to last primary key
            coachReferenceId = mycursor.lastrowid


            mycursor.execute("INSERT INTO Team(CoachId, UniversityName, Address, TeamSize, Wins, Losses, Ties) VALUES (%s, %s, %s, %s, %s, %s, %s);", (coachReferenceId, row["UniversityName"], row["Address"], row["TeamSize"], row["Wins"], row["Losses"], row["Ties"]))
            db.commit()

            teamReferenceId = mycursor.lastrowid

            mycursor.execute("INSERT INTO Player(TeamId, Name, JerseyNumber, Year, Position, Injured) VALUES (%s, %s, %s, %s, %s, %s);", (teamReferenceId, row["Name"], row["JerseyNumber"], row["Year"], row["Position"], row["Injured"]))
            db.commit()

            playerReferenceId = mycursor.lastrowid

            mycursor.execute("INSERT INTO Academics(PlayerId, Major, Gpa) VALUES (%s, %s, %s);", (playerReferenceId, row["Major"], row["Gpa"]))
            db.commit()

            mycursor.execute("INSERT INTO Stats(PlayerId, Goals, Assists, MinutesPlayedTotal, GamesPlayedIn) VALUES (%s, %s, %s, %s, %s);", (playerReferenceId, row["Goals"], row["Assists"], row["MinutesPlayedTotal"], row["GamesPlayedIn"]))
            db.commit()

            print("import successful")

