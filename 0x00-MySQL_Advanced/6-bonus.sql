-- Creates a stored procedure AddBonus that adds a new
--     correction for a student.
-- Requirements:
--   1. Procedure `AddBonus` is taking 3 inputs (in this order):
--      i. `user_id`: a `users.id` value
--            (assumes `user_id` is linked to an existing user)
--      ii. `project_name`: a new or already existing project.
--           - if no projects.name found in the table,
--             it is created
--      iii. `score`: the score value for the correction

-- the stored procedure itself

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT,
       IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    DECLARE projectId INT DEFAULT NULL;
    -- get project_id if project already exists
    SELECT id INTO projectId FROM projects WHERE name = project_name;
    IF projectId IS NULL THEN
       INSERT INTO projects(name) VALUES(project_name);
       SET projectId = LAST_INSERT_ID();
    END IF;
    -- add correction for student
    INSERT INTO corrections(user_id, project_id, score)
    VALUES (user_id, projectId, score);
END $$

DELIMITER ;
