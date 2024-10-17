-- ranks country origins of bands, ordered by the number of
-- (non-unique) fans
-- Requirement:
--    1. Column names must be: origin and nb_fans
--    2. Script is executable on any database

-- the script itself
SELECT origin, SUM(fans) AS 'nb_fans'
FROM metal_bands
GROUP BY 1
ORDER BY 2 DESC;
