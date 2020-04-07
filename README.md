Pi Radio

Transmit audio files (.wav or .mp3) via FM and listen to your music anywhere near you!

--------------
Requirements
--------------

Things you'll need:
A Raspberry Pi
An Antenna

-------------
Instructions
-------------

Using the program is simple!  
Install PiFM and other required software by running the install.py:
<code>sudo python3 ./install.py</code>  

Proceed to run the file Pi Radio: 
<code>sudo python3 ./pi_radio.py</code>  

After the program is up and running you will be asked to enter default values for highest, lowest and default audio directory.If you do not wish to enter these values; default values will be used.You can can these later in the Settings option in top menu.

Then in the main menu, select the audio file by clicking the select button next to 'File:' and selecting the file via the dialog box; your selected file's name will be displayed.Enter the frequency at which you want to air the song in the entry below.In the end, click play button.

-----
About 
-----

The code used in the program is <code>ffmpeg -i input.mp3 -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - 99.9</code> for MP3's and <code>sudo ./pifm left_right.wav 103.3 22050 stereo</code> for WAV files.  The program will automatically decide weather to play it as a WAV or MP3 file.  As of now, these are the only two files supported. 

WAV files must be in the following format: 16 bit (mono or stereo) 22050 hz (generaly these are fine as-is, but you may need to convert it if it doesn't mach the required specs.)  Anything below 16 bits will work as well.

The Raspberry Pi can handle anywhere from 1MHz to 250MHz, however I limited it in the code to 80.0 and 108.0  by default beacuse generaly radio bands don't go past these numbers.You can change this by using the settings menu.
You can use the Frequency Reference option to find radio frequency restrictions in your local area.

Inspired by CodyJHeiser's PiStation
More here :

http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter

--------------

I am still a very amateur programmer, and still have a lot to learn, so any help would be awesome!

