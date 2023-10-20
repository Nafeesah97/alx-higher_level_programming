-- lists all the cities of California
SELECT id, name
	FROM cities
	WHERE state_id = (
		SELECT id
		WHERE name = 'California'
		LIMIT 1)
	ORDER BY id;
