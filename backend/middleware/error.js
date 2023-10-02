/* 
ERROR STRUCTURE
{
    error: {
        message:
        details: {

        }
    }
}
*/

const errorHandler = (err, req, res, next) => {
    const errorObject = {
        message: undefined,
        details: undefined
    };
    console.log(JSON.stringify(err));
    if (err.msg) {
        errorObject.message = err.msg;
        errorObject.details = {
            field: err.param,
            value: err.value
        };
        res.status(400);
    } else if (err.code === 11000) {
        const field = Object.keys(err.keyValue)[0];
        const value = Object.values(err.keyValue)[0];
        const message = `An entry with that ${field} (${value}) already exists.`;
        errorObject.message = message;
        res.status(409);
    } else if (err.status === 403) {
        // Handle forbidden errors (HTTP status code 403) here
        errorObject.message = "Forbidden";
        res.status(403);
    } else {
        errorObject.message = err.message;
        res.status(400);
    }
    res.json({ error: errorObject });
};

module.exports = {
    errorHandler
};
