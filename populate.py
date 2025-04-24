import csv
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dog_breed.settings")
django.setup()

from mypage.models import Dog, CharacterTrait, HealthProblem

# Load data from CSV
csv_file = "dog_breeds.csv"

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        breed = row['Breed']
        country_of_origin = row['Country_of_Origin']
        fur_color = row['Fur_Color']
        height_inches = row['Height_inches']
        color_of_eyes = row['Color_of_Eyes']
        longevity_yrs = row['Longevity_yrs']
        image = row['image']
        
        # Create Dog entry
        dog, created = Dog.objects.get_or_create(
            breed=breed,
            defaults={
                "country_of_origin": country_of_origin,
                "fur_color": fur_color,
                "height_inches": height_inches,
                "color_of_eyes": color_of_eyes,
                "longevity_yrs": longevity_yrs,
                "image": image,
            },
        )

        # Add Character Traits (split by comma if multiple traits are in one column)
        character_traits = row['Character_Traits'].split(",") if row['Character_Traits'] else []
        for trait in character_traits:
            CharacterTrait.objects.get_or_create(dog=dog, trait=trait.strip())

        # Add Health Problems (split by comma if multiple issues are in one column)
        health_problems = row['Common_Health_Problems'].split(",") if row['Common_Health_Problems'] else []
        for problem in health_problems:
            HealthProblem.objects.get_or_create(dog=dog, health_problem=problem.strip())

print("Data import completed successfully!")
