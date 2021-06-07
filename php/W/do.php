<?php
$c = $_REQUEST['c'];
$u =  $_REQUEST['u'];

$W = $c*$u*;
?>

<!DOCTYPE html>
<html>
<head>
	<title>Формула</title>
</head>
<body>

	<a style="color:red;font-size: 50px;">W:</a> <input style="font-size: 30px;" type="text" value="<?php echo $W ?>" /><br /> 
	<button><a style="color:red;font-size: 50px" href="./"> Вернутся </a></button>

</body>
</html>