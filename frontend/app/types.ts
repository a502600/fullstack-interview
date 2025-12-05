export type TodoItem = {
    id: number;
    name: string;
    order: number;
    completed: boolean;
}

export type CreateTodoResponse = {
    successful: boolean;
    createdTodo: TodoItem;
    todos: TodoItem[];
    error: string;
}

export type ToggelTodoResponse = {
    successful: boolean;
    updatedTodo: TodoItem;
    todos: TodoItem[];
    error: string;
}

export type DeleteTodoResponse = {
    successful: boolean;
    deletedTodo: TodoItem;
    todos: TodoItem[];
    error: string;
}