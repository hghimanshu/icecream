if (isset($_POST['submit'])) {
	$email = $_POST['email'];
	// Here you could connect to a database and insert the email address into a table
	// or you could append the email address to a text file on the server
	$file = fopen('emails.txt', 'a');
	fwrite($file, $email . "\n");
	fclose($file);
}
