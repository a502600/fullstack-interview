-- Create table
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    "order" INTEGER NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
);

-- Read all todos
SELECT * FROM todos;

-- Read single todo by id
SELECT * FROM todos WHERE id = 1;

-- Create a todo (id is auto-generated)
INSERT INTO todos (name, "order", completed)
VALUES ('Buy groceries', 1, 0);

-- Update a todo (multiple fields)
UPDATE todos
SET name = 'Buy groceries and cook dinner', "order" = 2
WHERE id = 1;

-- Delete a todo
DELETE FROM todos WHERE id = 1;

-- Get all todos ordered
SELECT * FROM todos ORDER BY "order" ASC;
