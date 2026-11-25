-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mysql-draco459.alwaysdata.net
-- Generation Time: Nov 25, 2026 at 02:52 PM
-- Server version: 10.11.18-MariaDB
-- PHP Version: 8.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `draco459_cinema_dev`
--

--
-- Dumping data for table `capteur`
--
SET FOREIGN_KEY_CHECKS=0;

INSERT INTO `capteur` (`id`, `id_salle`, `num_capteur`, `nom`) VALUES
(8, 1, 108, ''),
(9, 1, 15, ''),
(10, 1, 111, ''),
(11, 1, 104, '');

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`id`, `nom_film`, `id_seance`, `resume`) VALUES
(2, 'Smile_2', 2, 'À l’aube d’une nouvelle tournée mondiale, la star de la pop Skye Riley se met à vivre des événements aussi terrifiants qu’inexplicables. Submergée par la pression de la célébrité et devant un quotidien qui bascule de plus en plus dans l’horreur, Skye est forcée de se confronter à son passé obscur pour tenter de reprendre le contrôle de sa vie avant qu’il ne soit trop tard.'),
(3, 'Lee_Miller', 3, 'Lee Miller est un film britannique réalisé par Ellen Kuras et sorti en 2023. Il s\'agit d\'un film biographique sur la photographe Elizabeth \"Lee\" Miller.'),
(4, 'Backrooms', 4, 'Après avoir découvert une mystérieuse porte dans le sous-sol de sa boutique, Clark sombre dans un labyrinthe infini d\'espaces liminaires appelés les Backrooms.  Sa psychologue, Mary, le suit pour l\'aider, mais ils se retrouvent tous deux piégés dans cette dimension qui agit comme un reflet déformé de leurs traumatismes et souvenirs');

--
-- Dumping data for table `mesure`
--

INSERT INTO `mesure` (`id`, `horodatage`, `id_capteur`, `temperature`, `humidite`, `CO2`) VALUES
(1, '0000-00-00 00:00:00', 8, 21.00, 48.00, 620.00),
(2, '0000-00-00 00:00:00', 8, 22.00, 51.00, 850.00),
(3, '0000-00-00 00:00:00', 8, 23.00, 54.00, 1200.00),
(4, '0000-00-00 00:00:00', 8, 24.00, 55.00, 1450.00),
(5, '0000-00-00 00:00:00', 8, 25.00, 57.00, 1600.00),
(6, '0000-00-00 00:00:00', 8, 14.00, 30.00, 700.00),
(7, '0000-00-00 00:00:00', 8, 16.00, 26.00, 800.00),
(8, '0000-00-00 00:00:00', 9, 14.00, 26.00, 1000.00),
(10, '0000-00-00 00:00:00', 9, 32.00, 56.00, 1675.00),
(11, '0000-00-00 00:00:00', 9, 23.00, 57.00, 1234.00),
(12, '0000-00-00 00:00:00', 9, 42.00, 0.00, 500.00),
(13, '0000-00-00 00:00:00', 11, -20.00, 100.00, 1800.00),
(14, '0000-00-00 00:00:00', 9, -15.00, 90.00, 1600.00),
(15, '0000-00-00 00:00:00', 8, 20.00, 60.00, 1400.00),
(16, '2026-09-09 15:30:21', 8, 18.24, 83.00, 913.83),
(17, '2026-09-09 15:31:33', 8, 16.24, 28.00, 2623.41),
(18, '2026-09-09 15:31:34', 8, 15.59, 57.00, 872.58),
(19, '2026-09-09 15:31:42', 8, 18.93, 55.00, 1761.71),
(20, '2026-09-09 15:32:06', 8, 18.61, 63.00, 2688.88),


--
-- Dumping data for table `salle`
--

INSERT INTO `salle` (`id`, `num_salle`, `nom_salle`, `id_film`) VALUES
(1, 8, 'Salle 8 Premium ICE', 1),
(2, 11, 'Salle 11 grand écran', 2),
(3, 15, 'Salle Prof', 3),
(4, 4, 'Salle 4', 4);

--
-- Dumping data for table `seance`
--

INSERT INTO `seance` (`id`, `date`, `langue`) VALUES
(1, '2026-10-21 01:27:00', 'vf'),
(2, '2026-10-22 02:00:00', 'vf'),
(3, '2026-10-21 00:00:00', 'vf'),
(4, '2026-10-21 00:00:00', 'vf'),
(5, '2026-10-21 00:00:00', 'vostf'),
(6, '2026-10-22 00:00:00', 'vf');
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
