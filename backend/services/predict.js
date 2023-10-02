const util = require("util");
const { exec } = require("child_process");
const fs = require("fs");

const execPromise = util.promisify(exec);

const predict = async (data) => {
  fs.writeFileSync("services/input.json", JSON.stringify(data));

  try {
    console.log('oi')
    // Execute a Python script to make predictions using a promise
    const { stdout, stderr } = await execPromise("python services/predict.py");
    
    // Read and send back the prediction results
    const predictions = fs.readFileSync("services/output.txt", "utf-8");
    console.log(predictions)
    return predictions;
  } catch (error) {
    console.error(`Error: ${error.message}`);
    throw new Error("Something went wrong");
  }
};

module.exports = {
  predict,
};
