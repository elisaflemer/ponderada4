const { body } = require('express-validator');

const create = [body('name').not().isEmpty().withMessage('The name field is required'),
                body('email').not().isEmpty().withMessage('The email field is required').isEmail().withMessage('This is not a valid email'),
                body('password').not().isEmpty().withMessage('The password is required')]

module.exports = {
    create
}