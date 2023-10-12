import { useState, useEffect } from 'react';
import PlayerItem from './PlayerItem';
import styles from './PlayerList.module.css';
import { useContext } from 'react';
import { ThemeContext } from '../context/Contexts';

function PlayerList() {
  const [players, setPlayers] = useState([]);
  const theme = useContext(ThemeContext);

  async function fetchPlayers() {
    const response = await fetch('http://127.0.0.1:8000/players/all');
    const data = await response.json();
    setPlayers(data.data);
  }

  useEffect(() => {
    fetchPlayers();
  }, []);

  return (
    <div className={styles.players}>
      {players.map((player, index) => (
        <PlayerItem key={index} {...player} />
      ))}
    </div>
  );
}

export default PlayerList;
