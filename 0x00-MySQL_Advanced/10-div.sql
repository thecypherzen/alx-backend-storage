-- A function that divides (and returns) the first divided by the second number or returns 0 if the second number is equal to 0.
-- Requirements:
--   (1). The function takes 2 arguments:
--        (1). a, INT
--        (2). b, INT
--   (2). returns a / b or 0 if b == 0

DROP FUNCTION IF EXISTS safediv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF b = 0 THEN
       RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END $$
DELIMITER ;
