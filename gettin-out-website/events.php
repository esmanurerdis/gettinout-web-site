<?php 
require_once 'config.php';

if (!isset($_GET["category"])) {
    $events = $con->prepare("SELECT ID,img, Name FROM events");
    $events->execute();
    $events = $events->fetchAll(PDO::FETCH_ASSOC);    
}else {
    $events = $con->prepare("SELECT ID,img, Name FROM events WHERE Category = :category");
    $events->execute([
        'category' => $_GET["category"]
    ]);
    $events = $events->fetchAll(PDO::FETCH_ASSOC);
}


$categories = $con->prepare("SELECT ID, Name FROM categories");
$categories->execute();
$categories = $categories->fetchAll(PDO::FETCH_ASSOC);
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

    <!-- Product Section Begin -->
    <section class="product spad">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-md-5">
                    <div class="sidebar">
                        <div class="sidebar__item">
                            <h4>Event Kategorileri</h4>
                            <ul>
                                <?php foreach($categories as $category) {?>
                                <li><a href="events.php?category=<?php echo $category["ID"] ?>"><?php echo $category["Name"] ?></a></li>
                                <?php } ?>
                            </ul>
                        </div>
                        
                    </div>
                </div>
                <div class="col-lg-9 col-md-7">
                    
                    <div class="filter__item">
                        <div class="row">
                            <div class="col-lg-4 col-md-5">
                                
                            </div>
                            <div class="col-lg-4 col-md-4">
                                <div class="filter__found">
                                    <h6><span><?php echo count($events); ?></span> Events found</h6>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-3">
                                
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <?php foreach($events as $event) {?>
                        <div class="col-lg-4 col-md-6 col-sm-6">
                            <div class="product__item">
                                <?php $resim = $event["img"] ?>
                                <div class="product__item__pic set-bg" data-setbg="img/categories/<?php echo $resim ?>">
                              
                                    <ul class="product__item__pic__hover">
                                        <li><a href="#"><i class="fa fa-heart"></i></a></li>
                                        <li><a href="#"><i class="fa fa-retweet"></i></a></li>
                                        <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                                    </ul>
                                </div>
                                <div class="product__item__text">
                                    <h6><a href="eventDetails.php?id=<?php echo $event["ID"]?>"><?php echo $event["Name"] ?></a></h6>
                                    <h5></h5>
                                </div>
                            </div>
                        </div>
                        <?php } ?>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Product Section End -->

<?php require_once "footer.php" ?>
</body>

</html>