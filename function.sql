DELIMITER $$

CREATE FUNCTION det_don(date_of_Donation date)
DETERMINISTIC
BEGIN
	SELECT Donor_ID, organ_donated FROM donor WHERE date_of_Donation = date_donation;
END; $$

DELIMITER ;
