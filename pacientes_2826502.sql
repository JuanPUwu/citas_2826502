-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para citas_2826502
DROP DATABASE IF EXISTS `citas_2826502`;
CREATE DATABASE IF NOT EXISTS `citas_2826502` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `citas_2826502`;

-- Volcando estructura para tabla citas_2826502.citas
DROP TABLE IF EXISTS `citas`;
CREATE TABLE IF NOT EXISTS `citas` (
  `id_cita` int(20) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `hora` time(6) NOT NULL DEFAULT current_timestamp(),
  `consultorio` varchar(50) NOT NULL DEFAULT '0',
  `doctor_id` int(20) NOT NULL DEFAULT 0,
  `paciente_id` int(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_cita`),
  KEY `FK__doctores` (`doctor_id`),
  KEY `FK__pacientes` (`paciente_id`),
  CONSTRAINT `FK__doctores` FOREIGN KEY (`doctor_id`) REFERENCES `doctores` (`id_doctores`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__pacientes` FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id_pacientes`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla citas_2826502.citas: ~2 rows (aproximadamente)
DELETE FROM `citas`;
INSERT INTO `citas` (`id_cita`, `fecha`, `hora`, `consultorio`, `doctor_id`, `paciente_id`) VALUES
	(2, '2024-02-14', '17:02:55.000000', '1', 3, 3),
	(3, '2025-02-14', '10:03:23.000000', '3', 1, 2);

-- Volcando estructura para tabla citas_2826502.doctores
DROP TABLE IF EXISTS `doctores`;
CREATE TABLE IF NOT EXISTS `doctores` (
  `id_doctores` int(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `documento` int(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_doctores`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla citas_2826502.doctores: ~3 rows (aproximadamente)
DELETE FROM `doctores`;
INSERT INTO `doctores` (`id_doctores`, `nombre`, `apellido`, `documento`) VALUES
	(1, 'Carlos', 'Sanchez', 178967823),
	(2, 'Carla', 'Diaz', 198283811),
	(3, 'Laura', 'Mesa', 139820915);

-- Volcando estructura para tabla citas_2826502.pacientes
DROP TABLE IF EXISTS `pacientes`;
CREATE TABLE IF NOT EXISTS `pacientes` (
  `id_pacientes` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL DEFAULT '',
  `apellido` varchar(50) NOT NULL DEFAULT '',
  `edad` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id_pacientes`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla citas_2826502.pacientes: ~3 rows (aproximadamente)
DELETE FROM `pacientes`;
INSERT INTO `pacientes` (`id_pacientes`, `nombre`, `apellido`, `edad`) VALUES
	(1, 'Ricardo', 'Trujillo', '34'),
	(2, 'Pedro', 'Paez', '31'),
	(3, 'Olga', 'Hernandez', '29');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
information_schemamysql