<?php
/*
���ߣ�����ϼ
����޸����ڣ�2019-07-19
˵����
	�����ļ�Ԥɾ����顣
*/
include "path.php";
//<META HTTP-equiv=REFRESH CONTENT='15;URL=/ewm/dx.php'>��дҳ�汾����Զ�ˢ��
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
	| <a href="/ewm/dx.php">���»�ȡ</a>| <a href="/index.php">������ҳ</a>
	|<hr />
message:
<?php
system($py."dx.py ".$user." ".$pwd." ".$host);
?>
</body><META HTTP-equiv=REFRESH CONTENT='600;URL=/index.php'></html>
