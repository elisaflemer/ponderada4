const { validationResult } = require('express-validator')
const userServices = require('../services/users')

const registerUser = async (req, res, next) => {
    try {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return next(errors.array()[0])
        }
        const registeredUser = await userServices.registerUser(req.body)
        return res.status(201).json({ registeredUser: registeredUser })
    } catch (err) {
        return next(err)
    }
}

const login = async (req, res, next) => {
    try {
        const user = await userServices.login(req.body)
        return res.status(200).json(user)
    } catch (err) {
        return next(err)
    }
}

const getMe = async (req, res) => {
    try {
        const me = await userServices.getMe(req.user_id)
        return res.status(200).json(me);

    } catch (err) {
        return next(err)
    }
}

module.exports = {
    registerUser,
    login,
    getMe
}