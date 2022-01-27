# Python-Audio-Converter
A Simple Python CLI Audio Converter, that can convert audio files from/to FLAC, M4A, MP2, MP3, OGG, and WAV.

# Requirements
* pydub
* ffmpeg

# Instructions
Clone this repository "git clone https://github.com/ParamonPlay2205/Python-Audio-Converter/"
Install these Python Packages (as listed above) using the commands below.

# Windows:
* pip install -r requirements.txt

# Linux:
* pip3 install pydub
* sudo apt-get install ffmpeg

# Running the program:
When you when this prorgam, you will need to provide a file name in the local directory and a format you want to convert it into.
Example:
* Windows: audio_converter --file [File Name] --new-format [audio file format]
* Windows: python main.py --file [File Name] --new-format [audio file format]
* Linux: python3 main.py --file [File Name] --new-format [audio file format]

If you would like to list the files in the local directory, then run:
* Windows: audio_converter --list files
* Windows: python --list files
* Linux: python3 --list files

If you want to list the formats you want to convert the file into, then run:
* Windows: audio_converter --list formats
* Windows: python main.py --list formats
* Linux: python3 main.py --list formats

# Optional (Windows Only):
If you want to make a portable executable file. Then run "pip install -r optional.txt", to install packages that can be used to make a portable exe file. This will install "pyinstaller" a CLI program that will make convert a python file into a portable executable. If you want a user-friendly alternative,
you can use "auto-py-to-exe" which uses pyinstaller to make a portable executable in a user-friendly way with a GUI. Or you can download an executable from the latest release in the "releases" page.

If you are going to use Pyinstaller, then run
* pyinstaller --onefile audio_conerter.py (saves the python file as a single portable executable).
* pyinstaller audio_converter.py (saves the python file as portable excutable in a directory).
