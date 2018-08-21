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
  "<div class=\"dropdown\">"+
  "<a class= \"dropdown\"> diary</a>"+
      "<div class=\"dropdown-content\">"+
        "<a href=\"/diary/\">diary</a>"+
        "<a href=\"/show/\">archive</a>"+
      "</div>"+
    "</div>"+
  "<a href = \"/forum/\"> forum </a>"+
  "<a href = \"/resources/\"> resources </a>"+
  "<a href=\"/getsurvey/\"> survey<a>"+
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
