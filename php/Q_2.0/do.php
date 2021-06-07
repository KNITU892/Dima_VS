<?php
$r = $_REQUEST['r'];
$m =  $_REQUEST['m'];

$Q = $r*$m*;
?>

<!DOCTYPE html>
<html>
<head>
	<title>Формула</title>
</head>
<body>

	<a style="color:red;font-size: 50px;">Q:</a> <input style="font-size: 30px;" type="text" value="<?php echo $Q ?>" /><br /> 
	<button><a style="color:red;font-size: 50px" href="./"> Вернутся </a></button>

</body>
</html>