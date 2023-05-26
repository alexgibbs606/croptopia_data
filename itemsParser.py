from private import CROPTOPIA_WORKSPACE
from csv import DictReader, DictWriter

ITEMS_FILE = CROPTOPIA_WORKSPACE + r'\Croptopia\shared\src\main\java\com\epherical\croptopia\register\Content.java'
FOOD_LEVELS_FILE = CROPTOPIA_WORKSPACE + r'\wiki\foodLevels.csv'
ITEMS_OUT_FILE = CROPTOPIA_WORKSPACE + r'\wiki\items.csv'

MANUAL_CODE_MAP = {
	'IceCream': 'REG_10',
	'Jam': 'REG_3',
	'Juice': 'REG_5',
	'Pie': 'REG_14',
	'Smoothie': 'REG_7',
}

# Getting a list of our possible hunger profiles
FOOD_CODES = []
with open(FOOD_LEVELS_FILE, 'r', encoding='utf-8') as foodLevels:
	reader = DictReader(foodLevels)
	for row in reader:
		FOOD_CODES.append(row['code'])


with open(ITEMS_FILE, 'r', encoding='utf-8') as inFile:
	# Opening our output file at the same time
	with open(ITEMS_OUT_FILE, 'w', encoding='utf-8') as outFile:
		# Opening a dictionary writer
		itemsWriter = DictWriter(outFile, [
			'name', 'source', 'hungerCode', 'category'
		], lineterminator='\n')
		itemsWriter.writeheader()

		# Gathering the useful content from our content file
		file = inFile.read().split('public class Content {')[1].split('public static Item GUIDE;')[0]
		# Iterating through each file
		for line in file.split('\n'):
			record = {}
			# Checking if this line is empty or commented
			line = line.strip()
			if line[0:2] == '//' or len(line) < 1 :
				continue

			# Grabbing some easy access information
			# print(line)
			source, name = line.split('=')[0].strip().split(' ')[-2:]
			altSource = line.split('=', 1)[1].split('(')[0].strip().split(' ')[-1]
			record['name'] = name.strip().title()
			record['source'] = altSource if source == 'Item' else source
			# Grabbing the arguments for the food creation
			args = [_.strip() for _ in line.split('(', 1)[-1].rsplit(')', 1)[0].split(',')]

			if args[0][:14] == 'createGroup().':
				for code in FOOD_CODES:
					if code in args[0]:
						record['hungerCode'] = code

			# Parsing arguments if valid
			for arg in args:
				# Getting our food code for the hunger/saturation profile
				if arg in FOOD_CODES:
					record['hungerCode'] = arg

				if arg.split('.')[0] == 'TagCategory':
					record['category'] = arg.split('.')[1].title()

			# Manually mapping some food types to their hungerCode
			# Typically from files in Croptopia\shared\src\main\java\com\epherical\croptopia\register\helpers
			if record.get('hungerCode') is None:
				record['hungerCode'] = MANUAL_CODE_MAP.get(record['source']) or None

			# We're finished parsing this record, lets write it to the file
			print(f'writing {record["name"]}')
			itemsWriter.writerow(record)