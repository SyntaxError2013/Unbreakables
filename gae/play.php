<html>
	<body>
<?php
	require_once 'google/appengine/api/users/UserService.php';

	use google\appengine\api\users\User;
	use google\appengine\api\users\UserService;

    $db = mysqli_connect("localhost", "monty", "12345678");

    $query = "USE db";
    mysqli_query($db, $query);

	$user = UserService::getCurrentUser();

    if ($user) {
        echo '<pre>Hello, ' . htmlspecialchars($user->getNickname());
        echo '<div>';
      	
        $query = "SELECT * FROM madfrets";
        $result = mysqli_query($db, $query);

        while($row = mysqli_fetch_array($result)){

$pine = "upload/" . $row[2];
echo <<<END
<div>
<a href = "$pine">$row[2]</a></div>
END;
//             echo $row[0]." ".$row[2];
        }
        echo '</div>';
    }
//         echo <<<END
// <form action="/music" method="post">
// <div><textarea name="content" rows="3" cols="60"></textarea></div>
// <div><input type="submit" value="Sign Guestbook"></div>
// </form>
// </body>
// </html>
// END;
    else {
    	echo 'Not logged in to your google account';
    }

?>

</body> </html>