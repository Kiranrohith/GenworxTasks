import { useState, type ChangeEvent } from "react";

type ItemFormProps = {
  addItem: (text: string) => void;
};

function ItemForm({ addItem }: ItemFormProps) {
  const [text, setText] = useState<string>("");

  function handleSubmit() {
    if (text.trim() === "") return;
    addItem(text);
    setText("");
  }

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        handleSubmit();
      }}
      className="mb-5"
    >

      <input
        type="text"
        placeholder="Enter item"
        value={text}
        onChange={(e: ChangeEvent<HTMLInputElement>) => setText(e.target.value)}
        className="border p-2 rounded w-full mb-3"
      />

      <button
        className="bg-blue-500 text-white px-4 py-2 rounded w-full"
      >
        Add Item
      </button>

    </form>
  );
}

export default ItemForm;