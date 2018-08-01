<?php
header("Content-Type:text/html;charset=gb2312");
date_default_timezone_set('prc');//设置时区为东八区
//路径
$home='C:/xampp/htdocs/sit/';//物理地址根目录
$ins=$home.'ins/';//文件上传根目录
$py='C:/xampp/htdocs/sit/py/';//python执行文件根目录
$desktop='D:/Users/Desktop/test/';//测试根目录
$report='D:/SVN/test/auto_test_plan/war_install_record_report.xls';//记录备份地址
$record='C:/xampp/htdocs/sit/ins/war_install_record_report.xls';
//文件
$filename=$_FILES['myFile']['name'];//文件名
$type=$_FILES['myFile']['type'];//文件类型
$tmp_name=$_FILES['myFile']['tmp_name'];//文件缓存目录
$size=$_FILES['myFile']['size'];//文件大小
$error=$_FILES['myFile']['error'];//文件上传报错
//主机
$hostip='http://'.$_SERVER['SERVER_ADDR'];//主机IP地址
$clip=$_SERVER['REMOTE_ADDR'];//客户端IP地址
$hostport=':'.$_SERVER['SERVER_PORT'];//主机端口
$root='/sit/ins/';//网页上传根目录
//参数
$Server_dir=$_POST['scontents'];
$Batch=$_POST['bcontents'];
$Que_st=$_POST['qcontents'];
$Tester=$_POST['tcontents'];
$opert=$_POST['optcontents'];
$que_con=$_POST['quecontent'];
$QUE_content=str_replace(array("\r\n","\r","\n"," "),"ppppp",$_POST['quecontent']);
$beizhu=$_POST['pcontents'];
$task=$_POST['rcontents'];
//系统时间
$date=date('ymd',time());
$time=date('His',time());
$wdate=date('y/m/d',time());
$wtime=date('H:i:s',time());
$opdate=$date.'_'.$time;
//综合链接
$Ulink=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/'.$filename;//生成下载链接
$cur_path=$ins.$Server_dir.'/'.$date;//日期根目录
$updir=$cur_path.'/'.$clip.'_'.$time;//时间目录

//执行代码
if($opert=="test"){//测试模式，用于测试压缩包是否能正常读取解压
	echo '测试模式：<hr/>';
	if(!file_exists($desktop.'test/'.$filename)){
	copy($tmp_name, $desktop.'test/'.$filename);
	move_uploaded_file($tmp_name, $desktop.$filename);
	}else{
		move_uploaded_file($tmp_name, $desktop.$filename);
	}
$filenamef=$desktop.'test/'.$filename;
$filenamed=$desktop.$filename;
	system($py.'comp.py '.$filenamef.' '.$filenamed.' '.$updir);
}else{
//问题清单判断逻辑
$count_1=substr_count($que_con,"\n");//统计回车
$count_2=substr_count($QUE_content,iconv("GB2312","UTF-8","、"));//统计"、"，以下同理
$count_3=substr_count($QUE_content,";");
$count_4=substr_count($QUE_content,iconv("GB2312","UTF-8","；"));
$count_5=substr_count($QUE_content,".");
$count_6=substr_count($QUE_content,iconv("GB2312","UTF-8","。"));
$count_7=substr_count($QUE_content,iconv("GB2312","UTF-8","："));
$count_8=substr_count($QUE_content,":");
$count_a=array(abs($Que_st-$count_1),abs($Que_st-$count_2),abs($Que_st-$count_3),abs($Que_st-$count_4),abs($Que_st-$count_5),abs($Que_st-$count_6),abs($Que_st-$count_7),abs($Que_st-$count_8));//生成问题与问题数差值，取绝对值
$count_min=min($count_a);//取最小绝对值
if (!file_exists($cur_path)){//判断日期根目录是否存在
	mkdir($cur_path);
	mkdir($updir);
}else{
	mkdir($updir);//时间目录需实时新建
}
if($count_min>=1){
	echo "<br/><br/><br/>问题数差值：".$count_min."<br/><br/><br/>"."仅当问题数差值小于1时方可提交成功!";
}else{
	if($Que_st==0 and $QUE_content=='' and !file_exists($ins.'first/'.$Batch.'_'.$filename)){
		if ($error==0){
			echo $filename."   成功上传到：<hr/>".$Ulink."<hr/>";
			system($py.'write.py '.$record.' '.$wtime.' '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$updir.' '.$Ulink.' '.$beizhu.' '.$Tester);
			system($py.'send_email.py '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$Ulink.' '.$beizhu.' '.$Tester.' '.$clip);
			copy($tmp_name, $ins.'first/'.$Batch.'_'.$filename);
			echo '<hr />';
		}else{
			switch ($error){
				case 1:
					echo "超过了上传文件的最大值，请上传100M以下文件";
					break;
				case 2:
					echo "上传文件过多，请一次上传20个及以下文件！";
					break;
				case 3:
					echo "文件并未完全上传，请再次尝试！";
					break;
				case 4:
					echo "未选择上传文件！";
					break;
				case 5:
					echo "上传文件为0";
					break;
			}
		}
	}elseif($Que_st!=0 and $QUE_content!=''){
		if ($error==0) {
			echo $filename."   成功上传到：<hr/>".$Ulink."<hr/>";
			system($py.'write.py '.$record.' '.$wtime.' '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$updir.' '.$Ulink.' '.$beizhu.' '.$Tester.' '.$QUE_content);
			system($py.'send_email.py '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$Ulink.' '.$beizhu.' '.$Tester.' '.$clip.' '.$QUE_content);
			echo $task.$Que_st.$Batch;
			echo '<hr />';
		}else{
			switch ($error){
				case 1:
					echo "超过了上传文件的最大值，请上传500M以下文件";
					break;
				case 2:
					echo "上传文件过多，请一次上传20个及以下文件！";
					break;
				case 3:
					echo "文件并未完全上传，请再次尝试！";
					break;
				case 4:
					echo "未选择上传文件！";
					break;
				case 5:
					echo "上传文件为0";
					break;
			}
		}
	}elseif($Que_st==0 and $QUE_content=='' and file_exists($ins.'first/'.$Batch.'_'.$filename)){
		echo '警告：该版本并非第一次发版！<hr />';
}else{
	echo "问题数与问题清单不匹配！<hr/>";
}
	move_uploaded_file($tmp_name, $updir.'/'.$filename);
	//copy($ins.'war_install_record_report.xls', $report);
$filenamef=$ins.'first/'.$Batch.'_'.$filename;
$filenamed=$updir.'/'.$filename;
if($task==""){
	system($py.'decide.py '.$Batch.' '.$filename.' '.$filenamed.' '.$ins);
}else{
	system($py.'decide.py '.$Batch.' '.$filename.' '.$filenamed.' '.$ins.' '.$task);
}
	echo '<br/>';
	system($py.'comp.py '.$filenamef.' '.$filenamed.' '.$updir);
	
}
}
	echo '<hr />| <a href="/ewm/ins.php">重新上传</a> | <a href='.$root.$Server_dir.'>查看当前目录</a>| ';