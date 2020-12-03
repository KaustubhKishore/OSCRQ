var req = new XMLHttpRequest();
req.open('GET', 'http://localhost:3000/data');
req.onload = function(){
    var x = JSON.parse(req.response);
    var data = document.getElementById("data");
    var score = document.getElementById("scoreVal");
    var devicelist = document.getElementById("devicelist");
    var sideDevice = document.getElementById("sideDevice");
    var detailsAnalysis = document.getElementById("detailsAnalysis");
    var LatestIndex = 0;
    for( i=0; i<x.length; i++){
        var dateString = x[i]["TestTime"]; 
        var dateParts = dateString.split("/");
        var TempTime = new Date(dateParts[1]+'/'+dateParts[0]+'/'+dateParts[2]); 
        var LatestTime = new Date(Date.now());
        if(i==0){
            LatestTime = TempTime;
        }else{
            if(TempTime > LatestTime)
            {
                LatestTime = TempTime;
                LatestIndex = i;
            }
        }
    }
    var totalComp = x[LatestIndex]["Compliant"].length;
    var totalNonComp = x[LatestIndex]["Non Compliant"].length;
    var testTime = x[LatestIndex]["TestTime"];
    var platform = x[LatestIndex]["Platform"];
    var devid = x[LatestIndex]["DeviceID"];
    var total = totalComp + totalNonComp;
    score.innerHTML = totalComp + "/" + total;
    data.innerHTML = "Test Conducted at:" + testTime + "<br>Plaform:" + platform + "<br>Device ID:" + devid + "<hr>";
    devicelist.innerHTML += devid;
    for(i=0 ; i<x.length; i++){
        sideDevice.innerHTML += "<li>" + devid + "</li>";
    } 
    for(i=0 ; i<totalComp ; i++){
        detailsAnalysis.innerHTML += x[0]["Compliant"][i] + " | Status: Compliant<br>";
    }
    for(i=0 ; i<totalNonComp ; i++){
        if (x[0]["Not Configured"].includes(x[0]["Non Compliant"][i])){
            detailsAnalysis.innerHTML += x[0]["Non Compliant"][i] + " | Status: Not Configured - Non Compliant<br>";
        }
        else{
            detailsAnalysis.innerHTML += x[0]["Non Compliant"][i] + " | Status: Non Compliant<br>";
        }
    }
    console.log(x);
}
req.send();


