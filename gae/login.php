<?php
	require_once 'google/appengine/api/users/UserService.php';

	use google\appengine\api\users\User;
	use google\appengine\api\users\UserService;
	
	$user = UserService::getCurrentUser();

	if ($user == null){
		header('Location: ' .
					 UserService::createLoginURL('http://localhost:8080/music'));
	}
	else
		header('Location: '.'http://localhost:8080/music')
?>