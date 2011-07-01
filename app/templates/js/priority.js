function getXMLHttpRequest() {
	try {
	  xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
	} catch (e) {
	  try {
	    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	  } catch (e2) {
	    xmlHttp = false;
	  }
	}
	if (!xmlHttp && typeof XMLHttpRequest != 'undefined') {
	  xmlHttp = new XMLHttpRequest();
	}	
	return xmlHttp;
}

function incPriority(id) {
	var xmlHttp = getXMLHttpRequest();	
	var url = "/requests/"; 
	xmlHttp.open("POST", url, true);
	xmlHttp.onreadystatechange = updatePage;
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
	xmlHttp.setRequestHeader("X_REQUESTED_WITH", "XMLHttpRequest");
	xmlHttp.send("id=" + id + "&csrfmiddlewaretoken=" + token);
}

function updatePage() {	
	if (xmlHttp.readyState == 4) {
		if (xmlHttp.status == 200) {		
			var response = xmlHttp.responseText;
			var mass = response.split(";");
			var id = mass[0];
			var priority = mass[1];
			document.getElementById(id).innerHTML = priority;
		}
	}
}