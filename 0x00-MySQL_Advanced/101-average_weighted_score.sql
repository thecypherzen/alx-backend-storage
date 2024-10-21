-- Creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students.
-- Requirements:
--   (1). Procedure takes in no inputs

-- the procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    DECLARE currentUserId INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE userIdCursor CURSOR FOR
        SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN userIdCursor;
    calUserAvg: LOOP
        FETCH userIdCursor INTO currentUserId;
        IF done THEN
           LEAVE calUserAvg;
        END IF;
        SELECT SUM(weight * score), SUM(weight)
        INTO @weighted_scores, @total_weights
        FROM (
            SELECT corrections.score, projects.weight
            FROM projects JOIN corrections
            ON project_id = projects.id
            WHERE user_id = currentUserId
        ) AS user_weighted_scores;

    UPDATE users
    SET average_score = @weighted_scores / @total_weights
    WHERE id = currentUserId;
    END LOOP;
END $$

DELIMITER ;
