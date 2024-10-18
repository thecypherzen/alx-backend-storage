-- Creates a trigger that decreases the quantity of an
-- item after adding a new order.
-- `Quantity` in the table `items` can be negative.

-- the trigger

DROP TRIGGER IF EXISTS newOrder;

DELIMITER $$
CREATE TRIGGER newOrder
AFTER INSERT ON orders
FOR EACH ROW

BEGIN
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$

DELIMITER ;
