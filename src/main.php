<?php
<<<<<<< HEAD
$command = "python3 main.py 2>&1";
$pid = popen( $command,"r");
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 usleep(100000);
}
pclose($pid);
=======
$command = escapeshellcmd('main.py');
$output = shell_exec($command);
echo $output;
>>>>>>> upstream/dev
?>
