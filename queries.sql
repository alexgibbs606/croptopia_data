-- Updating all empty hunger values
UPDATE items
SET hungerCode = NULL
WHERE hungerCode = '';

-- Confirming all items that shouldn't have a hunger value. This helps me confirm that I didn't miss a food.
SELECT *
FROM items
WHERE hungerCode IS NULL
	AND source <> 'Utensil' -- Filtering out Utensils
	AND source NOT LIKE '%block%' -- Filtering out salt and salt ore
	AND source NOT LIKE 'Tree%' -- Filtering out Apple crop and Cinnamon
;

SELECT REPLACE(i.name, '_', ' ') as name
	, i.source, i.category, f.hunger
	, f.saturation
FROM items i
LEFT JOIN foodlevels f
	ON i.hungerCode = f.code
WHERE source <> 'Utensil' -- Filtering out Utensils
	AND source NOT LIKE '%block%' -- Filtering out salt and salt ore
	AND source NOT LIKE 'Tree%' -- Filtering out Apple crop and Cinnamon
;