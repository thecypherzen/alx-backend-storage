-- Lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- Column names must be: `band_name` and `lifespan`
-- (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
--     Uses attributes `formed` and `split` for computing the lifespan
-- Can be executed on any database

-- the script itself
SELECT band_name, COALESCE(split, 2022) - formed AS 'lifespan'
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY 2 DESC;
