SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

USE `master`;

INSERT INTO `agents` (`id`, `username`, `email`, `firstname`, `lastname`, `password_hash`) VALUES
(1,	'Kacper Dziedzic',	'kacper.dziedzic@wp.pl',	'Kacper',	'Dziedzic',	'$2b$12$gKCWHWpi/bl92qF8cFM90usREiymp3yxLMV1VvSw4X6jRARdEjVVG'),
(5,	'Kacper Dziedzic',	'kacper.dziedzic2@wp.pl',	'Kacper',	'Dziedzic',	'$2b$12$CfRT7/gogaIu8aZLR0H6JOGRQhrukuekv9BsXobouvvlhlYuKYcWC');

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
(62,	'Outlook is not working',	'Hi, I\'ve tried to login this morning but',	2,	1,	1,	1,	1,	'2022-07-05 11:42:00',	NULL),
(63,	'Outlook is not working',	'Hi, I\'ve tried to login this morning but',	2,	1,	1,	1,	1,	'2022-07-05 11:42:00',	NULL),
(64,	'Outlook is not working',	'Hi, I\'ve tried to login this morning but',	2,	1,	1,	1,	1,	'2022-07-05 11:42:01',	NULL),
(70,	'test4',	'Hi, I\'ve tried to login this morning but',	2,	1,	1,	1,	1,	'2022-07-05 12:43:17',	NULL);

INSERT INTO `tickettypes` (`id`, `ticket_type_name`) VALUES
(3,	'Change Request'),
(1,	'Incident'),
(2,	'Service Request');