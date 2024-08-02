# Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning, 
# but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to recommend 
# additional things like "audio system" or "projector" based on the number of attendees.

audio_system = "UE Boom" if attendees < 20 else "Dolby"
projector = "imax" if attendees > 150 else "that old projector in storage"
print(f"use {audio_system} for audio & for the screen use {projector}")


# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

catering_preference = input("would you like vegetarian food (yes/no)? ")
print("we recommend Veggie Delight Caterers" if catering_preference == "yes" else "we recommend Gourmet Meals Caterers")
