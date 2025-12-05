import { useState } from "react"
import { CreateTodoResponse, DeleteTodoResponse, TodoItem, ToggelTodoResponse } from "./types"

const todos = [
    {
        id: 1,
        name: "Sample ToDo Item",
        order: 0,
        completed: false
    },
    {
        id: 2,
        name: "Another Sample ToDo Item",
        order: 1,
        completed: true
    },
    {
        id: 3,
        name: "Yet Another Sample ToDo Item",
        order: 2,
        completed: false
    }
]

export const handleTodoItems = () => {
    const [items, setItems] = useState<TodoItem[]>(todos)

    const backendUrl = process.env.BACKEND_URL || "http://localhost:8000"

    const fetchItems = async () => {
        try {
            const results = await fetch(`${backendUrl}/todo/read`)
            const data = await results.json()
            setItems(data)
        } catch (error) {
            console.error("Error fetching ToDo items:", error)
        }
    }

    const addItem = async (name: string) => {
        const newItem: Omit<TodoItem, "id"> = {
            name,
            order: items ? items.length : 0,
            completed: false
        }
        try {
            const results = await fetch(`${backendUrl}/todo/create`, {
                method: "POST",
                body: JSON.stringify(newItem),
            })
            const data: CreateTodoResponse = await results.json()
            setItems(data.items)
        } catch (error) {
            console.error("Error adding ToDo item:", error)
        }
    }

    const deleteItem = async (id: number) => {
        const item = items.find(i => i.id === id)
        if (!item) return
        try {
            const results = await fetch(`${backendUrl}/todo/delete/${id}`, {
                method: "DELETE",
            })
            const data: DeleteTodoResponse = await results.json()
            setItems(data.items)
        } catch (error) {
            console.error("Error adding ToDo item:", error)
        }
    }

    const toggleItem = async (id: number) => {
        const item = items.find(i => i.id === id)
        if (!item) return
        try {
            const results = await fetch(`${backendUrl}/todo/update/${id}`, {
                method: "PATCH",
                body: JSON.stringify({ completed: !item.completed }),
            })
            const data: ToggelTodoResponse = await results.json()
            setItems(data.items)
        } catch (error) {
            console.error("Error editing ToDo item:", error)
        }
    }

    return {
        items,
        fetchItems,
        addItem,
        deleteItem,
        toggleItem
    }
}