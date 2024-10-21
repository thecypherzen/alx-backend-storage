-- Creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and stores the average weighted score for a student.
-- Requirements:
--   (1). Takes 1 input: `user_id`, which is a users.id value (assumes user_id is linked to an existing users)

-- the procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userId INT)
BEGIN
    SELECT SUM(weight * score), SUM(weight)
    INTO @weighted_scores, @total_weights
    FROM (
         SELECT corrections.score, projects.weight
         FROM projects JOIN corrections
         ON project_id = projects.id
         WHERE user_id = userId
    ) AS user_weighted_scores;
    UPDATE users
        SET average_score = @weighted_scores / @total_weights
        WHERE id = userId;
END $$

DELIMITER ;
