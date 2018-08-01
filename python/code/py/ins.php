<?php  
/*
 * PHP QR Code encoder
 *
 * Exemplatory usage
 *
 * PHP QR Code is distributed under LGPL 3
 * Copyright (C) 2010-2013 Dominik Dzienia <deltalab at poczta dot fm>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 */
$clip=$_SERVER['REMOTE_ADDR'];
$dir="C:/xampp/htdocs/sit/ins/batch/".$_COOKIE["bcontents_value"]."/";///ins/batch/X89";//"C:/xampp/htdocs/ewm/ins/batch/X89/";//dirname(__FILE__);
$files = array();
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
$data=$files;
$qarr=array(0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20);
echo $_COOKIE["bcontents_value"];
$fp =fopen("D:/Users/Desktop/php.txt","w");
fwrite($fp,var_export($data,true));
fclose($fp);
 ?>

    <html>
    <head>
        <meta charset="utf-8">
        <title>Mlife_WAR包初审</title>
        <script type="text/javascript" src="lib/js/qrcanvas.js"></script>
    </head>
    <body>
    <h1>Mlife_WAR包初审</h1>
<?php echo "当前设备IP：".$clip."<hr/>";
?>
<form action="insup.php" method="post" enctype="multipart/form-data">
	请选择部署要求：
	<select name="scontents">
	<option value="">--请选择部署环境--</option>
	<option value="162">162 内部测试</option>
	<option value="249">249 验收测试</option>
	<option value="102">102 准生产</option></select>
	<select name="bcontents" id="bcontents" onChange="get_value()">
	<option value="">--请选择所属批次--</option>
	<option>X84</option>
	<option>X86</option>
	<option>X87</option>
	<option>P803</option>
	<option>P804</option>
	<option>P805</option>
	<option>P901</option>
	<option>X89</option>
	<option>X810</option>
	<option>X811</option>
	</select>
	<select name="rcontents" onChange="MM_jumpMenu('parent',this,0)">
	<option value="">------------请选择任务号------------</option>
	<?php
	foreach($data as $id=>$val){
	echo "<option value=".$id.">".$val."</option>";}
?>
	</select>
	<select name="qcontents">
	<option value="">-请选择问题数-</option>
	<?php
	foreach($qarr as $id=>$val){
	echo "<option value=".$id.">".$val." 个</option>";}
?>
	</select>
	<select name="tcontents">
	<option value="">--请选择主测--</option>
	<option value="niezongxia">聂宗霞</option>
	<option value="dinghe">丁鹤</option>
	<option value="litingting">李婷婷</option>
	<option value="jiangzhen">蒋朕</option>
	<option value="zhouliting">周丽婷</option>
	</select>
	<select name="optcontents">
	<option value="">--请选择部署方式--</option>
	<option value="all">全量部署</option>
	<option value="add">增量部署</option>
	</select>备注：
	<input type="text" name="pcontents" value="无"></text>
	<br/><hr />
	<label>问题清单：</label><br/>
	<textarea  name="quecontent" cols="100" rows ="20"></textarea>
	<br/><hr />
	请选择上传文件：
	<input type="file" name="myFile" />
	<input type="submit" value="上传"/>
	<hr />
	| <a href="/ewm/">返回主页</a>
	| <a href="/ewm/ins/">查看当前目录</a>
	| <hr /><br />部署需求均不可为空，若部署需求不完整会导致初审不通过，请谨慎操作。<br />
	<br />如填写问题清单，不限制具体格式，但建议参照如下格式填写，否则可能无法提交：
	<br />1.问题一；<br />2.问题二；<br />3.问题三；<br />4.问题四；
	<Script>function get_value(){
		var name="bcontents_value";
		var value=document.getElementById("bcontents").value;
		document.cookie="bcontents_value"+"="+value;
	}</Script>
	</body></html>