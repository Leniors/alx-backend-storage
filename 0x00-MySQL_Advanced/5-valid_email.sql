-- creates a trigger that resets the attribute valid_email only when the email has been changed.
-- Create trigger to reset valid_email attribute when email is changed
DROP TRIGGER IF EXISTS reset_valid_email_on_email_change;
DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		-- Check if the email has been changed
		IF OLD.email != NEW.email THEN
			-- Reset the valid_email attribute to 0 (false)
			SET NEW.valid_email = 0;
		ELSE
			SET NEW.valid_email = NEW.valid_email;
		END IF;
	END;//

DELIMITER ;

