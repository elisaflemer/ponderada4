const express = require('express');
const userController = require('../controllers/users')
const authenticate = require('../middleware/auth')
const router = express.Router();

router.route('/').post(userController.registerUser);

router.post('/login', userController.login);

router.get('/me', authenticate.protect, userController.getMe)

module.exports = router;