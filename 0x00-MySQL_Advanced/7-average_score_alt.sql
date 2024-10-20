-- Creates a stored procedure `ComputeAverageScoreForUser`
--   that computes and stores the average score for a student.
--   Note: An average score can be a decimal
-- Requirements:
--   1. Procedure `ComputeAverageScoreForUser` is taking 1 input:
--      `user_id`, a users.id value (assumes `user_id` is linked
--      to an existing users entry)

-- the procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN userId INT)
BEGIN
    DECLARE totalScores, projectCount, subTotal INT DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE currentProjectId INT;
    DECLARE c_cursor CURSOR FOR
        -- get sum of scores by project for user
        SELECT project_id, SUM(score)
        FROM holberton.corrections
        WHERE user_id = userId
        GROUP BY project_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN c_cursor;
    sumLoop: LOOP
        -- fetch row from cursor
        FETCH c_cursor INTO currentProjectId, subTotal;
        IF done THEN
            LEAVE sumLoop;
        END IF;
        SET projectCount = projectCount + 1;
        SET totalScores = totalScores + subTotal;
        SELECT currentProjectId, subTotal, totalScores;
    END LOOP;
    CLOSE c_cursor;
    -- set user's average score
    UPDATE users
        SET average_score = totalScores/projectCount
        WHERE id = userId;
END $$

DELIMITER ;
