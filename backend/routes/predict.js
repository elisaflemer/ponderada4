const express = require('express');
const authenticate = require('../middleware/auth')
const predictController = require('../controllers/predict')

const router = express.Router();

router.route('/').post(authenticate.protect, predictController.predict)

module.exports = router;