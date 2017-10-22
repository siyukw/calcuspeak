(function () {
    window.onload = function() {
	document.getElementById("button").onclick = click;
    };

    function click() {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "src/main.php");
	var error = function() {
	    console.log("Server error");
	};
	xhr.onload = function() {
	    if(this.status < 200 || this.status >= 300) {
		error();
	    } else {
		console.log(this.responseText);
	    }
	};
	xhr.onerror = error;
	console.log("starting.");
	xhr.send();
    }
})();
