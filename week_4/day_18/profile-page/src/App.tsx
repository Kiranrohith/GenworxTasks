import MyComponents from "./components/counter";
import Card from "./components/card";
import Result from "./components/result";
function App() {

  return (
    <div>
      <MyComponents />
      <div style={{display:"flex", gap:"10px", marginTop:"20px" }}>
      <Card name="kiran" cardtitle="Personal info" age={22} />
      <br />
      <Card name="Manoj" cardtitle="Personal info" age={23} />
      <br />
      </div>
      <br />
      <Result />
    </div>
  );
}

export default App;