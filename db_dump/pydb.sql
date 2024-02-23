-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: docker.for.mac.localhost:33062
-- Generation Time: Feb 23, 2024 at 08:35 PM
-- Server version: 8.1.0
-- PHP Version: 8.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE DATABASE pydb;

USE pydb;

CREATE TABLE `city` (
  `idcity` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `idcountry` int DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`idcity`, `name`, `idcountry`, `create_time`, `update_time`) VALUES
(1, 'city1', NULL, '2024-01-31 14:22:45', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `command_product`
--

CREATE TABLE `command_product` (
  `idcommand_product` int NOT NULL,
  `iduser` int DEFAULT NULL,
  `idproduct` int DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `idcountry` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `idproduct` int NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `iduser` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `idcity` int DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`iduser`, `name`, `idcity`, `create_time`, `update_time`) VALUES
(1, 'user1', NULL, '2024-01-31 14:21:59', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`idcity`),
  ADD KEY `city_fk1` (`idcountry`);

--
-- Indexes for table `command_product`
--
ALTER TABLE `command_product`
  ADD PRIMARY KEY (`idcommand_product`),
  ADD KEY `cmd_fk1` (`idproduct`),
  ADD KEY `cmd_fk2` (`iduser`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`idcountry`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`idproduct`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`iduser`),
  ADD KEY `user_fk1` (`idcity`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `idcity` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `command_product`
--
ALTER TABLE `command_product`
  MODIFY `idcommand_product` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `idcountry` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `idproduct` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `iduser` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_fk1` FOREIGN KEY (`idcountry`) REFERENCES `country` (`idcountry`);

--
-- Constraints for table `command_product`
--
ALTER TABLE `command_product`
  ADD CONSTRAINT `cmd_fk1` FOREIGN KEY (`idproduct`) REFERENCES `product` (`idproduct`),
  ADD CONSTRAINT `cmd_fk2` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_fk1` FOREIGN KEY (`idcity`) REFERENCES `city` (`idcity`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
