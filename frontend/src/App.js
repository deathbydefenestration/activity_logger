import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import UserContext from './UserContext'
import ChangePageContext from './ChangePageContext'
import './App.css'
import AthleteRunLog from './AthleteLog'
import AddRun from './AddRun'


const App = (props) => {
  const { user } = props
  const [activePage, setActivePage] = useState('AddRun')
  const [athleteLog, setAthleteLog] = useState([])

  const changePage = (newPage, apiResponse=null) => {
    if (apiResponse) {
      setAthleteLog(apiResponse)
    }    
    setActivePage(newPage)
  }

  useEffect(() => { changePage(activePage) }, [activePage])

  const AddRunWithContext = () => {
    return (
      <UserContext.Provider value={user}>
        <ChangePageContext.Provider value={changePage}>
          <AddRun />
        </ChangePageContext.Provider>
      </UserContext.Provider>
    )
  }
  
  const AthleteRunLogWithContext = () => {
    return (
      <ChangePageContext.Provider value={changePage}>
        <AthleteRunLog athleteLog={athleteLog} />
      </ChangePageContext.Provider>
    )
  }

  return (
    <div>
      {(activePage === 'AddRun') && <AddRunWithContext /> }
      {(activePage === 'AthleteRunLog') && <AthleteRunLogWithContext /> }
    </div>
  )
}

App.propTypes = {
  user: PropTypes.object,
}

export default App
