
export default function Card({ name ,cardtitle, age }:{age:number, cardtitle:string, name:string}){
  return (
    <div className='card' style={{border:"2px solid black", display:"flex", flexDirection:"column", width:"40%", borderRadius:"15px", boxShadow:"2px 2px 2px 2px black"}}>
      <h1>{cardtitle}</h1>
      <h2>Name:{name}</h2>
      <h2>Age:{age}</h2>
    </div>
  );
}




