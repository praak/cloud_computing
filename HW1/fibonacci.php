<html>
<head>
	<link rel="stylesheet" type="text/css" href="fibonacci.css" />
</head>
<style>
body{
background-image: url("bakground_image.jpg");
background-size: 100%;
background-position: fixed;
background-repeat: no-repeat;
background-color: black;
}
@font-face {
  font-family: BATMAN;
       src:url(batman.woff);
}
</style>
<body>
<div id="divcenter">
<h3> <font face='BATMAN' color='white'>The nth Fibonacci number is:</font></h3>
<font color='white'>
	<?php
$n = $_POST['n'];
	if ($n == 0){
		$fib = 0;
	}
	if ($n == 1 || $n == 2){
		$fib = 1;
	}
	if ($n >= 3){
		$int1 =  1;
		$int2 =  1;	
		$fib = 0;
		echo "The fibonacci sequence: <br>";
		echo "1 1 ";
	   for($i = 1; $i <= $n-2; $i++){
	      $fib = $int1 + $int2;
	      $int2 = $int1;
	      $int1 = $fib;
	      echo $fib;
	      echo " ";
	    }
	}
	echo "<br><br>And the nth number is: <br>";
	echo $fib;
?>
</font>
</div>

</body>
</html>