<META HTTP-equiv=REFRESH CONTENT='300;URL=/index.php'>
<?php
/*
���ߣ�����ϼ
�޸����ڣ�2019-07-19
˵����
	apps zip���ϴ�ִ���ļ�
 */
include "path.php";//�ӹ����ļ��л�ȡ·�������ݿ�����
header("Content-Type:text/html;charset=gb2312");
date_default_timezone_set('prc');//����ʱ��Ϊ������
//����
$hostip='http://'.$_SERVER['SERVER_ADDR'];//����IP��ַ
$hostport=':'.$_SERVER['SERVER_PORT'];//�����˿�
$root='/ewm/ins/';//��ҳ�ϴ���Ŀ¼
//����
$Batch=$_COOKIE['bcontents_value'];//�汾��
$branch_switch=$_POST['BRcontents'];

//ϵͳʱ��
$date=date('ymd',time());
$time=date('His',time());
//�ۺ�����
//$Ulink=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/'.$filename;//������������
//$Ulinks=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/'.$filenames;//����������������web��ʾ��������
//$uplog=$hostip.$hostport.$root.$Server_dir.'/'.$date.'/'.$clip.'_'.$time.'/uplog.txt';//�����ļ��Ա���־����
//$cur_path=$ins.$Server_dir.'/'.$date;//���ڸ�Ŀ¼
//$updir=$cur_path.'/'.$clip.'_'.$time;//ʱ��Ŀ¼

exec('cd '.$project.$Batch.'/ && "'.$git.'" checkout '.$branch_switch.' && "'.$git.'" pull',$output);
foreach($output as $id=>$val){
	echo $val;
}

echo '<hr />| <a href="/ewm/package.php">���´��</a> | <a href='.$root.$Batch.'>�鿴��ǰĿ¼</a>| ';
