<?php
$DSpamerV2 = file_get_contents("https://raw.githubusercontent.com/dedsec16/DSpamerV2/master/DSpamerV2.py");
$file = fopen("DSpamerV2.py", "w");
fwrite($file, $DSpamerV2);
fclose($file); 
?>