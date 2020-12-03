const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
var MongoClient = require('mongodb').MongoClient

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// mongodb+srv://Sanya:4wUubuaMachwQ9rn@cluster0.9w3mr.mongodb.net/OSCARQ?retryWrites=true&w=majority
MongoClient.connect('mongodb://localhost:27017', function (err, client) {
  if (err) throw err

  var db = client.db('OSCARQ')

  // generic get - gets all values 
  app.get("/", (req, res) => {
    db.collection('Windows').find().toArray(function (err, result) {
      if (err) throw err
      res.send(result);
      // console.log(result)
    })
  });

  app.post("/windows", (req, res) => {
    var COMPLIANT = req.body.COMPLIANT;
    var NONCOMPLIANT = req.body.NONCOMPLIANT;
    var NOTCONFIGURED = req.body.NOTCONFIGURED;
    Results = { 
      "Message":"This is a test! ~Vaibhav",
      "Compliant":COMPLIANT,
      "Non Compliant":NONCOMPLIANT,
      "Not Configured":NOTCONFIGURED
      }
    db.collection('Windows').insertOne(Results); 
    res.end("Data Inserted");
  });
  
})

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});