<?php

$connection = pg_connect("host=localhost dbname=testdb user=postgres password=postgres");

if ($connection) {
  $user_is_compliant = false;

  echo "Connected successfully!\n";

  while (!$user_is_compliant) {
    $operation = strtolower(trim(readline("Insert, select or delete?\n> ")));

    if ($operation == 'insert' || $operation == 'select' || $operation == 'delete') {
      $user_is_compliant = true;
    }
  }

  $name = readline("Name to $operation?\n> ");

  if ($operation == 'insert') {
    insert($connection, $name);
  } elseif ($operation == 'select') {
    select($connection, $name);
  } elseif ($operation == 'delete') {
    delete($connection, $name);
  }
} else {
echo "Couldn't connect.\n";
}

function insert($conn, $name_to_insert)
{
  $insert = pg_insert($conn, 'testtable', ['testcolumn2' => $name_to_insert]);

  if ($insert) {
    echo "Inserted '$name_to_insert'!\n";
  } else {
    echo "Couldn't insert '$name_to_insert'\n";
  }
}

function select($conn, $name_to_select)
{
  $select = pg_select($conn, 'testtable', ['testcolumn2' => $name_to_select]);
  /* SELECT ALL:
  // Actual query to the database
  $select_successful = pg_query($connection, 'SELECT * FROM public.testtable ORDER BY testcolumn1 ASC');

  // "Fetching" the resulting PgSql\Result into an array
  $fetched_select = pg_fetch_all($select_successful);
  */
  if ($select) {
    echo $select[0]['testcolumn2'], ", ID ", $select[0]['testcolumn1'], "\n";
    /* SELECT ALL:
    for ($i=0; $i < count($fetched_select); $i++) {
      // Indexing the "fetched" array to enable looping
      $indexed_select = array_values($fetched_select[$i]);
      for ($j=0; $j < count($indexed_select); $j++) {
        // Actually looping the nested arrays and echoing contents
        echo $indexed_select[$j], " ";
      }
      echo "\n";
    }
    */
  } else {
    // For single name only
    echo "'$name_to_select' not found\n";
  }
}

function delete($conn, $name_to_delete)
{
  $delete = pg_delete($conn, 'testtable', ['testcolumn2' => $name_to_delete]);

  if (!$delete) {
    echo "There was an error!";
  }
}

pg_close($connection);

?>
