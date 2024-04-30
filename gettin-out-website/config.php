<?php

$user = "root";
$pass = "";
$dbName = "proje";

try {
    $con = new PDO('mysql:host=localhost;port=3306;dbname='.$dbName, $user, $pass);
} catch (PDOexception $e) {
    echo "Veritabanı bağlantısı başarısız";
    die();
}

session_start();

?>