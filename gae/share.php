<?php
	define ('SITE_ROOT', realpath(dirname(__FILE__)));
	$ERROR_UPLOAD = 100;
	$ERROR_ALREADY_EXISTS = 101;
	$ERROR_NO_FILE_SENT = 102;
	$ERROR_MOVE_UPLOADED_FILE_FAILED = 103;
	$SUCCESS = 150;

	if ($_FILES[linkin_park]["error"] == 0)
		if(count($_FILES) > 0)
			if (file_exists("upload/" . $_FILES[linkin_park]["name"]) == false)
				if(move_uploaded_file($_FILES[linkin_park]["tmp_name"],
					SITE_ROOT."/upload/".$_FILES[linkin_park]["name"]))
					echo $SUCCESS;
				else
					echo $ERROR_MOVE_UPLOADED_FILE_FAILED;
			else
				echo $ERROR_ALREADY_EXISTS;
		else
			echo $ERROR_NO_FILE_SENT;
	else
		echo $ERROR_UPLOAD." ".$_FILES[linkin_park]["error"];
?>
