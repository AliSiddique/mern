const express = require('express')
const mongoose = require('mongoose')
require('dotenv').config()
const app = express()
const PORT =  4000
const WorkoutRoutes = require('./routes/Workout')

app.use('/api/workouts',WorkoutRoutes)


mongoose.connect(process.env.MONGO_URI)
.then(() => {
    app.listen(PORT,() => {
        console.log("Listening on port " + PORT + " and connected to database")
    })
    
})
.catch(error => console.log(error))


