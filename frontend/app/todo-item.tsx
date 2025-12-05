import { TodoItem } from "./types";

type TodoItemProps = {
    item: TodoItem;
    deleteItem: (id: number) => Promise<void>;
    toggleItem: (id: number) => Promise<void>;
}

export default function Item({ item, deleteItem, toggleItem }: TodoItemProps) {
    const { id, name, completed } = item;
    return (
        <div key={item.id} className={`item ${completed ? "item-completed" : ""}`}>
            <span className="name">{name}</span>
            <div className="flex gap-2">
                <span className="icon material-symbols-outlined cursor-pointer" onClick={() => toggleItem(id)}>
                    {completed ? "check_box" : "check_box_outline_blank"}
                </span>
                <span className="material-symbols-outlined cursor-pointer text-[#ff3a5b]" onClick={() => deleteItem(id)}>
                     delete
                </span>
            </div>
        </div>
    )
}