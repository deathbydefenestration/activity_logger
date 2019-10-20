import React, { useContext } from 'react'
import PropTypes from 'prop-types'
import ChangePageContext from './ChangePageContext'
import './App.css';

// Example Response:
//  [
//    {'athlete_id': '1', 'calories_burned': '50.191', 'date': '2019-09-27', 'distance': '100.00', 'duration': '10.83', 'id': '1', 'type': 'run'},
//    {'athlete_id': '1', 'calories_burned': '51.232', 'date': '2019-09-29', 'distance': '102.00', 'duration': '14.23', 'id': '2', 'type': 'run'},
//    {'athlete_id': '1', 'calories_burned': '53.55', 'date': '2019-09-30', 'distance': '103.00', 'duration': '13.62', 'id': '3', 'type': 'run'}
//   ]

const AthleteRunLog = (props) => {
  const COLUMNS = ['Date', 'Distance', 'Duration', 'Calories Burned']
  const changePage = useContext(ChangePageContext)
  let { athleteLog } = props 

  // Todo: ensure athleteLog is passed in correctly, so this isn't required
  if ((!Array.isArray(athleteLog) || athleteLog === undefined) || athleteLog.length === 0) {
    athleteLog = null
  }

  const setPageToAddRun = () => {
    changePage('AddRun')
  }
  
  const renderHeaderOrBlankColumns = (headers=true) => {
    let rowColumns = []
      for (let column of COLUMNS) {
        rowColumns.push(<td>{ headers ? column : '-' }</td>) 
      }
    return rowColumns
  }

  return (
    <div>
      <h1>My Runs</h1>
      <table>
        <tbody>
          <tr>
            { renderHeaderOrBlankColumns() }
          </tr>
          { athleteLog ? athleteLog.map((activity, key) => {
              return (
              <tr key = {activity.id}>
                <td>{activity.date}</td>
                <td>{activity.distance}</td>
                <td>{activity.duration}</td>
                <td>{activity.calories_burned}</td>
              </tr>
              )
            }) : renderHeaderOrBlankColumns(false)
          }
        </tbody>
      </table>
      <button onClick={setPageToAddRun}>Add Run</button>
    </div>
  );
}

AthleteRunLog.prototypes = {
  athleteLog: PropTypes.array
}

export default AthleteRunLog;
