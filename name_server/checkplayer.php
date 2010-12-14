<?php
  class pw_name_server_config
  {
    const db_connect_wrapper_filename = "databaseconnect.php";
    const db_name = "pw_player_names";
    const max_names_per_player = 5;
  }

  function pw_database_error()
  {
    error_log("pw database error: " . mysql_error());
    return -2;
  }

  function player_register_name($player_uid, $escaped_name)
  {
    $result = mysql_query("SELECT id, unique_id FROM player_names WHERE name = '$escaped_name';");
    if (!$result) return pw_database_error();
    if ($row = mysql_fetch_assoc($result))
    {
      if ($row["unique_id"] == $player_uid)
      {
        $result = mysql_query("UPDATE player_names SET last_used_time = CURRENT_TIMESTAMP() WHERE id = '$row[id]';");
        if (!$result) return pw_database_error();
      }
      else
      {
        return 1;
      }
    }
    else
    {
      $result = mysql_query("SELECT id FROM player_names WHERE unique_id = '$player_uid' ORDER BY last_used_time;");
      if (!$result) return pw_database_error();
      global $max_names_per_player;
      if (mysql_num_rows($result) >= pw_name_server_config::max_names_per_player)
      {
        $row =  mysql_fetch_assoc($result);
        $result = mysql_query("UPDATE player_names SET name = '$escaped_name' WHERE id = '$row[id]';");
        if (!$result) return pw_database_error();
      }
      else
      {
        $result = mysql_query("INSERT INTO player_names (unique_id, name) VALUES ('$player_uid', '$escaped_name');");
        if (!$result) return pw_database_error();
      }
    }
    return 0;
  }

  $id_restrictions = array("options"=>array("min_range"=>1, "max_range"=>250));
  $player_id = filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT, $id_restrictions);
  $id_restrictions = array("options"=>array("min_range"=>1, "max_range"=>10000000));
  $player_uid = filter_input(INPUT_GET, "uid", FILTER_VALIDATE_INT, $id_restrictions);
  $player_name = filter_input(INPUT_GET, "name", FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_LOW|FILTER_FLAG_STRIP_HIGH);

  $return_code = -1;
  if ($player_id && $player_uid && $player_name)
  {
    require(pw_name_server_config::db_connect_wrapper_filename);
    $db_connection = pw_mysql_connect();
    if ($db_connection)
    {
      mysql_select_db(pw_name_server_config::db_name, $db_connection);
      $escaped_name = mysql_real_escape_string($player_name);
      $return_code = player_register_name($player_uid, $escaped_name);
      mysql_close($db_connection);
    }
    echo "$return_code|$player_id|$player_uid|$player_name";
  }
  else
  {
    echo "$return_code";
  }
?>
