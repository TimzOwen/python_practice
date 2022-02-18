-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
-- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

--SOLN 

(SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY ASC LIMIT 1) UNION 
(SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) ASC, CITY ASC LIMIT 1);




-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

-- SOLN  -> starts with vowels 
select DISTINCT city from station where city REGEXP "^[aeiou].*";

--SOLN -> starts and ends with vowels
SELECT DISTINCT CITY 
FROM STATION  
WHERE CITY LIKE '[AEIOU]%' and CITY LIKE '%[aeiou]';

--SOLN ->starts and ends with vowel
SELECT DISTINCT CITY 
FROM STATION  
WHERE CITY regexp '^[AEIOU]%' and CITY regexp '[aeiou]$';



