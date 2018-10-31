<?php 
$text = $_GET['q'];

print "<html><title>Recommendation Analysis</title><body>";
print "$text";
system('dir', $retval);
print($retval);
#$html = fopen("recommend_table.html", 'r');
#print $html;
print "</body>";
print "</html>"
 ?>