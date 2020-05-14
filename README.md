# Switch-Off

-----

## Problem

* Laptop gets overheated when kept plugged it for a long amount of time at 100%.
* Decrease in battery life.
* This code will alarm you know when you should turn off the switch.
  
-----

* This was just a pet project of me for learning how to play sounds using python and run scripts on startup
* The code was tested on a windows10.

## Updation

**For running on your machine:**

1) Change the battery.bat file accordingly

```.bat
start "" "full\path\to\python_exe\folder\pythonw.exe" "full\path\to\where\script\is\stored\battery_alarm.py"
exit
```

2) Changes in the script file (line 22). full path of .wav file

```python
winsound.PlaySound(r"\full\path\to\sound\file.wav"
      flags=winsound.MB_ICONASTERISK)
```  

## Usage

* Place the battery.bat file in the startup folder
    1) Press: **Win+r**
    2) Type: **shell:startup**
    3) place the batch file in the folder.
