CREATE DATABASE function_store;
USE function_store;

-- Table to store function metadata
CREATE TABLE functions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    route VARCHAR(255) NOT NULL UNIQUE,
    language ENUM('python', 'javascript') NOT NULL,
    timeout INT NOT NULL CHECK (timeout > 0),
    description TEXT DEFAULT NULL,
    status ENUM('active', 'inactive') DEFAULT 'active',
    last_executed TIMESTAMP NULL DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store execution logs (optional, useful for monitoring)
CREATE TABLE function_executions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    function_id INT NOT NULL,
    execution_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('success', 'failure') NOT NULL,
    error_message TEXT DEFAULT NULL,
    FOREIGN KEY (function_id) REFERENCES functions(id) ON DELETE CASCADE
);
