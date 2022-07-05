SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

USE `master`;

INSERT INTO `agents` (`id`, `username`, `email`, `firstname`, `lastname`, `password_hash`) VALUES
(1,	'Admin',	'admin@gmail.com',	'Admin',	'Admin',	'$2b$12$gKCWHWpi/bl92qF8cFM90usREiymp3yxLMV1VvSw4X6jRARdEjVVG');

INSERT INTO `tickettypes` (`id`, `ticket_type_name`) VALUES
(3,	'Change Request'),
(1,	'Incident'),
(2,	'Service Request');

INSERT INTO `customers` (`id`, `username`, `email`, `firstname`, `lastname`) VALUES
(1,	'Pawel',	'pawel@consulting.eu',	'Pawel',	'Kwiatkowski'),
(2,	'Iwona',	'Iwona.Matczewka@gmail.com',	'Iwona',	'Matczewka'),
(3,	'KacperD',	'kacper.dziedzic@gmail.com',	'Kacper',	'Dziedzic');

INSERT INTO `levels` (`id`, `level_name`) VALUES
(4,	'Critical'),
(3,	'High'),
(1,	'Low'),
(2,	'Medium');

INSERT INTO `statuses` (`id`, `status_name`) VALUES
(4,	'Closed'),
(2,	'In Progress'),
(1,	'New'),
(3,	'OnHold');

INSERT INTO `tickets` (`id`, `summary`, `description`, `customer_id`, `status_id`, `level_id`, `agent_id`, `ticket_type_id`, `date_occured`, `closure_note`) VALUES
(1,	'Outlook is not working',	'Hi, I\'ve tried to login this morning but I can not access my outlook, please help',	1,	1,	1,	1,	1,	'2022-07-05 11:42:00',	NULL),
(2,	'Teams is not working',	'Hi, I\'ve tried to login this morning but to my Teams but they are not opening for me, help',	1,	1,	1,	1,	1,	'2022-07-05 11:56:00',	NULL);

