const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;


const filePath = path.join(__dirname, 'c2_client.py');


app.get('/', (req, res) => {
  res.setHeader('Content-Disposition', 'attachment; filename=c2_client.py');
  res.sendFile(filePath);
});


app.listen(PORT, () => {
  console.log(`Launch server http://localhost:${PORT}`);
});
