# dumpmon_tweeter_scraper
This script monitors the Dumpmon Bot Twitter page, (https://twitter.com/dumpmon, written by Jordan Wright) and saves the pastes posted by it.

This script was written and tested in Windows 7 x64 using Python v2.7.11 win32.

Usage is simple, ensure that Python 2.7.11 is installed on your machine, then run the script. It will prompt you for an output path.
The output path is where the pastes and checked paste log goes.

The script is meant to be run passively over time and uses randint timers to space out your page grabs, in an effort to reduce stress and traffic to Twitter/Pastebin/etc domains involved.

The script was quickly created with a very singular purpose in mind. I am not to enthralled with the prospect of reviewing the code of the existing Pastebin dump monitor bots out there, and figured I could just write this little script to quick, concisely, and dirtyishly grab data of potential interest.

Please reach out to me with any questions, concerns, thoughts, etc.
