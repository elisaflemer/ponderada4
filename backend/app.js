const express = require('express');
const cors = require('cors');
const usersRouter = require('./routes/users')
const predictRouter = require('./routes/predict')
const errorHandler = require('./middleware/error')
const app = express();

app.use(cors())
app.use(express.json());
app.use(express.urlencoded({extended: true}))
app.use('/api/users', usersRouter)
app.use('/api/predict', predictRouter)
app.use(errorHandler.errorHandler)

module.exports = app;