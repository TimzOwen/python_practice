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



-- calculate the avarage of population
SELECT ROUND(AVG(POPULATION)) FROM CITY;


-- AVG OF POPULATION FROM SPECIFIC CITY
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'CALIFORNIA'



--total score of an contest

--soln
select h.hacker_id, name, sum(score) as total_score
from
hackers as h inner join
/* find max_score*/
(select hacker_id,  max(score) as score from submissions group by challenge_id, hacker_id) max_score

on h.hacker_id=max_score.hacker_id
group by h.hacker_id, name

/* don't accept hackers with total_score=0 */
having total_score > 0

/* finally order as required */
order by total_score desc, h.hacker_id
;


-- query with name ending with voewls 
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','e','i','o','u');  --my sql
SELECT DISTINCT(CITY) FROM STATION WHERE CITY LIKE '%[AEIOU]'; ---> ms mysql server 

-- starts and ends in vowels
SELECT DISTINCT(CITY) FROM STATION WHERE LEFT(CITY,1) IN ('a','e','i','o','u') and RIGHT (CITY,1) IN ('a','e','i','o','u');

-- does not start with vowels
SELECT DISTINCT(CITY) FROM STATION WHERE CITY REGEXP '^[^a,e,i,o,u]';