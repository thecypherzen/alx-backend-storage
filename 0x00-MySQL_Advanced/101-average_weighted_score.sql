-- Creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students.
-- Requirements:
--   (1). Procedure takes in no inputs

-- the procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    UPDATE users,
        (SELECT user_id,
            SUM(weight) AS 'wsum',
            SUM(score * weight) AS 'wscores'
        FROM projects
             JOIN corrections
             ON project_id = projects.id
        GROUP BY user_id
        ) as weighted_table

    SET average_score = wscores / wsum
        WHERE users.id = weighted_table.user_id;
END $$

DELIMITER ;
