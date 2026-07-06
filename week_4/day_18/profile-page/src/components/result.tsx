const mark = [
    {
        name:"Kiran",
        score:77,
    },
    {
        name:"Manoj",
        score:90,
    },
    {
        name:"Light",
        score:34,
    },
    {
        name:"Vima",
        score:29,
    },
    {
        name:"Pavan",
        score:80,
    }
]

export default function Result(){
    return (
        <>
        <ul>
            {mark.map((item, index) => (    
                <li key={index} style={{color : `${item.score < 35 ? "red" : "green"}`}}>
                    {item.name} ({item.score}) 
                    {item.score < 35 ? " is fail" : " is pass"}
                    
                </li>
            ))}
        </ul>
        </>
    )
}