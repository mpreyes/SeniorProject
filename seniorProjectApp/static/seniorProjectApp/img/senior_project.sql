-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2019 at 04:51 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `senior_project`
--

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user', 1, 'add_customuser'),
(2, 'Can change user', 1, 'change_customuser'),
(3, 'Can delete user', 1, 'delete_customuser'),
(4, 'Can view user', 1, 'view_customuser'),
(5, 'Can add courses', 2, 'add_courses'),
(6, 'Can change courses', 2, 'change_courses'),
(7, 'Can delete courses', 2, 'delete_courses'),
(8, 'Can view courses', 2, 'view_courses'),
(9, 'Can add degree', 3, 'add_degree'),
(10, 'Can change degree', 3, 'change_degree'),
(11, 'Can delete degree', 3, 'delete_degree'),
(12, 'Can view degree', 3, 'view_degree'),
(13, 'Can add links', 4, 'add_links'),
(14, 'Can change links', 4, 'change_links'),
(15, 'Can delete links', 4, 'delete_links'),
(16, 'Can view links', 4, 'view_links'),
(17, 'Can add progress', 5, 'add_progress'),
(18, 'Can change progress', 5, 'change_progress'),
(19, 'Can delete progress', 5, 'delete_progress'),
(20, 'Can view progress', 5, 'view_progress'),
(21, 'Can add topics', 6, 'add_topics'),
(22, 'Can change topics', 6, 'change_topics'),
(23, 'Can delete topics', 6, 'delete_topics'),
(24, 'Can view topics', 6, 'view_topics'),
(25, 'Can add log entry', 7, 'add_logentry'),
(26, 'Can change log entry', 7, 'change_logentry'),
(27, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can view log entry', 7, 'view_logentry'),
(29, 'Can add permission', 8, 'add_permission'),
(30, 'Can change permission', 8, 'change_permission'),
(31, 'Can delete permission', 8, 'delete_permission'),
(32, 'Can view permission', 8, 'view_permission'),
(33, 'Can add group', 9, 'add_group'),
(34, 'Can change group', 9, 'change_group'),
(35, 'Can delete group', 9, 'delete_group'),
(36, 'Can view group', 9, 'view_group'),
(37, 'Can add site', 10, 'add_site'),
(38, 'Can change site', 10, 'change_site'),
(39, 'Can delete site', 10, 'delete_site'),
(40, 'Can view site', 10, 'view_site'),
(41, 'Can add content type', 11, 'add_contenttype'),
(42, 'Can change content type', 11, 'change_contenttype'),
(43, 'Can delete content type', 11, 'delete_contenttype'),
(44, 'Can view content type', 11, 'view_contenttype'),
(45, 'Can add session', 12, 'add_session'),
(46, 'Can change session', 12, 'change_session'),
(47, 'Can delete session', 12, 'delete_session'),
(48, 'Can view session', 12, 'view_session');

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(9, 'auth', 'group'),
(8, 'auth', 'permission'),
(11, 'contenttypes', 'contenttype'),
(2, 'seniorProjectApp', 'courses'),
(1, 'seniorProjectApp', 'customuser'),
(3, 'seniorProjectApp', 'degree'),
(4, 'seniorProjectApp', 'links'),
(5, 'seniorProjectApp', 'progress'),
(6, 'seniorProjectApp', 'topics'),
(12, 'sessions', 'session'),
(10, 'sites', 'site');

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-04-22 20:35:27.583976'),
(2, 'contenttypes', '0002_remove_content_type_name', '2019-04-22 20:35:28.836449'),
(3, 'auth', '0001_initial', '2019-04-22 20:35:33.948763'),
(4, 'auth', '0002_alter_permission_name_max_length', '2019-04-22 20:35:35.201121'),
(5, 'auth', '0003_alter_user_email_max_length', '2019-04-22 20:35:35.265089'),
(6, 'auth', '0004_alter_user_username_opts', '2019-04-22 20:35:35.332051'),
(7, 'auth', '0005_alter_user_last_login_null', '2019-04-22 20:35:35.387020'),
(8, 'auth', '0006_require_contenttypes_0002', '2019-04-22 20:35:35.432993'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2019-04-22 20:35:35.486963'),
(10, 'auth', '0008_alter_user_username_max_length', '2019-04-22 20:35:35.548927'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2019-04-22 20:35:35.602896'),
(12, 'seniorProjectApp', '0001_initial', '2019-04-22 20:35:51.936158'),
(13, 'admin', '0001_initial', '2019-04-22 20:35:54.915697'),
(14, 'admin', '0002_logentry_remove_auto_add', '2019-04-22 20:35:54.996024'),
(15, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-22 20:35:55.188113'),
(16, 'seniorProjectApp', '0002_auto_20190422_1531', '2019-04-22 20:35:57.496121'),
(17, 'sessions', '0001_initial', '2019-04-22 20:35:58.633530'),
(18, 'sites', '0001_initial', '2019-04-22 20:35:59.288761'),
(19, 'sites', '0002_alter_domain_unique', '2019-04-22 20:35:59.564979');

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1ebjktl348afgw2zr4fjcl31gfh4w21r', 'NjM0OTY1ZDM5NWU1NzgyOTg2YmIyN2U0YzdhMDIzNTViNGM4ZmFiMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDgwNjIzMWRiNjEzYmQ1OTBhNGYwOTY5NzQwNWY2NjVlMzhkNThiMSJ9', '2019-05-06 21:02:46.365225');

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

--
-- Dumping data for table `seniorprojectapp_courses`
--

INSERT INTO `seniorprojectapp_courses` (`courseID`, `courseName`, `courseDescription`, `level`, `degreeID_id`) VALUES
(1, 'Intro to Computer Science', 'Intro to programming focuses on coding basics and learning Python, which is becoming one of the most popular programming languages.', 'Freshman', 1),
(2, 'Intro to Computer Programming', 'Intro to programming focuses on coding basics and learning Python, which is becoming one of the most popular programming languages.', 'Freshman', 1),
(3, 'Object-Oriented System and Design', 'Object-Oriented Programming focuses on the basics of the Java programming language and then moves into classes and objects, finishing with inheritance and abstract classes. ', 'Freshman', 1),
(4, 'Data Structures and Algorithms', 'Implementation and application of fundamental data structures and computing algorithms used in computer science, including searching and sorting; elementary abstract data types including linked lists, stacks, queues, trees and graphs. Particular emphasis is given to the use of object-oriented design and data abstraction in the creation and application of these data structures.', 'Sophomore', 1),
(5, 'Database Management Systems', 'Introduction to database concepts and the relational database model. Topics include SQL, normalization, design methodology, DBMS functions, database administration, and other database management approaches such as client/server databases, object oriented databases, and data warehouses. Strong emphasis on database system design and application development.', 'Sophomore', 1),
(6, 'Computer Organization', 'Introduction to computer organization with emphasis on the lower level abstraction of a computer system including digital logic, instruction set and assembly language programming.', 'Sophomore', 1),
(7, 'Computer Graphics', 'Design and implementation of object-oriented graphical user interfaces (GUI) and two-dimensional computer graphics systems. Implementation methodologies including callbacks, handlers, event listeners, design patterns, layout managers, and architectural models.', 'Junior', 1),
(8, 'Design and Analysis of Algorithms', 'Study of the techniques for designing algorithms and for analyzing the time and space efficiency of algorithms. The algorithm design techniques include divide-and-conquer, greedy algorithms, dynamic programming, randomized algorithms and parallel algorithms.', 'Junior', 1),
(9, 'Comparative Programming Language', 'Discussion of the important issues in the specification, design and implementation of programming languages with emphasis on imperative programming. Emphasis is on evaluating alternative ways of providing various symbols, abstractions, definitions, theorems, proofs, programming language features and trade-offs involved.', 'Junior', 1),
(10, 'Compiler Construction', 'Study of the theory and design techniques used in compiler construction, including lexical analysis, parsing, grammars, semantic analysis, code generation and optimization. Each student will implement a subset of a compiler.', 'Senior', 1),
(11, 'Fundamentals of Automata and Formal Language Theory', 'Introduction to fundamental concepts of automata theory and formal languages including finite automata, regular expressions, formal language theory and pushdown automata.', 'Senior', 1),
(12, 'Artificial Intelligence', 'An exploration of concepts, approaches and techniques of artificial intelligence: specification, design, and implementation of selected applications of intelligent software agents and multi-agent systems.', 'Senior', 1);

--
-- Dumping data for table `seniorprojectapp_customuser`
--

INSERT INTO `seniorprojectapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `degreeID`) VALUES
(1, 'pbkdf2_sha256$120000$6GYeAdVqsfl0$JaGekuGD5gRjy3Nsm73fXfzu71fG/S6XOEwoekbCu4g=', '2019-04-22 21:02:46.213623', 0, 'tom', '', '', '', 0, 1, '2019-04-22 20:47:20.786896', '1');

--
-- Dumping data for table `seniorprojectapp_degree`
--

INSERT INTO `seniorprojectapp_degree` (`degreeID`, `degreeName`) VALUES
(1, 'Computer Science'),
(2, 'Software Engineering'),
(3, 'Web Development');

--
-- Dumping data for table `seniorprojectapp_links`
--

INSERT INTO `seniorprojectapp_links` (`linksID`, `linkName`, `linkUrl`, `topicID_id`) VALUES
(1, 'codingBat', 'https://codingbat.com/python', 1),
(2, 'For Loops', 'https://wiki.python.org/moin/ForLoop', 4),
(3, 'Intro to Python', 'https://www.python.org/about/gettingstarted/', 1);

--
-- Dumping data for table `seniorprojectapp_topics`
--

INSERT INTO `seniorprojectapp_topics` (`topicID`, `topicName`, `courseID_id`) VALUES
(1, 'Processing Programming', 1),
(2, 'History of Computing', 1),
(3, 'Programming Languages', 1),
(4, 'Programming Basics', 2),
(5, 'Python Basics', 2),
(6, 'Programming Practice', 2),
(7, 'OOP Basics', 3),
(8, 'OOP Intermediate', 3),
(9, 'Revised OOP', 3),
(10, 'Data Structures', 4),
(11, 'Algorithms (1)', 4),
(12, 'Algorithms (2)', 4),
(13, 'SQL', 5),
(14, 'Relational Algebra', 5),
(15, 'Entity Relational Model', 5),
(16, 'Assembly Language', 6),
(17, 'Circuitry', 6),
(18, 'Binary Arithmetic', 6),
(19, '2D Graphics Basics', 7),
(20, 'Fill Algorithms', 7),
(21, 'Viewing and Clipping', 7),
(22, 'Graph Theory', 8),
(23, 'Sorting Methods', 8),
(24, 'Complexity Theory', 8),
(25, 'Scheme Programming', 9),
(26, 'Prolog Programming', 9),
(27, 'Scoping', 9),
(28, 'Compiler Architecture', 10),
(29, 'Lexical Analysis', 10),
(30, 'Syntax Analysis', 10),
(31, 'Regular Grammar', 11),
(32, 'Deterministic Finite Automaton', 11),
(33, 'Non deterministic finite atomaton', 11),
(34, 'Agents and Environment', 12),
(35, 'Neural Networks', 12),
(36, 'Search Algorithms', 12);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
