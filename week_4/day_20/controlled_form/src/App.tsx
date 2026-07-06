import { useEffect, useState } from "react";
import ItemForm from "./components/itemform";
import ItemList from "./components/itemlist";

function App() {
  const [items, setItems] = useState<string[]>(() => {
    const defaults = ["Learn React", "Learn Tailwind"];

    try {
      const raw = localStorage.getItem("todo-items");
      if (raw) {
        const parsed = JSON.parse(raw) as string[];
        if (Array.isArray(parsed) && parsed.length > 0) {
          return parsed;
        }
      }
    } catch (e) {
      console.error(e);
    }

    return defaults;
  });

  function addItem(newItem: string) {
    setItems((prevItems) => [...prevItems, newItem]);
  }

  function removeItem(index: number) {
    setItems((prevItems) => prevItems.filter((_, i) => i !== index));
  }

  useEffect(() => {
    try {
      localStorage.setItem("todo-items", JSON.stringify(items));
    } catch (e) {
      console.error(e);
    }
  }, [items]);

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg shadow-md w-96">

        <h1 className="text-3xl font-bold text-center mb-6">
          Todo List
        </h1>

        <ItemForm addItem={addItem} />

        <ItemList items={items} removeItem={removeItem} />

      </div>
    </div>
  );
}

export default App;