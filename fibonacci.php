<html>
<body>

<h3> The nth Fibonacci number is:</h3>
<?php
$n = $_POST['n'];
if(!empty($n)){
	if ($n == 0){
		$fib = 0;}
	if ($n == 1 || $n == 2){
		$fib = 1;}
if ($n > 2){
	$int1 =  1;
	$int2 =  1;	
	$fib = 0;
   for($i = 1; $i < $n-2; $i++){
      $fib = $int1 + $int2;
      $int2 = $int1;
      $int1 = $fib;
   }}
   echo $fib;
}
echo $_POST['n']
?>

</body>
</html>