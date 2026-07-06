function ItemList({ items, removeItem }: { items: string[]; removeItem: (index: number) => void }) {
  return (
    <div>

      <h2 className="text-xl font-semibold mb-3">
        Items
      </h2>

      <ul>

        {items.map((item, index) => (
          <li key={index} className="bg-gray-200 p-2 rounded mb-2 flex justify-between items-center">
            <span>{item}</span>
            <button className="text-sm text-red-600 ml-4" onClick={() => removeItem(index)} aria-label={`Delete ${item}`}>
              Delete
            </button>
          </li>
        ))}

      </ul>

    </div>
  );
}

export default ItemList;