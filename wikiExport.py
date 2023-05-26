'''

Looks like we're gonna need something a little more powerful than sql to export this for the wiki as I want to export information for the graphics as well.

That doesn't mean that I'm going to be incredibly lazy about it tho. Instead of connecting to the server, I'm just gonna read in the final data csv that we've already exported...
'''

from csv import DictReader
from private import CROPTOPIA_WORKSPACE

TABLE_NAME = 'Croptopia Items'

with open(CROPTOPIA_WORKSPACE + r'\wiki\finalData.wiki', 'w', encoding='utf-8') as outFile:
    outFile.write(f'{{| class="sortable mw-collapsible mw-collapsed wikitable"\n|+ {TABLE_NAME}\n')

    with open(CROPTOPIA_WORKSPACE + r'\wiki\finalData.csv', 'r', encoding='utf-8') as inFile:
        reader = DictReader(inFile)
        header = reader.fieldnames.copy()
        header.insert(1, 'icons')
        outFile.write('|' + '\n|'.join(header) + '\n')
        for item in reader:
            outFile.write('|-\n')
            outFile.write(f'|[[{item["name"]}]]\n')
            outFile.write(f'|{{{{Empty Grid|{item["name"].lower()}}}}}\n')
            outFile.write(f'|{item["source"]}\n')
            outFile.write(f'|{item["category"]}\n')
            if item.get('hunger') is not None:
                outFile.write(f'|{{{{Hunger|{item["hunger"]}}}}}\n')
            else:
                outFile.write('|\n')
            if item.get('saturation') is not None:
                outFile.write(f'|{{{{saturation|{item["saturation"]}}}}}\n')
            else:
                outFile.write('|\n')
        outFile.write('|}')