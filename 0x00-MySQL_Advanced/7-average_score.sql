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
    DECLARE average FLOAT DEFAULT 0;
    SELECT AVG(score) INTO average
    FROM corrections
    WHERE user_id = userId;
    -- set user's average score
    UPDATE users
        SET average_score = average
        WHERE id = userId;
END $$

DELIMITER ;
