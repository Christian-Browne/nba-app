import PlayerList from './components/PlayerList';
import { ThemeContext } from './context/Contexts';
import { useState } from 'react';

function App() {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={theme}>
      <PlayerList />
    </ThemeContext.Provider>
  );
}

export default App;
