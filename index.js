(function () {
    //var rec = new Recorder(MediaDevices.getUserMedia());
    window.onload = function() {
	document.getElementById("button").onclick = startRecord;
    };

    function startRecord() {
	var step1 = new XMLHttpRequest();
	step1.open("GET", "src/audioToText.py");
	var step1Error = function() {
	    console.log("Could not record from mic");
	};
	step1.onload = function() {
	    if(this.status >= 200 && this.status < 300) {
		var step2 = new XMLHttpRequest();
		var input = this.responseText;
		step2.open("POST", "src/calculator.py");
		var step2Error = function() {
		    console.log("Could not convert to solution");
		};
		step2.onload = function() {
		    if(this.status >= 200 && this.status < 300) {
			console.log(this.responseText);
		    } else {
			step2Error();
		    }
		};
		step2.onerror = step2Error;
		var inputData = new FormData();
		inputData.append("text", this.responseText);
		step2.send(inputData);
	    } else {
		step1Error();
	    }
	};
	step1.onerror = step1Error;
	step1.send();
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
