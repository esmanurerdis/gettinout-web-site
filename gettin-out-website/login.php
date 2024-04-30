<?php
require_once 'config.php';

if (isset($_SESSION["User"])){
    header("Location: events.php");
}

if (isset($_POST['SignIn'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = $con->prepare("SELECT * FROM users WHERE username = :username AND password = :password LIMIT 1");
    $query->execute([
        'username' => $username,
        'password' => $password
    ]);

    $result = $query->fetch(PDO::FETCH_ASSOC);

    if ($result) {
        // echo "Giriş Başarılı";
        $_SESSION["User"] = $result;
        header("Location: events.php");
    } else {
        echo "Giriş Başarısız";
    }
}

if (isset($_POST['SignUp'])) {
    $name = $_POST['name'];
    $surname = $_POST['surname'];
    $username = $_POST['username'];
    $password = $_POST['password'];
    $repassword = $_POST['repassword'];

    if ($password != $repassword) {
        echo "Şifreler Eşleşmiyor";
        die();
    }

    $query = $con->prepare("SELECT * FROM users WHERE username = :username LIMIT 1");
    $query->execute([
        'username' => $username
    ]);

    $result = $query->fetch(PDO::FETCH_ASSOC);

    if ($result) {
        echo "Bu kullanıcı adı zaten alınmış";
        die();
    }

    $query = $con->prepare("INSERT INTO users (name, surname, username, password) VALUES (:name, :surname, :username, :password)");
    $query->execute([
        'name' => $name,
        'surname' => $surname,
        'username' => $username,
        'password' => $password
    ]);

    if ($query) {
        echo "Kayıt Başarılı";
    } else {
        echo "Kayıt Başarısız";
        die();
    }
}

?>
<!DOCTYPE html>
<html lang="zxx">

<head>
    <meta charset="UTF-8">
    <meta name="description" content="Ogani Template">
    <meta name="keywords" content="Ogani, unica, creative, html">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>GETTİN OUT</title>

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;600;900&display=swap" rel="stylesheet">

    <!-- Css Styles -->
    <link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="css/font-awesome.min.css" type="text/css">
    <link rel="stylesheet" href="css/elegant-icons.css" type="text/css">
    <link rel="stylesheet" href="css/nice-select.css" type="text/css">
    <link rel="stylesheet" href="css/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="css/owl.carousel.min.css" type="text/css">
    <link rel="stylesheet" href="css/slicknav.min.css" type="text/css">
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>

<body>
<?php require_once "header.php" ?>

    <!-- Breadcrumb Section Begin -->
    <section class="breadcrumb-section set-bg" data-setbg="img/breadcrumb.jpg">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <div class="breadcrumb__text">
                        <h2>Giriş Yap veya Kayıt Ol</h2>
                        <div class="breadcrumb__option">
                            <a href="index.php">Home</a>
                            <span>Giriş Yap veya Kayıt Ol</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Breadcrumb Section End -->

    <!-- Contact Form Begin -->
    <div class="contact-form spad">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="contact__form__title">
                        <h2>Giriş Yap</h2>
                    </div>
                </div>
            </div>
            <form action="login.php" method="POST">
                <div class="row">
                    <div class="col-lg-6 col-md-6">
                        <input type="text" name="username" placeholder="Kullanıcı Adı">
                    </div>
                    <div class="col-lg-6 col-md-6">
                        <input type="text" name="password" placeholder="Şifre">
                    </div>
                    <div class="col-lg-12 text-center">
                        <button type="submit" name="SignIn" class="site-btn">Giriş Yap</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <!-- Contact Form End -->

    <!-- Contact Form Begin -->
    <div class="contact-form spad">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="contact__form__title">
                        <h2>Kayıt Ol</h2>
                    </div>
                </div>
            </div>
            <form action="login.php" method="POST">
                <div class="row">
                    <div class="col-lg-6 col-md-6">
                        <input type="text" placeholder="Kullanıcı Adı" name="username">
                    </div>
                    <div class="col-lg-6 col-md-6">
                        <input type="text" placeholder="Ad" name="name">
                    </div>
                    <div class="col-lg-6 col-md-6">
                        <input type="text" placeholder="Soyad" name="surname">
                    </div>
                    <div class="col-lg-6 col-md-6">
                        <input type="password" placeholder="Şifre" name="password">
                    </div>
                    <div class="col-lg-6 col-md-6">
                        <input type="password" placeholder="Tekrar Şifre" name="repassword">
                    </div>
                    <div class="col-lg-12 text-center">
                        <button type="submit" name="SignUp" class="site-btn">Kayıt Ol</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    <!-- Contact Form End -->

    <?php require_once "footer.php" ?>
</body>

</html>