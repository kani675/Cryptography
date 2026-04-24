const http = require("http");
const fs = require("fs");

const PORT = 3000;

const server = http.createServer((req, res) => {

  // Always serve the single HTML file
  fs.readFile("c1.html", (err, data) => {
    if (err) {
      res.writeHead(500, { "Content-Type": "text/plain" });
      res.end("Error loading HTML file");
      return;
    }

    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(data);
  });

});

server.listen(PORT, () => {
  console.log("Server running at http://localhost:" + PORT);
});