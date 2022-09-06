-- lists all records of the table with name value
-- Records should be listed by descending score

SELECT score, name
FROM second_table
WHERE EXISTS (SELECT name FROM second_table)
ORDER BY score DESC;
