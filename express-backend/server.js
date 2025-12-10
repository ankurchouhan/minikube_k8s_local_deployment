const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/api/message", (req, res) => {
  res.json({ message: "Hello from Express backend running in Kubernetes!" });
});

app.get("/", (req, res) => {
  res.send("Express backend is up. Try /api/message");
});

app.listen(PORT, () => {
  console.log(`Express backend listening on port ${PORT}`);
});
