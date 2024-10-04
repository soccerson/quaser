const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();

let db = new sqlite3.Database('./SQL/Test.db');  // SQLiteに接続

app.get('/api/data', (req, res) => {
  db.all('SELECT * FROM 対戦募集一覧', [], (err, rows) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ data: rows });  // データをJSON形式で返す
  });
});

app.listen(9001, () => {
  console.log('Server running on port 9001');
});