function OnStart(){
  alert("Hello world");
  getList();
}

function CheckLog(user, pass){
  var userName = ["kittykat", "user"];
  var userPass = ["qwerty", "password"];
  var arrayLength = userName.length;
  for (var i = 0; i < arrayLength; i++) {
    if (user == userName[i]){
      if (pass == userPass[i]){
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
  CheckLog(user, pass)
}

function registerChanged(){
  var user = document.getElementsByName("username")[0].value;
  var pass = document.getElementsByName("password")[0].value;
  var name = document.getElementsByName("name")[0].value;
  var email = document.getElementsByName("email")[0].value;
}

function error(){
  document.getElementById("status").innerHTML = "<p> Wrong username or password, try again! </p>"
}

function getList() {
  alert("running!");
	var query = "file:///C:/Users/Girls%20Who%20Code/Documents/GitHub/easewebsite/userinfo.json";

	// We create a request, send it, and get back the response
	var userPass = new XMLHttpRequest();
	userPass.open('GET', query, false);
	userPass.onreadystatechange = function()
  {
    if (userPass.readyState === 4)
    {
      if(userPass.status === 200 || userPass.status == 0)
      {
        var allText = userPass.responseText;
        alert(allText);
      }
    }
  userPass.send(null);
  // This takes the text response and creates a JSON object
	var allAcc = JSON.parse(userPass.responseText);
  alert(allAcc)
}
}
