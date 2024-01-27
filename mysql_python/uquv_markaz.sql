-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               10.3.22-MariaDB - mariadb.org binary distribution
-- Операционная система:         Win64
-- HeidiSQL Версия:              11.0.0.5958
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Дамп структуры базы данных uquv_markaz
DROP DATABASE IF EXISTS `uquv_markaz`;
CREATE DATABASE IF NOT EXISTS `uquv_markaz` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `uquv_markaz`;

-- Дамп структуры для таблица uquv_markaz.kurslar
DROP TABLE IF EXISTS `kurslar`;
CREATE TABLE IF NOT EXISTS `kurslar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kurs_nomi` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `narxi` decimal(10,2) DEFAULT NULL,
  `davomiyligi` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица uquv_markaz.tulovlar
DROP TABLE IF EXISTS `tulovlar`;
CREATE TABLE IF NOT EXISTS `tulovlar` (
  `uquvchi_id` int(11) DEFAULT NULL,
  `tulov` decimal(10,2) DEFAULT NULL,
  `kurs_id` int(11) DEFAULT NULL,
  `vaqti` datetime DEFAULT NULL,
  KEY `FK_tulovlar_kurslar` (`kurs_id`),
  KEY `FK_tulovlar_uquvchilar` (`uquvchi_id`),
  CONSTRAINT `FK_tulovlar_kurslar` FOREIGN KEY (`kurs_id`) REFERENCES `kurslar` (`id`),
  CONSTRAINT `FK_tulovlar_uquvchilar` FOREIGN KEY (`uquvchi_id`) REFERENCES `uquvchilar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица uquv_markaz.uqituvchilar
DROP TABLE IF EXISTS `uqituvchilar`;
CREATE TABLE IF NOT EXISTS `uqituvchilar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ism` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `familiya` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `yunalishi` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tel_raqami` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица uquv_markaz.uqituvchi_kurslari
DROP TABLE IF EXISTS `uqituvchi_kurslari`;
CREATE TABLE IF NOT EXISTS `uqituvchi_kurslari` (
  `uqituvchi_id` int(11) DEFAULT NULL,
  `kurs_id` int(11) DEFAULT NULL,
  `vaqti` time DEFAULT NULL,
  KEY `FK_uqituvchi_kurslari_kurslar` (`kurs_id`),
  KEY `FK_uqituvchi_kurslari_uqituvchilar` (`uqituvchi_id`),
  CONSTRAINT `FK_uqituvchi_kurslari_kurslar` FOREIGN KEY (`kurs_id`) REFERENCES `kurslar` (`id`),
  CONSTRAINT `FK_uqituvchi_kurslari_uqituvchilar` FOREIGN KEY (`uqituvchi_id`) REFERENCES `uqituvchilar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица uquv_markaz.uquvchilar
DROP TABLE IF EXISTS `uquvchilar`;
CREATE TABLE IF NOT EXISTS `uquvchilar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ism` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `familiya` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tugulgan_sana` date DEFAULT NULL,
  `tel_raqam` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица uquv_markaz.uquvchi_kurslari
DROP TABLE IF EXISTS `uquvchi_kurslari`;
CREATE TABLE IF NOT EXISTS `uquvchi_kurslari` (
  `uquvchi_id` int(11) DEFAULT NULL,
  `kurs_id` int(11) DEFAULT NULL,
  `uqituvchi_id` int(11) DEFAULT NULL,
  KEY `FK_uquvchi_kurslari_kurslar` (`kurs_id`),
  KEY `FK_uquvchi_kurslari_uquvchilar` (`uquvchi_id`),
  KEY `FK_uquvchi_kurslari_uqituvchilar` (`uqituvchi_id`),
  CONSTRAINT `FK_uquvchi_kurslari_kurslar` FOREIGN KEY (`kurs_id`) REFERENCES `kurslar` (`id`),
  CONSTRAINT `FK_uquvchi_kurslari_uqituvchilar` FOREIGN KEY (`uqituvchi_id`) REFERENCES `uqituvchilar` (`id`),
  CONSTRAINT `FK_uquvchi_kurslari_uquvchilar` FOREIGN KEY (`uquvchi_id`) REFERENCES `uquvchilar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Экспортируемые данные не выделены.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
