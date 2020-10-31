<?php    
/*
作者：聂宗霞
修改日期：2020-10-31
说明：
	连接maven库，git库，实现自动打包
 */
include "path.php";//从公共文件中获取路径和数据库配置
if(!isset($_COOKIE["bcontents_value"])){
	$batch='';
	echo "请选择版本库！";
}else{
	$batch=$_COOKIE["bcontents_value"];
}
$dir=$project;
//数组参数
$files = array();
$user_addr=array();
$user_id=array();
$qarr=array();
$branchs=array();

//读取文件目录
if(is_dir($dir)){
	if ($dh=opendir($dir)){
		$i=0;
		while(($file=readdir($dh))!= false){
			if($file!='.'&&$file!='..'){
				if(is_dir($dir.$file)){
					$files[$i]=$file;
					$i++;
				}
			}
		}
		closedir($dh);
	}
}

header("Content-Type:text/html;charset=utf-8");//gb2312
 $hostip='http://'.$_SERVER['SERVER_ADDR'];
    echo '<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>APP上传</title>
        <script type="text/javascript" src="lib/js/qrcanvas.js"></script>
    </head>
    <body bgcolor="#D7E4F2">
	<h1><font face="华文彩云">maven打包</font></h1><a href="/ewm/batch.php"><img src="/ewm/images/head.jpg" width="25" height="25" /></a>';
?>
<script type="text/javascript">
//Cookie生成及清空，存入当前版本库、用户IP
	function get_value(){
		var name="bcontents_value";
		var value=document.getElementById("bcontents").value;
		var exp=new Date();
		exp.setTime(exp.getTime()+120*60*60*1000);//过期时效为5天
		document.cookie=name+"="+value+";expires="+exp.toGMTString();
		document.location.reload();
	}
</script>
<?php
echo "当前版本库： ".$batch."<hr/>";
?>
<form action="do_package.php" method="post" enctype="multipart/form-data">
	请选择版本库分支及打包者：
	<select name="bcontents" id="bcontents" onChange="get_value()">
	<option value="">--版本库--</option>
	
<?php
	foreach($files as $id=>$val){
	echo "<option value=".$val.">".$val."</option>";}//从path.php传入的路径获取当前目录下的目录清单（该清单为版本库）
?>
</select>
<select name="BRcontents" onChange="MM_jumpMenu('parent',this,0)">
	<option value="0">------------请选择分支------------</option>
<?php
	$branchs_cmd=exec('cd '.$dir.$batch.'/ && "'.$git.'" branch',$output);
	foreach($output as $branch=>$val){
	echo "<option value=".$val.">".$val."</option>";}
?>
	</select>
<input type="submit" value="开始打包"/>
<hr /><a href="/index.php"> | 返回主页 | </a></form>
<hr />

</body><META HTTP-equiv=REFRESH CONTENT='600;URL=/index.php'></html>
