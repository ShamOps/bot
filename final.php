
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>Sharo</title>
	<?php
	if(isset($_POST['submit'])) {
	    $d = $_POST['data'];
	    $fp = fopen('/final.txt', 'w');  
		fwrite($fp, $d);   
		fclose($fp);  
	}
	?>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
	<h2>New Text:</h2>
	<textarea name="data" class="text" form="form" rows="5"></textarea>

	
	<div>
	<form method='post' class="form" id="form">
		
		<input type="submit" name="submit" class="submit">
	</form>
	
	</div>
	<h2>Saved Text:</h2>
    <textarea id="ta" class="textarea" rows="10"></textarea>
    <script>
	       fetch('/final.txt')
		  .then(response => response.text())
		  .then(data => {
		  	document.getElementById('ta').innerHTML = data;
		  });
    </script>

</body>
</html>