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


<div id ="top_head">
	<h1><font face='BATMAN' color='white' face=''>Simple nth Fib Calculator </font></h1> 
</div>
	<div id="fib_form">
		<form action="fibonacci.php" method="POST">
		<label for="n"><font color='white'>Input N = </font></label><input id="n" name = "n" value = "0" type="textbox" />
		<input padding-left="10px" type="submit" value="Calculate" />
	</div>
		
</form>
</body>
</html>
