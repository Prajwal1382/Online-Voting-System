<?php
    session_start();
    require_once("Config.php");

    if($_SESSION['Key'] != "AdminKey")
    {
        echo "<script> location.assign('logout.php'); </script>";
        die;
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adminpanel - Online Voting System</title>
    <link rel="stylesheet" href="../assest/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assest/css/style.css">
</head>
<body>
    
       <div class="container-fluid">
       <div class="row bg-black text-white">
            <div class="col-1">
                <img src="../assest/Images/logo.gif" width="80px" />
            </div>
               <div class="col-11 my-auto">
                       <h3> ONLINE VOTING SYSTEM - <small> WELCOME </small><?php echo $_SESSION['username']; ?><!DOCTYPE html>
            </div>
        </div>
        
        
