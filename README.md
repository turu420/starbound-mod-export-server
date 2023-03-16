# Starbound Steam Server export Mods into Mod Folder


If you want to create a starbound Server with mods there is the problem of exporting 
a lot of mods from your steam library into you dedicated Server. In normal case you
have to rename every mod from "contents.pak" into its folders name. But if you have more than 10 Mods it
can be really painfull to do that by yourself, so I created this Skript which makes that automaticly.
It scans for all folders inside the skript running directory and copies the pak file into the export folder with the name of its orginal folder. Run the Skript and just copy and paste the output inside the server mod folder and you are good to go c:



# HOW TO USE THIS SCRIPT
I know a lot of you guys will have problems to export your mods from your local Starbound Installation to a dedicated Server.
In this Guide I will not tell you how to setup a Server. I just want to help those people who have to manually rename their Mods from their Steam Workshop Folder ("workshop\content\211820\").

I wrote a Python Script that will make the rename process automaticly so you can save time <3.
Step 0:
I assume you have already installed your mods inside the steam workshop page

Step 1:
`Install [url=https://www.python.org/]Python[/url]`
Step 2:
`Grap my Skript on my Github Page [url=https://github.com/turu420/starbound-mod-export-server]Python[/url]`
Step 3:
`Go into your Locale Starbound Workshop Folder (Usually its on SteamLibrary/steamapps/workshop/content/211820)`
Step 4:
`Create a new Folder "export" inside this directory`
Step 5:
`Copy the downloaded "exportMods.py" Script`
Step 6:
`Run CMD inside this folder (SteamLibrary/steamapps/workshop/content/211820)`
Step 7:
`Type "python exportMods.py"`
Step 8:
`Wait ... (It can take longer -> it depends on how many mods you have)`
Step 9:
`If it says "DONE!!!" you can close the CMD`
Step 10:
`You are ready to copy the renamed mods from the export Folder to your dedicated Server via FTP/SFTP`

Hope It was helpful <3


Hope I saved your time <3
