var req = new XMLHttpRequest();
req.open('GET', 'http://localhost:3000/data');
req.onload = function(){
    var x = JSON.parse(req.response);
    var data = document.getElementById("data");
    var score = document.getElementById("scoreVal");
    var devicelist = document.getElementById("devicelist");
    var sideDevice = document.getElementById("sideDevice");
    var detailsAnalysis = document.getElementById("detailsAnalysis");
    for( i=0; i<x.length; i++){
        var dateString = x[i]["TestTime"]; 
        var dateParts = dateString.split("/");
        var TempTime = new Date(dateParts[1]+'/'+dateParts[0]+'/'+dateParts[2]); 
        if(i==0){
            var LatestTime = TempTime;
            var LatestIndex = 0;
        }else{
            if(TempTime > LatestTime)
            {
                LatestTime = TempTime;
                console.log(i);
                LatestIndex = i;
            }
        }
        console.log('herrrrrrrrrrrreeeee' + TempTime + " " + LatestTime + " " + LatestIndex);
    }
    var totalComp = x[LatestIndex]["Compliant"].length;
    var totalNonComp = x[LatestIndex]["Non Compliant"].length;
    var testTime = x[LatestIndex]["TestTime"];
    var platform = x[LatestIndex]["Platform"];
    var devid = x[LatestIndex]["DeviceID"];
    var total = totalComp + totalNonComp;
    score.innerHTML = totalComp + "/" + total;
    data.innerHTML = "Test Conducted at:" + testTime + "<br>Plaform:" + platform + "<br>Device ID:" + devid;
    devicelist.innerHTML += devid;
    for(i=0 ; i<x.length; i++){
        sideDevice.innerHTML += "<li>" + devid + "</li>";
    } 
    for(i=0 ; i<totalComp ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Compliant"][i] + "</td><td><span class='compliant'>Compliant</span><br></td></tr>";
    }
    for(i=0 ; i<totalNonComp ; i++){
        if (x[LatestIndex]["Not Configured"].includes(x[LatestIndex]["Non Compliant"][i])){
            detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Non Compliant"][i] + "</td><td><span class='notconfigured'>NotConfigured</span> <br> <span class='noncompliant'>NonCompliant</span><br></td></tr>";
        }
        else{
            detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Non Compliant"][i] + "</td><td><span class='noncompliant'>NonCompliant</span><br></td></tr>";
        }
    }
    console.log(x);
}
req.send();

