const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const { ObjectId, ObjectID } = require("bson");

const app = express();
var MongoClient = require('mongodb').MongoClient

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// mongodb+srv://Sanya:4wUubuaMachwQ9rn@cluster0.9w3mr.mongodb.net/OSCARQ?retryWrites=true&w=majority
// mongodb://localhost:27017
MongoClient.connect('mongodb+srv://Sanya:4wUubuaMachwQ9rn@cluster0.9w3mr.mongodb.net/OSCARQ?retryWrites=true&w=majority', function (err, client) {
  if (err) throw err

  var db = client.db('OSCARQ')

  // generic get - gets all data from **Windows** collection
  app.get("/windowsdata", (req, res) => {
    db.collection('Windows').find().toArray(function (err, result) {
      if (err) throw err
      res.send(result);
      // console.log(result)
    })
  });

  // generic get - gets all data from **Debian** collection
  app.get("/debiandata", (req, res) => {
    db.collection('Debian').find().toArray(function (err, result) {
      if (err) throw err
      res.send(result);
      // console.log(result)
    })
  });

  // windows sample post method
  app.post("/windows", (req, res) => {
    var COMPLIANT = req.body.COMPLIANT;
    var NONCOMPLIANT = req.body.NONCOMPLIANT;
    var NOTCONFIGURED = req.body.NOTCONFIGURED;
    var userID = req.body.UserID;
    var macAdd = req.body.DeviceID;
    var platVer = req.body.Platform;
    var dt_string = req.body.TestTime;
    Results = { 
        "UserID":userID,
        "DeviceID":macAdd,
        "Platform":platVer,
        "TestTime":dt_string,
        "Compliant":COMPLIANT,
        "Non Compliant":NONCOMPLIANT,
        "Not Configured":NOTCONFIGURED
      }
    db.collection('Windows').insertOne(Results); 
    res.end("Data Inserted");
  });

  //windows sample update method
  app.put("/updatewin/:id" , (req, res) =>{
    id = req.params;
    try{
    db.collection('Windows').updateOne(
      { "_id": id },
      {
        $push: { "TestTime" : "03/12/2020 13:21:37" }
      }
    ); 
    } catch (e) {
      print (e);
    }
    res.end("Entry Updated"); 
  });

  //windows sample delete method
  app.delete("/deletewin" , (req, res) => {
    try {
      db.collection('Windows').deleteOne(
          { "_id" : ObjectId("5fc7676457eb5e533af60afa") }
      );
    } catch (e) {
      res.send (e);
    }
  })
});
app.use(express.static(__dirname));
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});



