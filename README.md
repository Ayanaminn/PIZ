# PIZ
PIZ (Programmble Interface for Zebrafish Sensor-motor Biotest)

PLS is an open-source, programmable interface for sensory-motor biotests with zebrafish (Danio rerio). The interface includes software and hardware component that enables automated delivery of three independent and fully programmable stimuli behavioral bioassays. 


![gui](https://github.com/Ayanaminn/PIZ/assets/49441654/66d14120-6b41-48ed-b8c8-c47b91b44a06)



**Please cite our manuscript:**

Coming Soon

&nbsp;


PIZ is a prototype program that first wrote in C# then remake in Python. An advanced version with improved features is now available under [NeuroBox](https://github.com/Ayanaminn/NeuroBox) project.


Installation:
------------
### Requirements

* Windows operating system.


### Software

1. Download the latest release from [Releases](https://github.com/Ayanaminn/PIZ/releases).

2. Unzip file and double click to run "PIZ.exe".


### Hardware

1. Download the latest release from [Releases](https://github.com/Ayanaminn/PIZ/releases).

2. Unzip file and open "PIZ_Arduino" folder.

3. Using [Arduino IDE](https://www.arduino.cc/en/software) to open the "PIZ_Arduino.ino" and upload it to board.

4. Wire LED circuit to Arduino pin 8, 9 10 (default pin), if user prefer to use other pins, change pin number in the script accordingly and re-upload.


Getting Started:
------------

1. Connect the Arduino with the computer.

2. Run the programm, select the Arduino port, then click "Connect".

3. Set protocols.

4. Disconnect the Arduino before exit the program.


License:
------------

GPL-3.0 License. See [LICENSE](https://github.com/Ayanaminn/PIZ/blob/master/LICENSE) for details.


Contact:
------------

Should you have any questions about this application, please report an issue [here](https://github.com/Ayanaminn/PIZ/issues), or send an [email](mailto:yutao.bai@hotmail.com).

If you have further interests about the research this program has been applied for, please [visit our website](https://neurotoxlab.com).
