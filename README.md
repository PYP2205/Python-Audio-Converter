# Python-Audio-Converter
A Simple Python CLI Audio Converter, that can convert audio files from/to FLAC, M4A, MP2, MP3, OGG, and WAV.

# Requirements
* pydub
* ffmeg

# Instructions
Clone this repository "git clone https://github.com/ParamonPlay2205/Python-Audio-Converter/"
Install these Python Packages (as listed above) using the commands below.

# Windows:
* pip install -r requirements.txt

# Linux:
* pip3 install pydub
* sudo apt-get ffmeg

# Optional (Windows Only):
If you want to make a portable executable file. Then run "pip install -r optional.txt", to install packages that can be used to make a portable exe file. This will install "pyinstaller" a CLI program that will make convert a python file into a portable executable. If you want a user-friendly alternative,
you can use "auto-py-to-exe" which uses pyinstaller to make a portable executable in a user-friendly way with a GUI.

If you are going to use Pyinstaller, then run
* pyinstaller --onefile audio_conerter.py (saves the python file as a single portable executable).
* pyinstaller audio_converter.py (saves the python file as portable excutable in a directory).
