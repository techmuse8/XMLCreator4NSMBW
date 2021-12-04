# XMLCreator4NSMBW
A fork of a python program that builds a New Super Mario Bros. Wii (NSMBW) Riivolution XML file for you.

Originally forked from the release build at https://github.com/EterSky/XMLCreator
# Features
- Makes an XML with support for a single recursive directory where the user can add their replaced files
- savegame redirection to the SD Card
# Supported Versions
So far, only tested on the US version and briefly tested on the EUR version. Untested on the JPN version but should work. No support for the KOR or TWN versions at this time but may come later. CHN support is probably a hard no.

# How to run

## Requirements
- Python 3 installed. Download here: https://www.python.org

In a terminal window, run `python3 XMLCreatorNSMBW.py` (`py -3` in substitute of `python3` on Windows) and follow the on screen instructions.
You can then use the generated XML with Riivolution and HLE Riivolution on Dolphin.

# Credits
- [EterSky](https://github.com/EterSky): making the original XMLCreator
- [techmuse8](https://github.com/techmuse8): (myself) of course and testing all of this
- [Danster64](https://github.com/Danster64): suggesting the order of the NSMBW folders (for  1.0.0)
- [Asu-chan](https://github.com/Asu-chan): suggesting the recursive directory XML line to save a huge amount of XML lines and more simplicity.
