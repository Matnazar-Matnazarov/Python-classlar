-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2024 at 11:33 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uquv_markaz`
--

-- --------------------------------------------------------

--
-- Table structure for table `guruhlar`
--

CREATE TABLE `guruhlar` (
  `id` int(11) NOT NULL,
  `guruh` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `uqtuvchilar`
--

CREATE TABLE `uqtuvchilar` (
  `id` int(11) NOT NULL,
  `ism` varchar(50) NOT NULL,
  `familiya` varchar(50) NOT NULL,
  `tel_raqami` varchar(30) NOT NULL,
  `qaysi_fan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `uquvchilar`
--

CREATE TABLE `uquvchilar` (
  `id` int(11) NOT NULL,
  `ismi` varchar(50) NOT NULL,
  `familiya` varchar(50) NOT NULL,
  `kurs` varchar(20) NOT NULL,
  `telfon_raqam` varchar(20) NOT NULL,
  `tugulgan_sana` date NOT NULL,
  `guruh_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
