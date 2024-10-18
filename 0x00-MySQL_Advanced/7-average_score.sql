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

CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE totalScores, projectCount, subTotal INT DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE c_cursor CURSOR FOR
        SELECT SUM(score)
        FROM holberton.corrections
        WHERE user_id = p_user_id
        GROUP BY project_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN c_cursor;
    sumLoop: LOOP
        FETCH c_cursor INTO subTotal;
        IF done THEN
            LEAVE sumLoop;
        END IF;
        SET projectCount = projectCount + 1;
        SET totalScores = totalScores + subTotal;
    END LOOP;
    CLOSE c_cursor;

    UPDATE users
        SET average_score = ROUND(totalScores/projectCount)
        WHERE id = p_user_id;
END $$

DELIMITER ;
