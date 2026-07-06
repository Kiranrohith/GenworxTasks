import { useState, type ReactNode } from 'react';

export default function MyComponents() {
  const [count, setCount] = useState(0);

  function increment() {
    setCount(count + 1);
  }
  function decrement() {
    setCount(count - 1);
  }
  function reset() {
    setCount(0);
  }

  return (
    <div >
        <div style={{backgroundColor:"whitesmoke", width:"100%", height:"100%", display:"flex", justifyContent:"center", alignItems:"center", flexDirection:"column"  }}>  
          <h1>Counter</h1>
          <p style={{fontSize:"4rem", marginBottom:"35px"}}>{count}</p>
          <MyButton onClick={increment} children={"increment"} />
          <br />
          <MyButton  onClick={decrement} children={"decrement"}/>
          <br />
          <MyButton onClick={reset} children={"reset"}/>
        </div>
    </div>
  );
}

function MyButton({ children , onClick }:{onClick:()=>void, children : ReactNode}){
  return (
    <button onClick={onClick}>
     {children}
    </button>
  );
}

