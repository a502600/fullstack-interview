"use client";
import { useEffect, useState } from "react";
import { handleTodoItems } from "./hooks";
import "./styles.scss";
import Item from "./todo-item";

export default function Home() {

  const { items, fetchItems, addItem, deleteItem, toggleItem } = handleTodoItems();
  const [name, setName] = useState("");

  useEffect(() => {
    fetchItems();
  }, [])

  const addTodo = () => {
    if (name.trim() === "") return;
    addItem(name.trim());
    setName("");
  }

  return (
    <main>
      <h1>Todo Items</h1>
      <div className="create-container">
        <input placeholder="What's your next plan?" value={name} onChange={(e) => setName(e.target.value)}/>
        <button onClick={() => addTodo()}>Add Todo</button>
      </div>
      <div className="item-container">
        {items.map(item => (
          <Item 
            key={item.id} 
            item={item} 
            deleteItem={deleteItem} 
            toggleItem={toggleItem}
          />
        ))}
      </div>
    </main>
  );
}
