-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: bgg
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `artist_id` int NOT NULL AUTO_INCREMENT,
  `artist_name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `designers`
--

DROP TABLE IF EXISTS `designers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `designers` (
  `designer_id` int NOT NULL AUTO_INCREMENT,
  `designer_name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`designer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designers`
--

LOCK TABLES `designers` WRITE;
/*!40000 ALTER TABLE `designers` DISABLE KEYS */;
/*!40000 ALTER TABLE `designers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `id` int NOT NULL AUTO_INCREMENT,
  `site_id` int DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_artists`
--

DROP TABLE IF EXISTS `game_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_artists` (
  `game_id` int NOT NULL,
  `artist_id` int NOT NULL,
  PRIMARY KEY (`game_id`,`artist_id`),
  KEY `artist_id` (`artist_id`),
  CONSTRAINT `game_artists_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `game_artists_ibfk_2` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`artist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_artists`
--

LOCK TABLES `game_artists` WRITE;
/*!40000 ALTER TABLE `game_artists` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_category`
--

DROP TABLE IF EXISTS `game_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_category` (
  `game_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`game_id`,`category_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `game_category_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `game_category_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_category`
--

LOCK TABLES `game_category` WRITE;
/*!40000 ALTER TABLE `game_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_designers`
--

DROP TABLE IF EXISTS `game_designers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_designers` (
  `game_id` int NOT NULL,
  `designer_id` int NOT NULL,
  PRIMARY KEY (`game_id`,`designer_id`),
  KEY `designer_id` (`designer_id`),
  CONSTRAINT `game_designers_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `game_designers_ibfk_2` FOREIGN KEY (`designer_id`) REFERENCES `designers` (`designer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_designers`
--

LOCK TABLES `game_designers` WRITE;
/*!40000 ALTER TABLE `game_designers` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_designers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_mechanics`
--

DROP TABLE IF EXISTS `game_mechanics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_mechanics` (
  `game_id` int NOT NULL,
  `mechanics_id` int NOT NULL,
  PRIMARY KEY (`game_id`,`mechanics_id`),
  KEY `mechanics_id` (`mechanics_id`),
  CONSTRAINT `game_mechanics_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `game_mechanics_ibfk_2` FOREIGN KEY (`mechanics_id`) REFERENCES `mechanics` (`mechanic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_mechanics`
--

LOCK TABLES `game_mechanics` WRITE;
/*!40000 ALTER TABLE `game_mechanics` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_mechanics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_reimplements`
--

DROP TABLE IF EXISTS `game_reimplements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_reimplements` (
  `game_id` int NOT NULL,
  `reimplement_game_id` int NOT NULL,
  PRIMARY KEY (`game_id`,`reimplement_game_id`),
  KEY `reimplement_game_id` (`reimplement_game_id`),
  CONSTRAINT `game_reimplements_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `game_reimplements_ibfk_2` FOREIGN KEY (`reimplement_game_id`) REFERENCES `game` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_reimplements`
--

LOCK TABLES `game_reimplements` WRITE;
/*!40000 ALTER TABLE `game_reimplements` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_reimplements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_stats`
--

DROP TABLE IF EXISTS `game_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_stats` (
  `game_id` int NOT NULL,
  `ave_rating` float DEFAULT NULL,
  `overall_rank` int DEFAULT NULL,
  `type_rank` int DEFAULT NULL,
  `n_comments` int DEFAULT NULL,
  `n_page_views` int DEFAULT NULL,
  `played_all_times` int DEFAULT NULL,
  `played_last_month` int DEFAULT NULL,
  `n_own` int DEFAULT NULL,
  `n_wishlist` int DEFAULT NULL,
  `n_ratings` int DEFAULT NULL,
  PRIMARY KEY (`game_id`),
  CONSTRAINT `game_stats_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_stats`
--

LOCK TABLES `game_stats` WRITE;
/*!40000 ALTER TABLE `game_stats` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `general_info`
--

DROP TABLE IF EXISTS `general_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `general_info` (
  `game_id` int NOT NULL,
  `type_id` int DEFAULT NULL,
  `min_num_players` int DEFAULT NULL,
  `max_num_players` int DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `year_published` int DEFAULT NULL,
  `min_time_duration` int DEFAULT NULL,
  `max_time_duration` int DEFAULT NULL,
  `age_limit` int DEFAULT NULL,
  PRIMARY KEY (`game_id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `general_info_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `general_info_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `types` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `general_info`
--

LOCK TABLES `general_info` WRITE;
/*!40000 ALTER TABLE `general_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `general_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mechanics`
--

DROP TABLE IF EXISTS `mechanics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mechanics` (
  `mechanic_id` int NOT NULL AUTO_INCREMENT,
  `machanic` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`mechanic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mechanics`
--

LOCK TABLES `mechanics` WRITE;
/*!40000 ALTER TABLE `mechanics` DISABLE KEYS */;
/*!40000 ALTER TABLE `mechanics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `types` (
  `type_id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `types`
--

LOCK TABLES `types` WRITE;
/*!40000 ALTER TABLE `types` DISABLE KEYS */;
/*!40000 ALTER TABLE `types` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-31 14:52:10
