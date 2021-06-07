<?php
$M = $_REQUEST['m1'];
$t1 =  $_REQUEST['t1'];
$t2 =  $_REQUEST['t2'];
$m =  $_REQUEST['m'];
$R =  $_REQUEST['r'];

$A = ((-3/2)*($m/$M))*($R*($t2 - $t1));
?>

<!DOCTYPE html>
<html>
<head>
	<title>Формула</title>
</head>
<body>

	<a style="color:red;font-size: 50px;">A:</a> <input style="font-size: 30px;" type="text" value="<?php echo $A ?>" /><br /> 
	<button><a style="color:red;font-size: 50px" href="./"> Вернутся </a></button>

</body>
</html>