-- Create Table
CREATE TABLE Students (
    ID INT,
    Name VARCHAR(50),
    Marks INT
);

-- Insert Data
INSERT INTO Students VALUES (1, 'Susmitha', 90);
INSERT INTO Students VALUES (2, 'Ravi', 85);
INSERT INTO Students VALUES (3, 'Priya', 95);

-- View All Records
SELECT * FROM Students;

-- View Students with Marks > 80
SELECT * FROM Students
WHERE Marks > 80;

-- Update Marks
UPDATE Students
SET Marks = 98
WHERE ID = 1;

-- Delete Record
DELETE FROM Students
WHERE ID = 2;
