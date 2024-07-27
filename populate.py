#i have db.sqlite3 i want to get the data of dictionary.csv 
# and transfer that to my homepage_dictionary 
# table each row, row of my table was word.part_of_speech and description


import csv

# Initialize a list to hold the data from CSV
data = []

# Assuming dictionary.csv is in the same directory as this script
csv_file = 'dog_breeds.csv'

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming your CSV has columns word, part_of_speech, description
        Breed = row['Breed']
        Country_of_Origin = row['Country_of_Origin']
        Fur_Color = row['Fur_Color']
        Height_inches = row['Height_inches']
        Color_of_Eyes = row['Color_of_Eyes']
        Longevity_yrs = row['Longevity_yrs']
        Character_Traits = row['Character_Traits']
        Common_Health_Problems = row['Common_Health_Problems']
        image = row['image']

        # Append data as tuples
        data.append((Breed, Country_of_Origin, Fur_Color,Height_inches,Color_of_Eyes,Longevity_yrs,Character_Traits,Common_Health_Problems,image))

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


# Iterate through data and insert into homepage_dictionary table
for row in data:
    Breed, Country_of_Origin, Fur_Color,Height_inches,Color_of_Eyes,Longevity_yrs,Character_Traits,Common_Health_Problems,image = row
    # Assuming your table schema is (word TEXT, part_of_speech TEXT, description TEXT)
    cursor.execute("INSERT INTO mypage_dog (Breed, Country_of_Origin, Fur_Color,Height_inches,Color_of_Eyes,Longevity_yrs,Character_Traits,Common_Health_Problems,image) VALUES (?,?,?,?,?,?,?,?,?)", (Breed, Country_of_Origin, Fur_Color,Height_inches,Color_of_Eyes,Longevity_yrs,Character_Traits,Common_Health_Problems,image))

# Commit changes and close connection
conn.commit()
conn.close()
