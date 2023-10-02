const jwt = require('jsonwebtoken')

const protect = (async (req, res, next) => {
    try {
        if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
            const token = req.headers.authorization.split(' ')[1]
            const decoded = jwt.verify(token, process.env.JWT_SECRET)
            req.user_id = decoded.id
            next()


        } else {
            throw new Error('No authorization token')
        }
    } catch (err) {
        next(err);
    }
})


module.exports = { protect }