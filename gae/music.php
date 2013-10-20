<html>
	<body>
<?php
	require_once 'google/appengine/api/users/UserService.php';

	use google\appengine\api\users\User;
	use google\appengine\api\users\UserService;
	
	// echo "Hello World";

	$user = UserService::getCurrentUser();

    if ($user) {
        echo '<pre>Hello, ' . htmlspecialchars($user->getNickname());
      	
      	if (array_key_exists('content', $_POST)) {
        	echo "</br></br>You wrote:</pre><pre>\n";
        	echo htmlspecialchars($_POST['content']);
        	echo "\n</pre>";
        }
        	echo <<<END
<form action="/music" method="post">
<div><textarea name="content" rows="3" cols="60"></textarea></div>
<div><input type="submit" value="Sign Guestbook"></div>
</form>
</body>
</html>
END;
    }
    else {
    	echo 'Not logged in to your google account';
    }

?>