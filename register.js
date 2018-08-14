function OnStart(){
  alert("Hello world");
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

function registerChanged(){
  var user = document.getElementsByName("username")[0].value;
  var pass = document.getElementsByName("password")[0].value;
  var name = document.getElementsByName("name")[0].value;
  var email = document.getElementsByName("email")[0].value;
  var list = getList();
  var query = "https://api.myjson.com/bins/csi18";

	// We create a request, send it, and get back the response
	var userPass = new XMLHttpRequest();
	userPass.open('POST', query, false);
  userPass.push(list);
  userPass.send();
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
