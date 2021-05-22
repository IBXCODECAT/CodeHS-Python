"""
This program asks the user for the building name and room number then outputs 
an abbreviation that identifies the room by taking the first two letters of the
building name, and concatenating it with the room number.
"""

building_name = input("Building name: ")

room_number = input("Room number: ")

abbreviation = building_name[:2] + room_number
print abbreviation