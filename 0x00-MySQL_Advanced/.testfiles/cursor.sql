-- a basic procedure
DROP PROCEDURE IF EXISTS ListCorrection;

DELIMITER $$

CREATE PROCEDURE ListCorrection(IN userId INT)
BEGIN
    DECLARE grade, totalScore, projectId INT DEFAULT 0;
    DECLARE rowCount INT DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE  c_cursor CURSOR FOR
        SELECT project_id, score
        FROM holberton.corrections
        WHERE user_id = userId;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN c_cursor;
    REPEAT
        FETCH c_cursor INTO projectID, grade;
        SET rowCount = rowCount + 1;
        SET totalScore = totalScore + grade;
        SELECT projectId, grade, rowCount;
    UNTIL done = TRUE
    END REPEAT;
    CLOSE c_cursor;
    SELECT totalScore;
END $$

DELIMITER ;
