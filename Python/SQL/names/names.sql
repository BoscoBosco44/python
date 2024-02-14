DELETE FROM names WHERE names.id > 0;
INSERT INTO names (id, name, created_at, updated_at) values (1, 'Peter Bosco', NOW(), NOW()), (2, 'Paul Paula', NOW(), NOW()), (3, 'Mr.EveilEggGuy', NOW(), NOW());
UPDATE names SET name = "Bosco Bosco" WHERE names.id = 1;
select * from names;
