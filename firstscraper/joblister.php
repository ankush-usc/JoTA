<?php

$link = mysql_connect('127.0.0.1','','');
if(!$link){

die('Could not connect:'.mysql_error());
}
$db_select = mysql_select_db("testdb",$link);
 if (!$db_select) {
 die("Database selection also failed miserably: " . mysql_error());
 }
 
function get_best_match($skill1,$skill2,$skill3,$loc){
	#We will generate three queries on the skill match
	#all skills match, 2 skills match, 1 skill match and display it based on the number of days it was posted before
	$curcount=0;
	$result_array = [];
	$curquery = "Select Company, skills, days, title, link from JobDetail where Location='$loc' and skills like '%$skill1 %' and skills like '%$skill2 %' and skills like '%$skill3 %' limit 10";
	#echo "$curquery\n";
	$curresult = mysql_query($curquery);
	$num = @mysql_numrows($curresult);
	$i = 0;
	while($i<$num){
		$field1 = mysql_result($curresult,$i,"Company");
		$field2 = mysql_result($curresult,$i,"skills");
		$field3 = mysql_result($curresult,$i,"days");
		$field4 = mysql_result($curresult,$i,"title");
		$field5 = mysql_result($curresult,$i,"link");
		array_push($result_array, [
			'Company' => $field1,
			'skills'=>$field2,
			'days'=>$field3,
			'title'=>$field4,
			'link'=>$field5
		]);
		$i++;
	}
	$curcount = $num;
	$curcount = 10 - $curcount;
	$curquery = "Select Company, skills, Days, Jobtitle, Link from jota where Location='$loc' and skills like '%$skill1%' or skills like '%$skill2%' or skills like '%$skill3%' limit $curcount;";
	#echo "$curquery\n";
	$curresult = mysql_query($curquery);

	$num = 	@mysql_numrows($curresult);
	$i = 0;
        while($i<$num){
                $field1 = mysql_result($curresult,$i,"Company");
                $field2 = mysql_result($curresult,$i,"skills");
                $field3 = mysql_result($curresult,$i,"Days");
                $field4 = mysql_result($curresult,$i,"Jobtitle");
                $field5 = mysql_result($curresult,$i,"Link");
                array_push($result_array, [
                        'Company' => $field1,
                        'skills'=>$field2,
                        'days'=>$field3,
                        'title'=>$field4,
                        'link'=>$field5
                ]);
                $i++;
        }
	$someJSON = json_encode($result_array,JSON_UNESCAPED_SLASHES);
        return $someJSON;
}
#Sample call = http://localhost/joblist.php?skill1=C&skill2=C++&skill3=Java&location=Sunnyvale

function get_raw_score($skill1,$skill2,$skill3,$loc){
	$myfile = fopen("output_best_match.txt", "r") or die("Unable to open file!");
	$sk1_val=0;
	$sk2_val=0;
	$sk3_val=0;
	$loc_val=0;
	$count = 0;
	$skill1 = $skill1 . ":";
	$skill2 = $skill2 . ":";
	$skill3 = $skill3 . ":";
	$loc = $loc . ":";
	#echo "received skills = ".$skill1." ," . $skill2 . "," . $skill3 . " and ".$loc;
	while(!feof($myfile) && $count!=4) {
  		$raw_string = fgets($myfile);
		#echo "rawstring = ".$raw_string;
		if(strstr($raw_string, $skill1) !== false && $sk1_val==0){
			$count++;
			$raw_val = explode($skill1,$raw_string);
			$intermediate = explode("::",$raw_val[1]);
			$sk1_val = intval($intermediate[0]);
				
		}
		if(strstr($raw_string, $skill2) !== false &&  $sk2_val==0){
                        $count++;
                        $raw_val = explode($skill2,$raw_string);
                        $intermediate = explode("::",$raw_val[1]);
                        $sk2_val = intval($intermediate[0]);

                }
		if(strstr($raw_string, $skill3) !== false && $sk3_val==0){
                        $count++;
                        $raw_val = explode($skill3,$raw_string);
                        $intermediate = explode("::",$raw_val[1]);
                        $sk3_val = intval($intermediate[0]);

                }
		if(strstr($raw_string, $loc) !== false && $loc_val == 0){
                        $count++;
                        $raw_val = explode($loc,$raw_string);
                        $intermediate = explode("::",$raw_val[1]);
                        $loc_val = intval($intermediate[0]);

                }
	}
	fclose($myfile);	
	$base_match = 0.6 * (0.57*$sk1_val+0.29*$sk2_val+0.14*$sk3_val) + 0.4 * $loc_val;
	return $base_match;
	# fetch data from DB based on params and apply best match
}

function get_scores($s1,$s2,$s3,$loc){
		$result = get_raw_score($s1,$s2,$s3,$loc);
		while($result > 100) {
			$result = $result/10;
		}
		echo $result."#";
		
		$result_match = get_best_match($s1,$s2,$s3,$loc);
		echo $result_match;
}

#echo $argv[1] . "and" . $argv[2] . " and " . $argv[3] . " and " . $argv[4];

get_scores($argv[1],$argv[2],$argv[3],$argv[4]);

mysql_close();

?>
