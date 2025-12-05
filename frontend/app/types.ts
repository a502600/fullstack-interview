export type TodoItem = {
    id: number;
    name: string;
    order: number;
    completed: boolean;
}

export type CreateTodoResponse = {
    successful: boolean;
    item: TodoItem;
    items: TodoItem[];
    error: string;
}

export type ToggelTodoResponse = {
    successful: boolean;
    item: TodoItem;
    items: TodoItem[];
    error: string;
}

export type DeleteTodoResponse = {
    successful: boolean;
    items: TodoItem[];
    error: string;
}