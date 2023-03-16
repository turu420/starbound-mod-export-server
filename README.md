# Starbound Steam Server export Mods into Mod Folder


If you want to create a starbound Server with mods there is the problem of exporting 
a lot of mods from your steam library into you dedicated Server. In normal case you
have to rename every mod from "contents.pak" into its folders name. But if you have more than 10 Mods it
can be really painfull to do that by yourself, so I created this Skript which makes that automaticly.
It scans for all folders inside the skript running directory and copies the pak file into the export folder with the name of its orginal folder. Run the Skript and just copy and paste the output inside the server mod folder and you are good to go c:



# HOW TO USE THIS SCRIPT
1. Install any Python 3 Version
2. copy "exportMods.py" into "SteamLibrary\steamapps\workshop\content\211820"
3. create "export" Folder in "SteamLibrary\steamapps\workshop\content\211820"
4. Run CMD inside "SteamLibrary\steamapps\workshop\content\211820"
5. run "python exportMods.py"
6. Wait
7. Your renamed mods will be in export


Hope I saved your time <3

# Questions?

Just send me a message