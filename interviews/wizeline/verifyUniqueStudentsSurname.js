const async = require('async');
const axios = require('axios');
const chai = require('chai');
const chai_http = require('chai-http');
const co = require('co');
const connect = require('connect');
const debug = require('debug');
const express = require('express');
const forever = require('forever');
const futil = require('futil');
const http = require('http');
const ip_router = require('ip-router');
const ip_to_int = require('ip-to-int');
const ipaddr_js = require('ipaddr.js');
const jquery = require('jquery');
const lodash = require('lodash');
const mocha = require('mocha');
const mongodb = require('mongodb');
const mongoose = require('mongoose');
const mssql = require('mssql');
const mysql = require('mysql');
const mysql2 = require('mysql2');
const node_fetch = require('node-fetch');
const pg = require('pg');
const rambda = require('rambda');
const request = require('request');

const HOST_URL = 'http://localhost';
const GET_STUDENTS_LIST_ENDPOINT = `${HOST_URL}/studentList`; 
const GET_STUDENT_DATA_ENDPOINT = `${HOST_URL}/student?student_id=`;

/* const STUDENTS_LIST = await (async () => {
    const RESPONSE = await axios.get(GET_STUDENTS_LIST_ENDPOINT);
    console.log('>>> RESPONSE', RESPONSE);
    return RESPONSE?.data;
}) */

axios.get(GET_STUDENTS_LIST_ENDPOINT).then((res) => {
    const RESPONSE = res?.data;
    const STUDENTS_IDS = RESPONSE?.ids
    const AUXILIAR_SURNAMES_CHECKER = {};
    var OUTPUT = true;
    
    STUDENTS_IDS.forEach((STUDENT_ID) => {
        const GET_SPECIFIC_STUDENT_ENDPOINT = `${GET_STUDENT_DATA_ENDPOINT}${STUDENT_ID}`;
        axios.get(GET_SPECIFIC_STUDENT_ENDPOINT).then((res) => {
            const RESPONSE = res?.data;
            const STUDENTS_DATA = RESPONSE;
            console.log('>>> STUDENTS_DATA', STUDENTS_DATA?.surname);
            if(!AUXILIAR_SURNAMES_CHECKER.hasOwnProperty(STUDENTS_DATA?.surname)){
                AUXILIAR_SURNAMES_CHECKER[STUDENTS_DATA?.surname] = true;
            } else {
                OUTPUT = false;
                this.break;
            }
        })
    })  
    console.log(OUTPUT ? 'The class can be divided' : 'The class can be divided');
});

