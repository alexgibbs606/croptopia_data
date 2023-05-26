from private import CROPTOPIA_WORKSPACE
from csv import DictWriter

FOOD_LEVELS = []
HUNGER_FILE = CROPTOPIA_WORKSPACE + r'\Croptopia\shared\src\main\java\com\epherical\croptopia\util\FoodConstructor.java'



with open(HUNGER_FILE, 'r', encoding='utf-8') as foodFile:
	content = foodFile.read().split('public record FoodConstructor(int hunger, float satMod) {', 1)[1].split('public static FoodProperties.Builder createBuilder')[0]
	for data in [_.strip() for _ in content.strip().split('\n')]:
		code = data.split('=')[0].strip().split(' ')[-1]
		hunger, saturation = data.split('(')[1].strip().split(')')[0].strip().split(',')
		FOOD_LEVELS.append({
			'code': code,
			'hunger': int(hunger),
			'saturation': float(saturation[:-1])
		})

with open(r'./foodLevels.csv', 'w', encoding='utf-8') as outFile:
	writer = DictWriter(outFile, FOOD_LEVELS[0].keys(), lineterminator='\n')
	writer.writeheader()
	for record in FOOD_LEVELS:
		writer.writerow(record)
