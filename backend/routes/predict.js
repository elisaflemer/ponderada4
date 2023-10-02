const express = require('express');
const authenticate = require('../middleware/auth')
const predictValidate = require('../middleware/predictValidate.js')
const predictController = require('../controllers/predict')

const router = express.Router();

router.route('/').post(predictValidate.predict, authenticate.protect, predictController.predict)

module.exports = router;