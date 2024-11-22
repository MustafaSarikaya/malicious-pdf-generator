const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Chemin vers le fichier à télécharger
const filePath = path.join(__dirname, 'c2_client.py');

// Route principale pour télécharger automatiquement le fichier
app.get('/', (req, res) => {
  res.setHeader('Content-Disposition', 'attachment; filename=c2_client.py');
  res.sendFile(filePath);
});

// Démarrer le serveur
app.listen(PORT, () => {
  console.log(`Serveur lancé sur http://localhost:${PORT}`);
});
