<a href="https://paypal.me/benckx/2">
<img src="https://img.shields.io/badge/Donate-PayPal-green.svg"/>
</a>

# About

Quick and dirty Python script to copy ROMs files from local folder to mounted SD card (to be placed in handheld retro
consoles, such as the Anbernic RG351M).

Compare the source and target folder and output a list of `rsync` commands, one for each file that exists in the source
folder, but not in the target folder. Files are filtered by extension (to avoid confusion with saved states). The script
only adds files.
