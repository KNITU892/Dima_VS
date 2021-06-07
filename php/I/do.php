<?php
$q1 = $_REQUEST['q1'];
$t1 =  $_REQUEST['t1'];
$t2 =  $_REQUEST['t2'];
$q2 =  $_REQUEST['q2'];

$I = ($q2 - $q1)/($t2 - $t1);
?>

<!DOCTYPE html>
<html>
<head>
	<title>Формула</title>
</head>
<body>

	<a style="color:red;font-size: 50px;">I:</a> <input style="font-size: 30px;" type="text" value="<?php echo $I ?>" /><br /> 
	<button><a style="color:red;font-size: 50px" href="./"> Вернутся </a></button>

</body>
</html>