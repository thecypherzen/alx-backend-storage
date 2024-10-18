-- Creates a trigger that resets the attribute
--   `valid_email` only when the email has been changed.

-- the triggeri
DROP TRIGGER IF EXISTS ReValidateEmail;

DELIMITER $$

CREATE TRIGGER ReValidateEmail
BEFORE UPDATE on users
FOR EACH ROW

BEGIN
    IF OLD.email != NEW.email THEN
       SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER ;
