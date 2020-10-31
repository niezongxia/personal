<?php
/*
作者：聂宗霞
最后修改日期：2019-07-19
说明：
	过期文件预删除检查。
*/
include "path.php";
//<META HTTP-equiv=REFRESH CONTENT='15;URL=/ewm/dx.php'>填写页面本身可自动刷新
header("Content-Type:text/html;charset=gbk");
$user="motion";
$pwd="qwe123";
$host="22.188.24.249";
?>
    <html>
    <head>
        <meta charset="utf-8" http-equiv="refresh" content="200">
        <title>message</title>
    </head>
    <body bgcolor="#D7E4F2">
	| <a href="/ewm/dx.php">重新获取</a>| <a href="/index.php">返回主页</a>
	|<hr />
message:
<?php
system($py."dx.py ".$user." ".$pwd." ".$host);
?>
</body><META HTTP-equiv=REFRESH CONTENT='600;URL=/index.php'></html>
