<?php
header("Content-Type:text/html;charset=gb2312");
date_default_timezone_set('prc');//����ʱ��Ϊ������
//·��
$home='C:/xampp/htdocs/sit/';//�����ַ��Ŀ¼
$ins=$home.'ins/';//�ļ��ϴ���Ŀ¼
$py='C:/xampp/htdocs/sit/py/';//pythonִ���ļ���Ŀ¼
$desktop='D:/Users/Desktop/test/';//���Ը�Ŀ¼
$report='D:/SVN/test/auto_test_plan/war_install_record_report.xls';//��¼���ݵ�ַ
$record='C:/xampp/htdocs/sit/ins/war_install_record_report.xls';
//�ļ�
$filename=$_FILES['myFile']['name'];//�ļ���
$type=$_FILES['myFile']['type'];//�ļ�����
$tmp_name=$_FILES['myFile']['tmp_name'];//�ļ�����Ŀ¼
$size=$_FILES['myFile']['size'];//�ļ���С
$error=$_FILES['myFile']['error'];//�ļ��ϴ�����
//����
$hostip='http://'.$_SERVER['SERVER_ADDR'];//����IP��ַ
$clip=$_SERVER['REMOTE_ADDR'];//�ͻ���IP��ַ
$hostport=':'.$_SERVER['SERVER_PORT'];//�����˿�
$root='/sit/ins/';//��ҳ�ϴ���Ŀ¼
//����
$Server_dir=$_POST['scontents'];
$Batch=$_POST['bcontents'];
$Que_st=$_POST['qcontents'];
$Tester=$_POST['tcontents'];
$opert=$_POST['optcontents'];
$que_con=$_POST['quecontent'];
$QUE_content=str_replace(array("\r\n","\r","\n"," "),"ppppp",$_POST['quecontent']);
$beizhu=$_POST['pcontents'];
$task=$_POST['rcontents'];
//ϵͳʱ��
$date=date('ymd',time());
$time=date('His',time());
$wdate=date('y/m/d',time());
$wtime=date('H:i:s',time());
$opdate=$date.'_'.$time;
//�ۺ�����
$Ulink=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/'.$filename;//������������
$cur_path=$ins.$Server_dir.'/'.$date;//���ڸ�Ŀ¼
$updir=$cur_path.'/'.$clip.'_'.$time;//ʱ��Ŀ¼

//ִ�д���
if($opert=="test"){//����ģʽ�����ڲ���ѹ�����Ƿ���������ȡ��ѹ
	echo '����ģʽ��<hr/>';
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
//�����嵥�ж��߼�
$count_1=substr_count($que_con,"\n");//ͳ�ƻس�
$count_2=substr_count($QUE_content,iconv("GB2312","UTF-8","��"));//ͳ��"��"������ͬ��
$count_3=substr_count($QUE_content,";");
$count_4=substr_count($QUE_content,iconv("GB2312","UTF-8","��"));
$count_5=substr_count($QUE_content,".");
$count_6=substr_count($QUE_content,iconv("GB2312","UTF-8","��"));
$count_7=substr_count($QUE_content,iconv("GB2312","UTF-8","��"));
$count_8=substr_count($QUE_content,":");
$count_a=array(abs($Que_st-$count_1),abs($Que_st-$count_2),abs($Que_st-$count_3),abs($Que_st-$count_4),abs($Que_st-$count_5),abs($Que_st-$count_6),abs($Que_st-$count_7),abs($Que_st-$count_8));//������������������ֵ��ȡ����ֵ
$count_min=min($count_a);//ȡ��С����ֵ
if (!file_exists($cur_path)){//�ж����ڸ�Ŀ¼�Ƿ����
	mkdir($cur_path);
	mkdir($updir);
}else{
	mkdir($updir);//ʱ��Ŀ¼��ʵʱ�½�
}
if($count_min>=1){
	echo "<br/><br/><br/>��������ֵ��".$count_min."<br/><br/><br/>"."������������ֵС��1ʱ�����ύ�ɹ�!";
}else{
	if($Que_st==0 and $QUE_content=='' and !file_exists($ins.'first/'.$Batch.'_'.$filename)){
		if ($error==0){
			echo $filename."   �ɹ��ϴ�����<hr/>".$Ulink."<hr/>";
			system($py.'write.py '.$record.' '.$wtime.' '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$updir.' '.$Ulink.' '.$beizhu.' '.$Tester);
			system($py.'send_email.py '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$Ulink.' '.$beizhu.' '.$Tester.' '.$clip);
			copy($tmp_name, $ins.'first/'.$Batch.'_'.$filename);
			echo '<hr />';
		}else{
			switch ($error){
				case 1:
					echo "�������ϴ��ļ������ֵ�����ϴ�100M�����ļ�";
					break;
				case 2:
					echo "�ϴ��ļ����࣬��һ���ϴ�20���������ļ���";
					break;
				case 3:
					echo "�ļ���δ��ȫ�ϴ������ٴγ��ԣ�";
					break;
				case 4:
					echo "δѡ���ϴ��ļ���";
					break;
				case 5:
					echo "�ϴ��ļ�Ϊ0";
					break;
			}
		}
	}elseif($Que_st!=0 and $QUE_content!=''){
		if ($error==0) {
			echo $filename."   �ɹ��ϴ�����<hr/>".$Ulink."<hr/>";
			system($py.'write.py '.$record.' '.$wtime.' '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$updir.' '.$Ulink.' '.$beizhu.' '.$Tester.' '.$QUE_content);
			system($py.'send_email.py '.$Server_dir.' '.$Batch.' '.$opert.' '.$Que_st.' '.$Ulink.' '.$beizhu.' '.$Tester.' '.$clip.' '.$QUE_content);
			echo $task.$Que_st.$Batch;
			echo '<hr />';
		}else{
			switch ($error){
				case 1:
					echo "�������ϴ��ļ������ֵ�����ϴ�500M�����ļ�";
					break;
				case 2:
					echo "�ϴ��ļ����࣬��һ���ϴ�20���������ļ���";
					break;
				case 3:
					echo "�ļ���δ��ȫ�ϴ������ٴγ��ԣ�";
					break;
				case 4:
					echo "δѡ���ϴ��ļ���";
					break;
				case 5:
					echo "�ϴ��ļ�Ϊ0";
					break;
			}
		}
	}elseif($Que_st==0 and $QUE_content=='' and file_exists($ins.'first/'.$Batch.'_'.$filename)){
		echo '���棺�ð汾���ǵ�һ�η��棡<hr />';
}else{
	echo "�������������嵥��ƥ�䣡<hr/>";
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
	echo '<hr />| <a href="/ewm/ins.php">�����ϴ�</a> | <a href='.$root.$Server_dir.'>�鿴��ǰĿ¼</a>| ';