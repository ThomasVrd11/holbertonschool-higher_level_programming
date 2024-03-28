-- TASK : 8
SELECT cities.id, cities.name
FROM cities, states 
WHERE states.name = "California" AND cities.state_id = states.id
ORDER BY cities.id ASC;
