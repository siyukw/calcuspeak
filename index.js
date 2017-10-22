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
		step2.open("POST", "src/calculator.py");
		var step2Error = function() {
		    console.log("Could not convert to solution");
		};
		step2.onload = function() {
		    if(this.status >= 200 && this.status < 300) {
			var step3 = new XMLHttpRequest();
			step3.open("POST", "src/textToAudio.py");
			var step3Error = function() {
			    console.log("Could not output audio");
			};
			step3.onload = function() {
			    if(this.status >= 200 && this.status < 300) {
				console.log(this.responseText);
			    } else {
				step3Error();
			    }
			}
			step3.onerror = step3Error;
			var step3InputData = new FormData();
			step3InputData.append("text", this.responseText);
			step3.send(step3InputData);
		    } else {
			step2Error();
		    }
		};
		step2.onerror = step2Error;
		var step2InputData = new FormData();
		step2InputData.append("text", this.responseText);
		step2.send(step2InputData);
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
