<?php
	require_once 'google/appengine/api/users/UserService.php';

	use google\appengine\api\users\User;
	use google\appengine\api\users\UserService;
	
	$user = UserService::getCurrentUser();
	$REDIRECT = 'http://localhost:8080/music';

	if ($user == null){
		header('Location: ' .
					 UserService::createLoginURL($REDIRECT ));
	}
	else
		header('Location: '.$REDIRECT)
?>