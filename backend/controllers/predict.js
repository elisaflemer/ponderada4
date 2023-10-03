const predictService = require('../services/predict')

const predict = async (req, res, next) => {
    try {
        const prediction = await predictService.predict(req.body)
        return res.status(200).json({ prediction: prediction })
    } catch (err) {
        return next(err)
    }
}

module.exports = {
    predict
}