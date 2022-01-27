"""
convert

Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.9.7 (64-Bit)

Description:
This Python Library is used for converting
the audio files given by the user to a different
format that is also given by the user.
"""
    
# used for converting audio files.
def audio_file(file_name, new_format):
    
    try:
        # Used for converting audio files into another format
        from pydub import AudioSegment

        # Converts the file name into a string value
        file_name = str(file_name)

        # Splits the audio file name into two values.
        audio_file, old_format = file_name.split(".")

        # Makes a converter
        convert = AudioSegment.from_file(file_name)

        # Replaces the old audio format into a new format given by the user.
        file_name = file_name.replace(old_format, new_format)

        # Converts the file into a new format
        convert.export(file_name, format=new_format)
    
    # If any exception is raised, then it will show the user what exception was raised.
    except Exception as error:
        print(f"\nError: {error}")
