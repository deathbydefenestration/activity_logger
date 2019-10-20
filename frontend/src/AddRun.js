import React, { useState, useContext } from 'react'
// import PropTypes from 'prop-types'
import UserContext from './UserContext'
import ChangePageContext from './ChangePageContext'
import './App.css'
import axios from 'axios'


const AddRun = (props) => {
  const user = useContext(UserContext)
  const changePage = useContext(ChangePageContext)

  const [runDate, setRunDate] = useState('')
  const [runDistance, setRunDistance] = useState('')
  const [runDuration, setRunDuration] = useState('')

  const saveRun = async (event) => {
    event.preventDefault()
    const url = 'http://localhost:5000/api/activities'
    const payload = {
      'athlete_id': user.athlete_id,
      'operation': 'add',
      'activity_type': 'run',
      'activity_date': runDate,
      'activity_distance': runDistance,
      'activity_duration': runDuration
    }

    const axiosConfig = {
      headers: {
        'Content-Type': 'application/json;charset=UTF8',
        'Access-Control-Allow-Origin': '*'
      }
    }
    try {
      const response = await axios.post(url, payload, axiosConfig)
      loadAthleteRunLog(response.data)
    } catch (error) {
      // TODO: Error Gracefully
      console.log({error})
    }
  }
  
  const loadAthleteRunLog = (apiResponse=[]) => {
    changePage('AthleteRunLog', apiResponse)
  }

  return (
    <div>
      <h1>Add Run</h1>
      <form onSubmit={ saveRun }>
        <label>Date:</label>
        <input
          type='date'
          value={runDate}
          onChange={event => setRunDate(event.target.value)}
          required 
        />
        
        <label>Distance (m):</label>
        <input
          type='number'
          value={runDistance}
          onChange={event => setRunDistance(event.target.value)} 
          placeholder='Enter a number in metres, e.g. 5.04'
          required
        />
        
        <label>Duration (seconds):</label>
        <input
          type='number'
          value={runDuration}
          onChange={event => setRunDuration(event.target.value)}
          placeholder='Enter a number in seconds, e.g. 10.33'
          required
        />
        
        <input
          type='submit'
          value='Save'
        />
      </form>
    </div>
  )
}

export default AddRun
