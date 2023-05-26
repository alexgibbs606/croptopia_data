Wanted to have a list of all croptopia items and their hunger/saturation values.

Croptopia is a public repository, so I pulled it down from `https://github.com/ExcessiveAmountsOfZombies/Croptopia`.

Adjacent to the repository, I placed this repository, and pointed the value in `private.py` to both the repository's parent folder.

The food level parser needs to be run before the items parser. Some values for hunger codes had to be manually pulled from files in `Croptopia\shared\src\main\java\com\epherical\croptopia\register\helpers`.

Both these scripts export to .csv files. I loaded them into mysql and did some data checking to make sure I didn't miss any food, then joined on the hunger code to make a master table.

If you want this data as well, you'll need to change the path in `private.py`.