import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [playerName] = useState('Princess Peach')
  return (
    <div className="cssClassName">
      <h1>Hello World { playerName }!</h1>
    </div>
  );
}

export default App;
