var req = new XMLHttpRequest();
req.open('GET', 'http://localhost:3000');
req.onload = function(){
    var x = JSON.parse(req.response);
    var data = document.getElementById("data");
    var score = document.getElementById("scoreVal");
    var totalComp = x[0]["Compliant"].length;
    var totalNonComp = x[0]["Non Compliant"].length;
    var total = totalComp + totalNonComp;
    for(i=0 ; i<x.length; i++){
        score.innerHTML = totalComp + "/" + total;
        // data.innerHTML = x[i]["Non Compliant"];
    }
    console.log(x);
}
req.send();