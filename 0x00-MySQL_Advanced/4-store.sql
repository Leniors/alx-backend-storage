-- creates a trigger that decreases the quantity of an item after adding a new order
-- Create trigger to decrease quantity after adding a new order
DELIMITER //
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		-- Update the quantity of the corresponding item in the items table
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END;//
DELIMITER ;

