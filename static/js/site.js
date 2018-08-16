function start(){
  navMenu();
}


function navMenu(){
  document.getElementById("navMenu").innerHTML =
  "<div class = \"navfloat\">"+
  "<ul>"+
  "<a href = \" /about/ \"> about </a>"+
  "<a href = \"/chat/\"> chat</a>"+
  "<a href = \"/diary/\"> diary</a>"+
  "<a href = \"/forum/\"> forum </a>"+
  "<a href = \"/resources/\"> resources </a>"+
  "</ul>"+
  "</div>";
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
