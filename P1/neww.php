		<html>
      <body>
            <?php
            $im1 = imagecreatefromjpeg("cat.jpg");
		$str = 'h';
		for ($i = 0; $i < strlen($str); $i++)
		{
			$dec = ord(substr($str, $i, 1));
			$bin = sprintf('%08d', base_convert($dec,10,2));
			$out .= $bin;
		}

		$x = 0;
		$y = 0;

		for ($i = 0;$i < strlen($out); $i ++)
		{
			$rgb = imagecolorat($im1, $x, $y)
			$r = ($rgb >> 16) & 0xFF;
            $g = ($rgb >> 8) & 0xFF;
            $b = $rgb & 0xFF;

            if($out[$i] == '1')
            {
            	if ($r == 255) 
            	{
            		$r--;
            	}
            	else 
            	{
            		$r++;
            	}
            }
            if($out[$i+1] == '1')
            {
            	if ($g == 255) 
            	{
            		$g--;
            	}
            	else 
            	{
            		$g++;
            	}
            }
            if($out[$i+2] == '1')
            {
            	if ($b == 255) 
            	{
            		$b--;
            	}
            	else 
            	{
            		$b++;
            	}
            }

            $newColor = imagecolorallocate($im, $r, $g, $b);
            imagesetpixel($im, $x, $y, $newColor);
            if($x == imagesx($im)-1)
            {
            	$x = 0;
            	$y++;
            }
            else
            {
            	$x++;
            }

		}


	imagejpeg($im1, "newCat.jpg");
	imagedestroy($im1);
      ?>
      </body>
</html>
