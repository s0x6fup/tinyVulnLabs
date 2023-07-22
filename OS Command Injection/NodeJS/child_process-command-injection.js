const express = require('express');
const {exec} = require('child_process');
const app = express();
const port = 3000;

// Listen in on root
app.get('/', (req, res) => {
  const folder = req.query.folder;
  if (folder) {
    // Run the command with the parameter the user gives us
    exec(`ls -l ${folder}`, (error, stdout, stderr) => {
      let output = stdout;
      if (error) {
        // If there are any errors, show that
        output = error; 
      }
      res.send(
        {output: output, folder: folder}
      );
    });
  } else {
    res.send({message: 'nothing'});
  }
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});