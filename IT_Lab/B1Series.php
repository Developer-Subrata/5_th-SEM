<!-- 1> Print The Following Series : 
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
Code:  -->

<?php
echo "The Series Is : \n";
for ($i=1; $i<=5; $i++){
    for ($j=1; $j<=$i; $j++){
        echo "$j ";
    }
    echo "\n";
}
?>

