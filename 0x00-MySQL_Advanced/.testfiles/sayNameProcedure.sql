DROP PROCEDURE IF EXISTS sayName;

DELIMITER $$

CREATE PROCEDURE sayName(IN user_id INT, OUT user_name VARCHAR(255))
BEGIN
    DECLARE userName VARCHAR(255) DEFAULT NULL;
    SELECT name INTO userName FROM users WHERE id = user_id;
    IF userName IS NULL THEN
       SET userName = 'USER DOES NOT EXITS EXIST';
    END IF;
    SELECT LAST_INSERT_ID();
    SET user_name = userName;
END $$

DELIMITER ;
