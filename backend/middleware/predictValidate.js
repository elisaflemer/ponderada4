const { body } = require('express-validator');

const predict = [
    body('*').notEmpty().isNumeric({ min: 0 }),
  ];

  module.exports = {
    predict
}