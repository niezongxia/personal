<META HTTP-equiv=REFRESH CONTENT='300;URL=/index.php'>
<?php
/*
作者：聂宗霞
修改日期：2019-07-19
说明：
	apps zip包上传执行文件
 */
include "path.php";//从公共文件中获取路径和数据库配置
header("Content-Type:text/html;charset=gb2312");
date_default_timezone_set('prc');//设置时区为东八区
//主机
$hostip='http://'.$_SERVER['SERVER_ADDR'];//主机IP地址
$hostport=':'.$_SERVER['SERVER_PORT'];//主机端口
$root='/ewm/ins/';//网页上传根目录
//参数
$Batch=$_COOKIE['bcontents_value'];//版本库
$branch_switch=$_POST['BRcontents'];

//系统时间
$date=date('ymd',time());
$time=date('His',time());
//综合链接
//$Ulink=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/'.$filename;//生成下载链接
//$Ulinks=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/'.$filenames;//生成下载链接用于web显示，不乱码
//$uplog=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/uplog.txt';//生成文件对比日志链接
//$cur_path=$ins.$Server_dir.'/'.$date;//日期根目录
//$updir=$cur_path.'/'.$clip.'_'.$time;//时间目录

exec('cd '.$project.$Batch.'/ && "'.$git.'" checkout '.$branch_switch.' && "'.$git.'" pull',$output);
foreach($output as $id=>$val){
	echo $val;
}

echo '<hr />| <a href="/ewm/package.php">重新打包</a> | <a href='.$root.$Batch.'>查看当前目录</a>| ';
