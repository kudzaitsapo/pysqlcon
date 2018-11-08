IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='$tablename' AND xtype='U')
BEGIN
	CREATE TABLE $tablename (
		$properties
	)
END