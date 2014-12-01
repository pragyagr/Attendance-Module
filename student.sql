-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2014 at 01:05 PM
-- Server version: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE IF NOT EXISTS `attendance` (
  `Roll_Number` int(8) NOT NULL,
  `Name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`Roll_Number`, `Name`) VALUES
(72003, 'Sagar'),
(72004, 'Rajan Maurya'),
(72010, 'Pragya Agrawal'),
(72011, 'Vivek Tambi'),
(72016, 'Harshit'),
(72018, 'Rushil Agarwal'),
(72020, 'Simran Sahoo'),
(72034, 'Chaitanya Choudhary'),
(72059, 'Shantanu Yadav'),
(72061, 'Pragya Jaiswal'),
(72071, 'Simmi'),
(72078, 'Saurabh Gupta'),
(72118, 'Arun Sharma'),
(72122, 'Vidit Tiwari'),
(72123, 'Shoaib Chaudhary'),
(72125, 'Kapil Kumar'),
(72139, 'Mayank Chauhan'),
(72151, 'Vaibhav Sharma'),
(72161, 'Prashant Manda'),
(72171, 'Sagar'),
(72173, 'Shreya Agarwal'),
(72174, 'Prashant Sinha'),
(72213, 'Pawan Pal'),
(72334, 'Ronit Kishore'),
(72350, 'Ishaan Arora'),
(72373, 'Gourav Kalbalia'),
(72407, 'Ashish'),
(72440, 'Akshay'),
(72452, 'Dheeraj Kumar'),
(72454, 'Vedant'),
(72471, 'Ankit Pathak'),
(72508, 'Archit Garg'),
(72511, 'Yatharth Aggarwal'),
(72530, 'Kaustabh Barman'),
(72540, 'Aishwary Singh'),
(72554, 'Ankit Chauhan'),
(72567, 'Devesh Khandelwal'),
(72672, 'Shashank Tekriwal');

-- --------------------------------------------------------

--
-- Table structure for table `student_att`
--

CREATE TABLE IF NOT EXISTS `student_att` (
  `Id` int(2) NOT NULL,
  `Roll_Number` int(8) NOT NULL,
  `Name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_att`
--

INSERT INTO `student_att` (`Id`, `Roll_Number`, `Name`) VALUES
(51, 72003, 'Sagar'),
(52, 72004, 'Rajan Maurya'),
(53, 72010, 'Pragya Agrawal'),
(54, 72011, 'Vivek Tambi'),
(55, 72016, 'Harshit'),
(56, 72018, 'Rushil Agarwal'),
(57, 72020, 'Simran Sahoo'),
(58, 72034, 'Chaitanya Choudhary'),
(59, 72059, 'Shantanu Yadav'),
(60, 72061, 'Pragya Jaiswal'),
(61, 72071, 'Simmi'),
(62, 72078, 'Saurabh Gupta'),
(63, 72118, 'Arun Sharma'),
(64, 72122, 'Vidit Tiwari'),
(65, 72123, 'Shoaib Chaudhary'),
(66, 72125, 'Kapil Kumar'),
(67, 72139, 'Mayank Chauhan'),
(68, 72151, 'Vaibhav Sharma'),
(69, 72161, 'Prashant Manda'),
(70, 72171, 'Sagar'),
(71, 72173, 'Shreya Agarwal'),
(72, 72174, 'Prashant Sinha'),
(73, 72213, 'Pawan Pal'),
(74, 72334, 'Ronit Kishore'),
(75, 72350, 'Ishan Arora'),
(76, 72373, 'Gourav Kalbalia'),
(77, 72407, 'Ashish Sharma'),
(78, 72440, 'Akshay'),
(79, 72452, 'Dheeraj Kumar'),
(80, 72454, 'Vedant Kohli'),
(81, 72471, 'Ankit Pathak'),
(82, 72508, 'Archit Garg'),
(83, 72511, 'Yatharth Aggarwal'),
(84, 72530, 'Kaustabh Barman'),
(85, 72540, 'Aishwarya Singh'),
(86, 72554, 'Ankit Chauhan'),
(87, 72567, 'Devesh Khandelwal'),
(88, 72672, 'Shashank Tekriwal');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
 ADD PRIMARY KEY (`Roll_Number`);

--
-- Indexes for table `student_att`
--
ALTER TABLE `student_att`
 ADD PRIMARY KEY (`Roll_Number`), ADD UNIQUE KEY `Roll Number` (`Roll_Number`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`Roll_Number`) REFERENCES `student_att` (`Roll_Number`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
