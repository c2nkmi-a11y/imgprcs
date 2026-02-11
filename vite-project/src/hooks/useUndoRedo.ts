import {useState} from 'react';

export function useUndoRedo<T>(initialState: T) {
  const [state, setState] = useState<T>(initialState);
  const [history, setHistory] = useState<T[]>([]);
  const [future, setFuture] = useState<T[]>([]);

  const undo =() => {
    if (history.length === 0) return;
    const prevState = history[history.length - 1];
    setFuture([state, ...future]);
    setState(prevState);
    setHistory(history.slice(0, -1));
  }

  const redo =() => {
    if (future.length === 0) return;
    const nextState = future[0];
    setHistory([...history, state]);
    setState(nextState);
    setFuture(future.slice(1));
  }

  const saveState = (newState: T) => {
    setHistory([...history, state]);
    setState(newState);
  }

  return { state, undo, redo, saveState };
}