function start(){
  navMenu();
  logout();
}


function navMenu(){
  document.getElementById("navMenu").innerHTML =
  "<div class = \"navfloat\">"+
  "<ul>"+
  "<a href = \" /about/ \"> about us </a>"+
  "<a href = \"/chat/\"> chat</a>"+
  "<a href = \"/diary/\"> diary</a>"+
  "<a href = \"/forum/\"> forum </a>"+
  "<a href = \"/resources/\"> resources </a>"+
  "</ul>"+
  "</div>";
}

function logout(){
  document.getElementById("logout").innerHTML =
  "<a id = \"right\" href=\"/logout/\">logout</a>";
}

function redirect()
{
  var url = "http://www.google.com";
  window.location(url);
}
function enteredwords(){
  var enteredwords = document.getElementById("Start typing...").value;
  if(enteredwords === "")
  return;
}
