const express = require('express');
const userController = require('../controllers/users')
const userValidator = require('../middleware/usersValidate')
const authenticate = require('../middleware/auth')
const router = express.Router();

router.route('/').post(userValidator.create, userController.registerUser);

router.post('/login', userController.login);

router.get('/me', authenticate.protect, userController.getMe)

module.exports = router;