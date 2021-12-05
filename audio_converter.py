"""
Audio File Converter

Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.9.0 (64-Bit)

Description:
This is a Python Program, that can convert audio files from/to MP2, MP3, M4A, FlAC, OGG, and WAV.
"""

# Used for checking if the file exists in the local directory.
import os

# Used for converting the audio file in the local directory.
from pydub import AudioSegment

print("\nAudio File Converter: [flac, m4a, mp2, mp3, ogg, wav]\n")

# This will contain the file name
file = ""

selecting_file = True

while selecting_file:

    # Prompts user to enter an audio file in the local directory
    file = input("Enter the file you wish to convert: ")
    
    # Splits 'file' to store the old file name and old format into 2 sepreate strings.
    name = file.split(".")
    file_name = name[0]
    old_format = name[1]
    old_file = file

    # If the file does exist, then it will break the while-loop
    if os.path.isfile(file) == True:
        selecting_file = not selecting_file

    # If the file does not exist, then it will tell the user to re-enter the file name.
    else:
        print("'" + file + "' does not exist\n")

# Prompts the user to enter a new audio file format
new_format = input("Enter the file format to convert to: ")

# While-loop that will prompt the user for the new audio format.
checking_format = True
while checking_format:

    # If the user enters 'mp2' as the new audio file format,
    # then it will break the loop.
    if new_format.lower() == "mp2":
        checking_format = False
    
    # If the user enters 'mp3' as the new audio file format,
    # then it will break the loop.
    elif new_format.lower() == "mp3":
        checking_format = False

    # If the user enters 'm4a' as the new audio file format,
    # then it will break the loop.
    elif new_format.lower() == "m4a":
        checking_format = False
    
    # If the user enters 'ogg' as the new audio file format,
    # then it will break the loop.
    elif new_format.lower() == "ogg":
        checking_format = False

    # If the user enters 'flac' as the new audio file format,
    # then it will break the loop.
    elif new_format.lower() == "flac":
        checking_format = False
    
    # If the user enters 'wav' as the new audio file format,
    # then it will break the loop.
    elif new_format.lower() == "wav":
        checking_format = False

    # if the user entered an invalid audio file format,
    # then they will be prompted again until they enter a valid format.
    else:
        print("Invalid File Format!\n")
        new_format = input("Enter the format to convert to: ")

print("\nConverting File...\n")

# These will make the converted file name with the new format.
convert = AudioSegment.from_file(file=old_file)
converted_format = file.replace(old_format, new_format)
converted_file = file_name + "." + new_format

# This will convert the audio from its old format to a new format.
convert.export(converted_file, format=new_format)
print("File Converted Successfully!")

# Infinite While-Loop
while True:

    # prompts the user to enter 'Y' or 'N', if they want the previous file to be deleted.
    choice = input("Would you like to delete your previous file (Y/N)? ")

    # If te user enters 'Y', then it will delete the previous file.
    if choice.upper() == "Y":
        os.remove(old_file)
        break

    # If the user enters 'N', then it will end the program.

    elif choice.upper() == "N":
        break

    # If the user enters invalid input, then it will re-prompt the user for their choice until they neter valid input.
    else:
        continue
