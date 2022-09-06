-- lists all records of the table with name value
-- Records should be listed by descending score

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
