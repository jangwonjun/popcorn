CREATE TABLE `popcorn_user` (
  `name` VARCHAR(3),
  `phone_number` INT(12) UNIQUE,
  `bank` VARCHAR(7),
  `menu` VARCHAR(20),
  `cord` INT(20) UNIQUE
);
