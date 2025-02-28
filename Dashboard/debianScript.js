var req = new XMLHttpRequest();
req.open('GET', '/debiandata');
req.onload = function(){
    var user = localStorage.getItem('EmailID');
    if(user == null || user == undefined || user == ""){
        plsLogIn();
    }else{
    var x = JSON.parse(req.response);
    var data = document.getElementById("data");
    var score = document.getElementById("scoreVal");
    var devicelist = document.getElementById("devicelist");
    var sideDevice = document.getElementById("sideDevice");
    var detailsAnalysis = document.getElementById("detailsAnalysis");
    for( i=0; i<x.length; i++){
        var dateString = x[i]["BenchmarkingTime"]; 
        var dateParts = dateString.split("/");
        var TempTime = new Date(dateParts[1]+'/'+dateParts[0]+'/'+dateParts[2]); 
        if(i==0){
            var LatestTime = TempTime;
            var LatestIndex = 0;
        }else{
            // && x[i]["UserID"] == localStorage.getItem('EmailID')
            if(TempTime > LatestTime)
            {
                LatestTime = TempTime;
                console.log(i);
                LatestIndex = i;
            }
        }
        console.log('Test Times' + TempTime + " " + LatestTime + " " + LatestIndex);
    }
    var totalComp = x[LatestIndex]["Compliant"].length;
    var totalNonComp = x[LatestIndex]["Not Compliant"].length;
    var testTime = x[LatestIndex]["BenchmarkingTime"];
    var platform = x[LatestIndex]["Platform"];
    var devid = x[LatestIndex]["DeviceID"];
    var total = totalComp + totalNonComp;
    score.innerHTML = totalComp + "/" + total;
    scorePercent = (totalComp/total)*100;
    scorePercent = Math.round((scorePercent + Number.EPSILON) * 100) / 100
    var statusScore = document.getElementById("statusScore");
    statusScore.innerHTML = scorePercent + "%<br> Compliant";
    if(scorePercent>=70){
        statusScore.style.color = '#5fc88b';
    }else if(scorePercent>=40 && scorePercent<70){
        statusScore.style.color = '#eeb37c';
    }else{
        statusScore.style.color = '#f15b5b';
    }
    data.innerHTML = "Test Conducted at:" + testTime + "<br>Plaform:" + platform + "<br>Device ID:" + devid;
    devicelist.innerHTML += devid;
    for(i=0 ; i<x.length; i++){
        sideDevice.innerHTML += "<li onclick=changeIndex("+ i +");>" + x[i]["DeviceID"] + "</li>";
    } 
    for(i=0 ; i<totalComp ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Compliant"][i] + "</td><td><span class='compliant'>Compliant</span><br></td></tr>";
    }
    for(i=0 ; i<totalNonComp ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Not Compliant"][i] + "</td><td><span class='noncompliant'>NonCompliant</span><br></td></tr>";
    }
    for(i=0 ; i<x[LatestIndex]["Info Compliant"].length ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Info Compliant"][i] + "</td><td><span class='notconfigured'>InfoCompliant</span><br></td></tr>";
    }
    for(i=0 ; i<x[LatestIndex]["Info NotCompliant"].length ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Info NotCompliant"][i] + "</td><td><span class='notconfigured'>InfoNotCompliant</span><br></td></tr>";
    }
    for(i=0 ; i<x[LatestIndex]["Info Manual"].length ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Info Manual"][i] + "</td><td><span class='notconfigured'>InfoManual</span><br></td></tr>";
    }
    console.log(x);
    }
}
function changeIndex(LatestIndex){
    var x = JSON.parse(req.response);
    var data = document.getElementById("data");
    var score = document.getElementById("scoreVal");
    var devicelist = document.getElementById("devicelist");
    var sideDevice = document.getElementById("sideDevice");
    var detailsAnalysis = document.getElementById("detailsAnalysis");
    var totalComp = x[LatestIndex]["Compliant"].length;
    var totalNonComp = x[LatestIndex]["Not Compliant"].length;
    var testTime = x[LatestIndex]["BenchmarkingTime"];
    var platform = x[LatestIndex]["Platform"];
    var devid = x[LatestIndex]["DeviceID"];
    var total = totalComp + totalNonComp;
    score.innerHTML = totalComp + "/" + total;
    scorePercent = (totalComp/total)*100;
    scorePercent = Math.round((scorePercent + Number.EPSILON) * 100) / 100
    var statusScore = document.getElementById("statusScore");
    statusScore.innerHTML = scorePercent + "%<br> Compliant";
    if(scorePercent>=70){
        statusScore.style.color = '#5fc88b';
    }else if(scorePercent>=40 && scorePercent<70){
        statusScore.style.color = '#eeb37c';
    }else{
        statusScore.style.color = '#f15b5b';
    }
    data.innerHTML = "Test Conducted at:" + testTime + "<br>Plaform:" + platform + "<br>Device ID:" + devid;
    devicelist.innerHTML = "<span>Your Devices</span><br><hr>";
    devicelist.innerHTML += devid;
    sideDevice.innerHTML = "Test History";
    for(i=0 ; i<x.length; i++){
        sideDevice.innerHTML += "<li onclick=changeIndex("+ i +");>" + x[i]["DeviceID"] + "</li>";
    } 
    detailsAnalysis.innerHTML="";
    for(i=0 ; i<totalComp ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Compliant"][i] + "</td><td><span class='compliant'>Compliant</span><br></td></tr>";
    }
    for(i=0 ; i<totalNonComp ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Not Compliant"][i] + "</td><td><span class='noncompliant'>NonCompliant</span><br></td></tr>";
    }
    for(i=0 ; i<x[LatestIndex]["Info Compliant"].length ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Info Compliant"][i] + "</td><td><span class='notconfigured'>InfoCompliant</span><br></td></tr>";
    }
    for(i=0 ; i<x[LatestIndex]["Info NotCompliant"].length ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Info NotCompliant"][i] + "</td><td><span class='notconfigured'>InfoNotCompliant</span><br></td></tr>";
    }
    for(i=0 ; i<x[LatestIndex]["Info Manual"].length ; i++){
        detailsAnalysis.innerHTML += "<tr><td>" + x[LatestIndex]["Info Manual"][i] + "</td><td><span class='notconfigured'>InfoManual</span><br></td></tr>";
    }
    console.log(x);
}
function plsLogIn(){
    var data = document.getElementById("data");
    var score = document.getElementById("scoreVal");
    var devicelist = document.getElementById("devicelist");
    var sideDevice = document.getElementById("sideDevice");
    var detailsAnalysis = document.getElementById("detailsAnalysis");
    var statusScore = document.getElementById("statusScore");
    data.innerHTML="Sign-In to view data";
    score.innerHTML="NA";
    devicelist.innerHTML="";
    sideDevice.innerHTML="Please Sign-In";
    detailsAnalysis.innerHTML="";
    statusScore.innerHTML="NA";
}
req.send();



