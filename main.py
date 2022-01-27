"""
Python Audio Converter

Programmed by: Paramon yevstigneyev
Programed in: Python 3.9.7 (64-Bit)

Description:
This is a Python Program, that can convert Audio files into any other common
format (MP2, MP3, M4A, OGG, FLAC, WAV) you want to.
"""

# Used for checking if the audio file does exist,
# and to remove the old file from the user's system.
import os
# Sued for command line arguments when the user runs the file
import argparse

 # Used for converting the audio file into a new format
import convert

# Makes a parser to 
parser = argparse.ArgumentParser(description="A Python Audio Converter program")

# Adds a '--file' argument for the use to specify the existing audio file
parser.add_argument("--file", "--file", help="Name of the audio file to convert.")
# Adds a '--new-format' argument, for the user to specify an audio format they want to convert it into.
parser.add_argument("--new-format", "--new_format", help="Specify new audio file format.")

# Adds a '--list-formats' argument, for the user to see the local files and audio file formats.
parser.add_argument("--list","--list", help="Lists audio file formats or local audio files.")

args = parser.parse_args()

def convert_file():
    if args.list != "" and args.list != None:

        if args.list == "files":
            print("\nLocal Files:")

            local_files = os.listdir()

            for audio_files in local_files:
                
                if "m4a" in audio_files:
                    print(audio_files)

                elif "mp2" in audio_files:
                    print(audio_files)

                elif "mp3" in audio_files:
                    print(audio_files)

                elif "ogg" in audio_files:
                    print(audio_files)

                elif "flac" in audio_files:
                    print(audio_files)

                elif "wav" in audio_files:
                    print(audio_files)

                else:
                    pass

            print()

        elif args.list == "formats":
            audio_formats = ["flac", "mp2","mp3", "m4a", "ogg", "wav"]
            print("\nAudio file formats:")

            for formats in audio_formats:
                print(formats)

            print()

        else:
            pass

    elif args.file != "" and args.file != None:
        # If the user enters a file that does exist in the local directory,
        # then it will 
        if os.path.isfile(args.file):

            # If the user enter 'mp3' as a new file format, then it will convert
            # the given file into an mp3 file.
            if args.new_format == "mp3":
                convert.audio_file(args.file, args.new_format)

            # If the user enter 'm4a' as a new file format, then it will convert
            # the given file into an m4a file.
            elif args.new_format == "m4a":
                convert.audio_file(args.file, args.new_format)

            # If the user enter 'mp2' as a new file format, then it will convert
            # the given file into an mp2 file.
            elif args.new_format == "mp2":
                convert.audio_file(args.file, args.new_format)
            
            # If the user enter 'flac' as a new file format, then it will convert
            # the given file into an flac file.
            elif args.new_format == "flac":
                convert.audio_file(args.file, args.new_format)

            # If the user enter 'ogg' as a new file format, then it will convert
            # the given file into an ogg file.
            elif args.new_format == "ogg":
                convert.audio_file(args.file, args.new_format)
            
            # If the user enter 'wav' as a new file format, then it will convert
            # the given file into an wav file.
            elif args.new_format == "wav":
                convert.audio_file(args.file, args.new_format)

            # If the user enters an invalid audio format, then it will
            # tell the user that it was an invalid format.
            else:
                print("\nInvalid file format!\n")

        # If the user enters a file name that does not exist,
        # or can not be found. It will show that the file was not found.
        else:
            print(f"\n'{args.file}' not found!\n")

try:
    convert_file()

# If the "KeyboardInterrupt" exception is raised,
# then this will prevent the program from raaising this exception.
except KeyboardInterrupt:
    pass

# If any other excpetion is raised then this will
# handle the excpetion when an exception is raised.
except:
    convert_file()
