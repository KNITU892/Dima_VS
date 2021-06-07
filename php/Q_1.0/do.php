<?php
$c = $_REQUEST['c'];
$t1 =  $_REQUEST['t1'];
$t2 =  $_REQUEST['t2'];
$m =  $_REQUEST['m'];

$Q = $c*$m*($t2 - $t1);
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