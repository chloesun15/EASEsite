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

function CheckLog(user, pass, list){
  var arrayLength = list.length;
  for (var i = 0; i < arrayLength; i++) {
    if (user == list[i]["user"]){
      if (pass == list[i]["pass"]){
        window.location.replace("homepage.html");
        break
      }else {
          error();
          break
        }
      }
    else {
        error();
        break
    }
  }
}

function formChanged(){
  var user = document.getElementsByName("username")[0].value;
  var pass = document.getElementsByName("password")[0].value;
  var list = getList();
  CheckLog(user, pass, list)
}


function error(){
  document.getElementById("status").innerHTML = "<p> Wrong username or password, try again! </p>"
}

function getList() {
	var query = "https://api.myjson.com/bins/csi18";

	// We create a request, send it, and get back the response
	var userPass = new XMLHttpRequest();
	userPass.open('GET', query, false);
  userPass.send();

  // If there's an error, we'll bail out
  if(userPass.readyState != 4 || userPass.status != 200 || userPass.responseText === "") {
    window.console.error("Request had an error!");
    return;
  }

  // This takes the text response and creates a JSON object
  var loginfo = JSON.parse(userPass.responseText);
  return loginfo;
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
