(function () {
    //var rec = new Recorder(MediaDevices.getUserMedia());
    window.onload = function() {
	document.getElementById("button").onclick = startRecord;
    };

    function startRecord() {
	var step1 = new XMLHttpRequest();
	step1.open("GET", "src/speechToText.py");
	step1.onload = new function() {
	    if(this.status >= 200 && this.status < 300) {
		var step2 = new XMLHttpRequest();
		var input = this.responseText;
		step2.open("POST", "src/calculator.py");
		step2.onload = new function() {
		    if(this.status >= 200 && this.status < 300) {
			console.log(this.responseText);
		    } else {
			step2.onerror();
		    }
		};
		step2.onerror = new function() {
		    console.log("Could not convert to solution");
		};
		var inputData = new FormData();
		inputData.append("text", this.responseText);
		step2.send(inputData);
	    } else {
		step1.onerror();
	    }
	};
	step1.onerror = function() {
	    console.log("Could not record from mic");
	};
	//rec.record();
	//document.getElementById("button").onclick = stopRecord;
    }
/*
    function stopRecord() {
	rec.stop();
	rec.exportWAV(calculate);
	rec.clear();
	document.getElementById("button").onclick = startRecord;
    }

    function calculate(wav) {
	
    }
*/
})();
