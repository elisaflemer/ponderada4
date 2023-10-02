const { validationResult } = require('express-validator')
const predictService = require('../services/predict')

const predict = async (req, res, next) => {
    try {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return next(errors.array()[0])
        }
        const prediction = await predictService.predict(req.body)
        return res.status(200).json({ prediction: prediction })
    } catch (err) {
        return next(err)
    }
}

module.exports = {
    predict
}