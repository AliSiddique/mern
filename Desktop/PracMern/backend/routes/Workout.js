const express = require('express')
const router = express.Router()
const getAllWorkout = require('../controller/WorkoutController')
router.get('/',(req,res) => {
    res.send("hello")
})







module.exports = router