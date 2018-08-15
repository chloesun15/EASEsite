function start(){
  navMenu();
  foot();
}
function start2(){
  navMenu();
  var information = getTemperature();
	var temperature = information["currently"]["temperature"];
  var summary = information["currently"]["summary"];
  document.getElementById("temp").innerHTML = temperature;
  document.getElementById("desc").innerHTML = summary;
}

function showAlert(){
  alert("HelloWorld!")
}

function foot(){
  document.getElementById("standardFoot").innerHTML =
  "<br>"+
  "<div>"+
  "<img width=\"40px\" height=\"40px\" src=https://cdn3.iconfinder.com/data/icons/transparent-on-dark-grey/500/icon-04-512.png></img>"+
  "<p>"+
    "instagram: @chile.sun"+
  "<br>"+
  "questions or concerns? email us at <a href=\"mailto:chloesun15@gmail.com\">chloesun15@gmail.com</a>"+
  "</div>";
}

function navMenu(){
  document.getElementById("navMenu").innerHTML =
  "<h1>"+
  "let's do some good!"+
  "</h1>"+
  // "<h3 id="txt"></h3>"+
  "<h2 id=center>"+
  "resources for teens for living conciously and ethically"+
  "</h2>"+
  "<div class = \"navfloat\">"+
  "<a href = \"starting.html\"> easy ways to start</a>"+
  "<a href = \"volunteering.html\"> volunteering</a>"+
  "<a href = \"buying.html\"> ethical consumerism </a>"+
  // "<div class=\"search-container\">"+
  //    "<form action=\"/action_page.php\">"+
  //      "<input type = \"text\" style=\"width=4px\" placeholder= \"search...\" name=\"search\">"+
  //      "<button type=\"submit\"><i class=\"fa fa-search\"></i></button>"+
  //   "</form>"+
  //  "</div>"
   "</div>";
}

function getTemperature() {
	var apiKey = "9a8ebdb56bb327df5dce8916a082676e";
	var lon = 40.7128;
	var lat = 74.0060;

	// query template:
	// https://api.darksky.net/forecast/[key]/[latitude],[longitude]
	//query example:
	// https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589
  var proxy = 'https://cors-anywhere.herokuapp.com/';
	var query = "https://api.darksky.net/forecast/9a8ebdb56bb327df5dce8916a082676e/40.7128,-74.0060";

	// We create a request, send it, and get back the response
	var weatherRequest = new XMLHttpRequest();
	weatherRequest.open('GET', proxy + query, false);

	weatherRequest.send();

	// If there's an error, we'll bail out
	if(weatherRequest.readyState != 4 || weatherRequest.status != 200 || weatherRequest.responseText === "") {
	 	window.console.error("Request had an error!");
	 	return;
	}

	// This takes the text response and creates a JSON object
	var weatherInformation = JSON.parse(weatherRequest.responseText);
  return weatherInformation;

}
