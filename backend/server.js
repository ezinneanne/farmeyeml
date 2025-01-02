const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const { spawn } = require("child_process");

const app = express();
const PORT = 5000;

app.use(bodyParser.json());
app.use(cors());

// Route to handle ML predictions
app.post("/predict", (req, res) => {
    const inputData = req.body;

    // Call the Python script
    const python = spawn("python", ["ml-predict/ml-api.py", JSON.stringify(inputData)]);

    let result = "";
    python.stdout.on("data", (data) => {
        result += data.toString();
    });

    python.stderr.on("data", (data) => {
        console.error(`Python error: ${data}`);
    });

    python.on("close", (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: "Python script failed" });
        }

        try {
            const output = JSON.parse(result);
            res.json(output);
        } catch (error) {
            res.status(500).json({ error: "Failed to parse Python response" });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
