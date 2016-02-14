<html>
	<body>
		<?php
		

$im1 = imagecreatefromjpeg("cat.jpg");

			$im2 = imagecreatefromjpeg("newCat.jpg");
			$count = 0;
			
			if (!$im1 || !$im2)
			{
				echo "Failed to load image";
			}
			else
			{
				list($width1, $height1, $type1, $attr1) = getimagesize("cat.jpg");
				list($width2, $height2, $type2, $attr2) = getimagesize("newCat.jpg");
				// echo $width1 . " " . $height1;
				// echo $width2 . " " . $height2;
				if (($width2 == $width1) && ($height2 == $height1))
				{
					$x = 0;
					$y = 0;
					// for ($y = 0; $y < $width2; $y ++)
					// {
					// 	for ($x = 0; $x < $height2; $x ++)
					// 	{
							for ($z = 0; $z < 24; $z ++)
							{
								$rgb1 = imagecolorat($im1,$x,$y);
	            				$r1 = ($rgb1 >> 16) & 0xFF;
	            				// echo $r1 . ":\n";
	            				$g1 = ($rgb1 >> 8) & 0xFF;
	            				// echo $g1 . ":\n";
	            				$b1 = $rgb1 & 0xFF;
	            				// echo $b1 . ":\n";
	            				
	            				$rgb2 = imagecolorat($im2,$x,$y);
								$r2 = ($rgb2 >> 16) & 0xFF;
								// echo $r2 . ":\n";
	            				$g2 = ($rgb2 >> 8) & 0xFF;
	            				// echo $g2 . ":\n";
	            				$b2 = $rgb2 & 0xFF;
	            				// echo $b2 . ":\n";

	            				$r = abs($r1 - $r2);
	            				$diff = $r; 
	            				echo $diff;
	            				// echo " ":
	            				$g = abs($g1 - $g2);
	            				$diff = $g; 
	            				echo $diff;
	            				// echo " ";
	            				$b = abs($b1 - $b2);
	            				$diff = $b; 
	            				echo $diff;
	            				// echo " ":
	            				
							}
						// }
					// }
				}
				else
				{
					echo "not same size";
				}






		    }
			?>
	</body>
</html>