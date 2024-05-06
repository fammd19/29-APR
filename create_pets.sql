--Create pet owners table
CREATE TABLE IF NOT EXISTS pet_owners (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
gender TEXT,
age INTEGER
);

--Create pets table
CREATE TABLE IF NOT EXISTS pets (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
type TEXT NOT NULL,
pet_owner_id INTEGER NOT NULL,
FOREIGN KEY (pet_owner_id) REFERENCES pet_owners(id)
);

--Add data to pet_owners
insert into pet_owners (name, gender, age) values ('Normie Saltman', 'Male', 80);
insert into pet_owners (name, gender, age) values ('Cooper Petrillo', 'Male', 21);
insert into pet_owners (name, gender, age) values ('Delphine Leebeter', 'Genderfluid', 55);
insert into pet_owners (name, gender, age) values ('Sabra Vashchenko', 'Agender', 21);
insert into pet_owners (name, gender, age) values ('Lorene Walworche', 'Female', 49);

--Add data to pets
insert into pets (name, type, pet_owner_id) values ('Molly', 'dog', 2);
insert into pets (name, type, pet_owner_id) values ('Bailey', 'dog', 1);
insert into pets (name, type, pet_owner_id) values ('Sadie', 'dog', 3);
insert into pets (name, type, pet_owner_id) values ('Max', 'dog', 5);
insert into pets (name, type, pet_owner_id) values ('Daisy', 'fish', 5);
insert into pets (name, type, pet_owner_id) values ('Rocky', 'fish', 3);
insert into pets (name, type, pet_owner_id) values ('Lucy', 'fish', 4);
insert into pets (name, type, pet_owner_id) values ('Bella', 'fish', 3);
insert into pets (name, type, pet_owner_id) values ('Buddy', 'fish', 1);
insert into pets (name, type, pet_owner_id) values ('Sadie', 'fish', 5);
