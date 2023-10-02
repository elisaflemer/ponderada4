const User = require('../models/users');
const bcrypt = require('bcryptjs')
const jwt = require('jsonwebtoken')

const registerUser = async (user) => {
    const salt = await bcrypt.genSalt(10);
    user.password = await bcrypt.hash(user.password, salt)
    createdUser = await User.create(user);
    return createdUser;
}

const login = async (credentials) => {
    console.log(credentials)
    const user = await User.findOne({email: credentials.email})
    console.log(user)
    if(!user) {
        throw new Error("This email is not registered")
    }
    else if (bcrypt.compare(credentials.password, user.password)) {
        const token = generateJWT(user._id)
        return {
            name: user.name,
            email: user.email,
            token: token,
        }
    } else {
        throw new Error('Invalid credentials')
    }
}

const getMe = async (id) => {
    const me = await User.findById(id);
    if(!me) {
        throw new Error('User not found for this id')
    }
    return me
}

const generateJWT = (id) => {
    return jwt.sign({id: id}, process.env.JWT_SECRET, {
        expiresIn: '2m'
    })
}

module.exports = {
    registerUser,
    login,
    getMe
}