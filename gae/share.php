<?php
	echo "Hello World";

	$db = mysqli_connect("localhost", "root", "rotator");

	$query = "USE db";
	mysqli_query($db, $query);


if ($_FILES["file"]["error"] > 0)
 	echo "Error: " . $_FILES["file"]["error"] . "<br>";
else{
	if(count($_FILES) > 0){
		echo "Upload: " . $_FILES["file"]["name"] . "<br>";
		echo "Type: " . $_FILES["file"]["type"] . "<br>";
		echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
		echo "Stored in: " . $_FILES["file"]["tmp_name"];

		$query = "INSERT INTO abc VALUES ('5')"
		mysqli_query($db, $query);

		if (file_exists("upload/" . $_FILES["file"]["name"]))
    		echo $_FILES["file"]["name"] . " already exists. ";
    	else{
		move_uploaded_file($_FILES["file"]["tmp_name"],
			"upload/" . $_FILES["file"]["name"]);
			echo "Stored in: " . "upload/" . $_FILES["file"]["name"];
		}
	}
}

?>
