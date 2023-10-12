import styles from './PlayerItem.module.css';

function PlayerItem(props) {
  return (
    <div className={styles.item}>
      <div className={styles.playerImage}>
        <img src={props.image} />
      </div>

      <div className={styles.info}>
        <h2>{props.first_name}</h2>
        <p>{props.last_name}</p>
        <p>{props.nickname}</p>
        <p>{props.position}</p>
        <p>{props.number}</p>
      </div>
    </div>
  );
}

export default PlayerItem;
