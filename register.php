<?php
$message= '';
$error = '';
if (isset($_POST["submit"]))
{
  if (empty($_POST["name"]))
  {
    $error = "<label class='text-danger'>Enter Name</label>";
  }
  else if (empty($_POST["email"]))
  {
    $error = "<label class='text-danger'>Enter Email</label>";
  }
  else if (empty($_POST["username"]))
  {
    $error = "<label class='text-danger'>Enter Username</label>";
  }
  else if (empty($_POST["password"]))
  {
    $error = "<label class='text-danger'>Enter Password</label>";
    $array_data = json_decode($current_data, true);
    $extra = array(
      'name' => $_POST ['name']
      'email'=> $_POST ["email"]
      'username' => $_POST ["username"]
      'password' => $_POST ["password"]
    );
    $array_data[] = $extra;
    $final_data = json_encode($array_data);
    if (file_put_contents('user.json', $final_data))
    {
      $message = "<label class='text-success'>File Appended Success fully</p>";
    }
  }
  else {
    if (file_exists('user.json'))
    {
      $current_data = file_get_contents('employee_data.json')
    }
    else {
      $error='JSON File not exist'
    }
    }
  }
}
?>
