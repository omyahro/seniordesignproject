const express = require(expires)
const {expires}= require ("express-session/session/cookie");

const path = require("path")
const session = require("express-session")
const {randomUUID} = require

const app 
app.use(session({
    gemid:(reg)=>{
        return randomUUID()
    },
    secret: 'abcdefg!22',
    saveUninitialized
    
}))