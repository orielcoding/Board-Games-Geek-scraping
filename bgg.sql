-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: target_db
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
  `artist_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (1,'Lina Cossette'),(2,'David Forest'),(3,'Damien Mammoliti'),(4,'Chris Quilliams'),(5,'Alexandr Elichev'),(6,'Josh T. McDowell'),(7,'Alvaro Nebot'),(8,'Steffen Bieker'),(9,'Loïc Billiau'),(10,'Dennis Lohausen'),(11,'Christof Tisch'),(12,'Scott Schomburg'),(13,'Isaac Fryxelius'),(14,'Francesca Baerald'),(15,'David Demaret'),(16,'John Howe'),(17,'Fabio Maiorana'),(18,'Matt Allsopp'),(19,'David Ardila'),(20,'Balaskas'),(21,'Tiziano Baracchi'),(22,'Clay Brooks'),(23,'Raul Ramos'),(24,'Nate Storm'),(25,'Jason Behnke'),(26,'Loïc Berger'),(27,'Kat G Birmelin'),(28,'Filip Murmak'),(29,'Radim Pech'),(30,'Jakub Politzer'),(31,'Milan Vavroň'),(32,'Viktor Csete'),(33,'Rodger B. MacGowan'),(34,'Chechu Nieto'),(35,'Guillaume Ries'),(36,'Mark Simonitch'),(37,'Cole Wehrle'),(38,'Fantasy Flight Games'),(39,'Iris de Haan'),(40,'Ynze Moedt'),(41,'Josh J. Carlson'),(42,'Anthony LeTourneau'),(43,'Atha Kanaani'),(44,'Cristi Balanescu'),(45,'Yoann Boissonnet'),(46,'Anders Finér'),(47,'Tony Foti'),(48,'Javier González Cava'),(49,'Klemens Franz'),(50,'Henning Ludvigsen'),(51,'Thierry Masson'),(52,'Mike McVey'),(53,'Adrian Smith'),(54,'Marco Armbruster'),(55,'Fiore GmbH'),(56,'Aline Kirrmann'),(57,'Dan Gerlach'),(58,'Monica Helland'),(59,'Samuel R. Shimota'),(60,'Allison Litchfield'),(61,'Orlando Ramirez'),(62,'Domonkos Bence'),(63,'Antonio Dessi'),(64,'Lars-Arne \"Maura\" Kalusky'),(65,'Prapach Lapamnuaysap'),(66,'Harald Lieske'),(67,'Ryan Laukat'),(68,'Ian O\'Toole'),(69,'Sensit Communication GmbH'),(70,'Wolfgang Warsch'),(71,'Arden Beckwith'),(72,'Christopher Burdett'),(73,'Rovina Cai'),(74,'Lucas Durham'),(75,'Danny Beck'),(76,'Tysen Henderson'),(77,'Mihajlo Dimitrievski'),(78,'Zeen Chin'),(79,'Lokman Lam'),(80,'Lorinda Tomko'),(81,'Bruno Balixa'),(82,'Ralph Beisner'),(83,'Del Borovic'),(84,'Adam S. Doyle'),(85,'Philippe Guérin'),(86,'Ossi Hiekkala'),(87,'Sampo Sikiö'),(88,'Martin Hoffmann'),(89,'Claus Stephan'),(90,'Gong Studios'),(91,'Rayph Beisner'),(92,'Clément Masson'),(93,'Nicolas Fructus'),(94,'Karl Kopinski'),(95,'Edgar Skomorowski'),(96,'Richard Cortes'),(97,'Paul Niemeyer'),(98,'Odysseas Stamoglou'),(99,'Tomasz Bentkowski'),(100,'Mateusz Bielski'),(101,'Vincent Dutrait'),(102,'Jerzy Ferdyn'),(103,'Eric Belisle'),(104,'Steven Belledin'),(105,'Zoltan Boros'),(106,'Noah Bradley'),(107,'Dimitri Chappuis'),(108,'Miguel Coimbra'),(109,'Etienne Hebinger'),(110,'Cyril Nouvel'),(111,'Bartek Jędrzejewski'),(112,'Chad Jensen'),(113,'Franz Vohwinkel'),(114,'Ludovic Roudy'),(115,'Piotr Foksowicz'),(116,'Piotr Gacek'),(117,'Patryk Jędraszek'),(118,'Ewa Labak'),(119,'Dan Hallagan'),(120,'Doris Matthäus'),(121,'Kevin Childress'),(122,'Brian Schomburg'),(123,'WiL Springer'),(124,'James Masino'),(125,'Michael Pedro'),(126,'Juliet Breese'),(127,'Jo Breese'),(128,'Gemma Tegelaers'),(129,'Cyril Demaegd'),(130,'Arnaud Demaegd'),(131,'Mike Doyle (I)'),(132,'Andreas Resch'),(133,'Fabien Fulchiron'),(134,'NILS'),(135,'Manuel Sanchez');
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
  `category` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Economic'),(2,'Industry / Manufacturing'),(3,'Post-Napoleonic'),(4,'Trains'),(5,'Transportation'),(6,'Environmental'),(7,'Medical'),(8,'Adventure'),(9,'Exploration'),(10,'Fantasy'),(11,'Fighting'),(12,'Miniatures'),(13,'Animals'),(14,'Civilization'),(15,'Negotiation'),(16,'Political'),(17,'Science Fiction'),(18,'Space Exploration'),(19,'Territory Building'),(20,'Novel-based'),(21,'Wargame'),(22,'Civil War'),(23,'Movies / TV / Radio theme'),(24,'Mythology'),(25,'Card Game'),(26,'Modern Warfare'),(27,'Educational'),(28,'Spies/Secret Agents'),(29,'Collectible Components'),(30,'Comic Book / Strip'),(31,'Dice'),(32,'Horror'),(33,'Farming'),(34,'Nautical'),(35,'American West'),(36,'Pirates'),(37,'Action / Dexterity'),(38,'Ancient'),(39,'City Building'),(40,'Medieval'),(41,'Video Game Theme'),(42,'Mature / Adult'),(43,'Bluffing'),(44,'Abstract Strategy'),(45,'Puzzle'),(46,'Renaissance'),(47,'Arabian'),(48,'Travel'),(49,'Prehistoric'),(50,'Deduction'),(51,'Party Game'),(52,'Word Game');
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
  `designer_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`designer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designers`
--

LOCK TABLES `designers` WRITE;
/*!40000 ALTER TABLE `designers` DISABLE KEYS */;
INSERT INTO `designers` VALUES (1,'Gavan Brown'),(2,'Matt Tolman'),(3,'Martin Wallace'),(4,'Rob Daviau'),(5,'Matt Leacock'),(6,'Isaac Childres'),(7,'Mathias Wigge'),(8,'Dane Beltrami'),(9,'Corey Konieczka'),(10,'Christian T. Petersen'),(11,'Jacob Fryxelius'),(12,'Roberto Di Meglio'),(13,'Marco Maggi'),(14,'Francesco Nepitello'),(15,'Paul Dennen'),(16,'R. Eric Reuss'),(17,'Jens Drögemüller'),(18,'Helge Ostertag'),(19,'Vlaada Chvátil'),(20,'Ananda Gupta'),(21,'Jason Matthews'),(22,'Cole Wehrle'),(23,'Michael Boggs'),(24,'Jeroen Doumen'),(25,'Joris Wiersinga'),(26,'Josh J. Carlson'),(27,'Adam Carlson'),(28,'Nikki Valens'),(29,'Uwe Rosenberg'),(30,'Eric M. Lang'),(31,'Thomas Sing'),(32,'Alexander Pfister'),(33,'(Uncredited)'),(34,'Simone Luciani'),(35,'Daniele Tascini'),(36,'Friedemann Friese'),(37,'Ryan Laukat'),(38,'Vital Lacerda'),(39,'Juma Al-JouJou'),(40,'Wolfgang Warsch'),(41,'Justin Kemppainen'),(42,'Jonathan Ying'),(43,'Chris Cantrell'),(44,'Rick Ernst'),(45,'Stone Librande'),(46,'Prashant Saraswat'),(47,'Nathan Tiras'),(48,'S J Macdonald'),(49,'Shem Phillips'),(50,'Adam Poots'),(51,'Richard Garfield'),(52,'Lukas Litzsinger'),(53,'Virginio Gigli'),(54,'Michael Kiesling'),(55,'Touko Tahkokallio'),(56,'Thomas Lehmann'),(57,'Jenny Iglesias'),(58,'Nick Little (I)'),(59,'Kevin Riley'),(60,'Bruno Cathala'),(61,'Joanna Kijanka'),(62,'Ignacy Trzewiczek'),(63,'Peter Lee'),(64,'Rodney Thompson'),(65,'Antoine Bauza'),(66,'Chad Jensen'),(67,'Dennis K. Chan'),(68,'Ludovic Roudy'),(69,'Bruno Sautter'),(70,'Krzysztof Piskorski'),(71,'Marcin Świerkot'),(72,'Dan Hallagan'),(73,'Wolfgang Kramer'),(74,'Richard Ulrich'),(75,'Matthew O\'Malley'),(76,'Ben Rosset'),(77,'Sebastian Bleasdale'),(78,'Richard Breese'),(79,'William Attia'),(80,'Thomas Dagenais-Lespérance'),(81,'Nathan I. Hajek'),(82,'Grace Holdinghaus');
/*!40000 ALTER TABLE `designers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `site_id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`site_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (93,'El Grande '),(521,'Crokinole '),(2651,'Power Grid '),(12333,'Twilight Struggle '),(18602,'Caylus '),(25613,'Through the Ages: A Story of Civilization '),(28143,'Race for the Galaxy '),(35677,'Le Havre '),(37111,'Battlestar Galactica: The Board Game '),(55690,'Kingdom Death: Monster '),(62219,'Dominant Species '),(68448,'7 Wonders '),(72125,'Eclipse '),(102794,'Caverna: The Cave Farmers '),(110327,'Lords of Waterdeep '),(115746,'War of the Ring: Second Edition '),(121921,'Robinson Crusoe: Adventures on the Cursed Island '),(122515,'Keyflower '),(124742,'Android: Netrunner '),(125153,'The Gallerist '),(126163,'Tzolk\'in: The Mayan Calendar '),(157354,'Five Tribes '),(159675,'Fields of Arle '),(161533,'Lisboa '),(161936,'Pandemic Legacy: Season 1 '),(162886,'Spirit Island '),(164153,'Star Wars: Imperial Assault '),(167791,'Terraforming Mars '),(170042,'Raiders of the North Sea '),(170216,'Blood Rage '),(171623,'The Voyages of Marco Polo '),(172386,'Mombasa '),(174430,'Gloomhaven '),(175914,'Food Chain Magnate '),(180263,'The 7th Continent '),(182028,'Through the Ages: A New Story of Civilization '),(182874,'Grand Austria Hotel '),(187645,'Star Wars: Rebellion '),(191189,'Aeon\'s End '),(192135,'Too Many Bones '),(200680,'Agricola (Revised Edition) '),(201808,'Clank!: A Deck-Building Adventure '),(205059,'Mansions of Madness: Second Edition '),(209010,'Mechs vs. Minions '),(216132,'Clans of Caledonia '),(220308,'Gaia Project '),(221107,'Pandemic Legacy: Season 2 '),(224517,'Brass: Birmingham '),(225694,'Decrypto '),(229853,'Teotihuacan: City of Gods '),(230802,'Azul '),(231733,'Obsession '),(233078,'Twilight Imperium: Fourth Edition '),(236457,'Architects of the West Kingdom '),(244521,'The Quacks of Quedlinburg '),(253344,'Cthulhu: Death May Die '),(255984,'Sleeping Gods '),(256960,'Pax Pamir: Second Edition '),(264220,'Tainted Grail: The Fall of Avalon '),(266810,'Paladins of the West Kingdom '),(269385,'The Lord of the Rings: Journeys in Middle-Earth '),(276025,'Maracaibo '),(279537,'The Search for Planet X '),(284083,'The Crew: The Quest for Planet Nine '),(284378,'Kanban EV '),(285774,'Marvel Champions: The Card Game '),(291457,'Gloomhaven: Jaws of the Lion '),(314040,'Pandemic Legacy: Season 0 '),(316554,'Dune: Imperium '),(317985,'Beyond the Sun '),(324856,'The Crew: Mission Deep Sea '),(341169,'Great Western Trail (Second Edition) '),(342942,'Ark Nova ');
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
  CONSTRAINT `game_artists_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`),
  CONSTRAINT `game_artists_ibfk_2` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`artist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_artists`
--

LOCK TABLES `game_artists` WRITE;
/*!40000 ALTER TABLE `game_artists` DISABLE KEYS */;
INSERT INTO `game_artists` VALUES (224517,1),(224517,2),(224517,3),(161936,4),(341169,4),(162886,9),(220308,10),(187645,18),(187645,19),(187645,20),(187645,21),(316554,22),(316554,23),(316554,24),(162886,25),(162886,26),(162886,27),(256960,37),(285774,38),(102794,48),(102794,49),(170216,50),(170216,51),(170216,52),(170216,53),(324856,54);
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
  CONSTRAINT `game_category_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`),
  CONSTRAINT `game_category_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_category`
--

LOCK TABLES `game_category` WRITE;
/*!40000 ALTER TABLE `game_category` DISABLE KEYS */;
INSERT INTO `game_category` VALUES (102794,1),(220308,1),(224517,1),(256960,1),(341169,1),(224517,2),(224517,3),(256960,3),(224517,4),(224517,5),(161936,6),(161936,7),(102794,10),(162886,10),(170216,10),(162886,11),(170216,11),(170216,12),(220308,12),(102794,13),(341169,13),(220308,14),(256960,15),(256960,16),(220308,17),(324856,17),(220308,18),(162886,19),(220308,19),(162886,24),(170216,24),(285774,25),(324856,25),(256960,27),(256960,28),(285774,29),(285774,30),(102794,33),(324856,34),(341169,35);
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
  CONSTRAINT `game_designers_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`),
  CONSTRAINT `game_designers_ibfk_2` FOREIGN KEY (`designer_id`) REFERENCES `designers` (`designer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_designers`
--

LOCK TABLES `game_designers` WRITE;
/*!40000 ALTER TABLE `game_designers` DISABLE KEYS */;
INSERT INTO `game_designers` VALUES (224517,1),(224517,2),(224517,3),(161936,4),(161936,5),(162886,16),(220308,17),(220308,18),(256960,22),(285774,23),(102794,29),(170216,30),(324856,31),(341169,32);
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
  CONSTRAINT `game_mechanics_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`),
  CONSTRAINT `game_mechanics_ibfk_2` FOREIGN KEY (`mechanics_id`) REFERENCES `mechanics` (`mechanic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_mechanics`
--

LOCK TABLES `game_mechanics` WRITE;
/*!40000 ALTER TABLE `game_mechanics` DISABLE KEYS */;
INSERT INTO `game_mechanics` VALUES (161936,1),(224517,1),(256960,1),(285774,1),(324856,1),(341169,1),(224517,2),(224517,3),(224517,4),(224517,5),(161936,6),(170216,6),(256960,6),(161936,7),(285774,7),(324856,7),(161936,8),(161936,9),(170216,13),(324856,14),(102794,17),(170216,19),(256960,19),(170216,23),(170216,26),(256960,26),(341169,27),(102794,30),(256960,33),(285774,37),(285774,38),(324856,38),(102794,39),(285774,39),(341169,39),(102794,43),(102794,44),(102794,45),(324856,46),(341169,47),(341169,48);
/*!40000 ALTER TABLE `game_mechanics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_sellers`
--

DROP TABLE IF EXISTS `game_sellers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_sellers` (
  `game_id` int NOT NULL,
  `seller_id` int NOT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`game_id`,`seller_id`),
  KEY `fk_seller_id` (`seller_id`),
  CONSTRAINT `fk_game_id` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`),
  CONSTRAINT `fk_seller_id` FOREIGN KEY (`seller_id`) REFERENCES `sellers` (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_sellers`
--

LOCK TABLES `game_sellers` WRITE;
/*!40000 ALTER TABLE `game_sellers` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_sellers` ENABLE KEYS */;
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
  CONSTRAINT `game_stats_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_stats`
--

LOCK TABLES `game_stats` WRITE;
/*!40000 ALTER TABLE `game_stats` DISABLE KEYS */;
INSERT INTO `game_stats` VALUES (93,7.733,91,75,5587,1743471,48297,162,24928,5919,26461),(521,7.998,53,6,3230,1167388,179071,1221,14710,5658,15982),(2651,7.825,55,52,11140,3684597,145629,433,76033,11150,62641),(12333,8.256,14,2,9702,5439875,120408,337,64568,11701,46387),(18602,7.729,95,81,6342,2242758,66463,112,28259,5290,28527),(25613,7.865,78,56,4115,2678168,71326,29,17962,4254,18982),(28143,7.75,72,64,10615,3709845,643526,3065,65306,10228,52885),(35677,7.854,62,50,5776,2437651,78580,197,34605,9426,30151),(37111,7.731,92,30,7087,2735785,79347,139,38246,6425,35562),(55690,8.517,67,15,2030,5142578,44995,118,12083,6639,9085),(62219,7.824,85,63,4226,1984017,33607,168,22122,7053,20158),(68448,7.701,84,83,15582,4474296,545763,1969,133017,13006,98591),(72125,7.845,71,61,4993,3701499,53321,105,27580,7001,27828),(102794,7.969,43,41,5251,2770331,75412,447,41899,11327,32805),(110327,7.739,82,79,8759,2517077,168370,554,65614,10206,52825),(115746,8.528,8,1,3295,3397129,29698,300,31058,10366,18869),(121921,7.775,81,26,6869,4254150,107111,360,64687,12304,40971),(122515,7.741,94,76,3810,1741639,57460,118,25146,6367,21901),(124742,7.876,68,3,6030,4711282,330715,501,44620,5140,29202),(125153,8.036,65,46,2244,1307684,30775,265,17975,6146,13145),(126163,7.874,54,48,5372,2099566,109879,503,43269,8828,36951),(157354,7.779,75,68,5760,1918718,111239,531,51217,10705,39004),(159675,8.043,79,51,1884,1196352,30880,133,15230,5627,10200),(161533,8.192,57,39,1812,1284929,23419,223,14983,5328,9760),(161936,8.542,2,1,7474,3863849,0,639,77730,12828,50184),(162886,8.358,11,10,6782,5078103,235204,2827,64694,19107,43384),(164153,7.974,63,21,3580,3828548,87086,276,40337,6994,23607),(167791,8.381,6,6,12691,7668154,537928,3986,122978,21378,88892),(170042,7.749,98,86,3266,1459500,66916,355,28260,6741,21880),(170216,7.954,44,44,6393,3486139,89708,546,51679,12509,43430),(171623,7.801,83,65,3397,1586237,87868,283,25803,4730,23753),(172386,7.863,96,73,1926,1062228,26342,110,14427,3545,12742),(174430,8.627,3,2,10114,12234013,471284,2507,90470,19364,57739),(175914,8.088,37,29,3114,2240621,45462,273,22656,9127,18359),(180263,7.891,87,24,4384,4436070,67556,176,36341,10980,21141),(182028,8.32,13,11,4313,3406238,116418,708,33892,8931,29323),(182874,7.919,69,54,2886,1270294,80479,843,22670,5683,18233),(187645,8.416,9,6,4499,4091284,44722,315,45844,12586,29634),(191189,7.939,73,60,2872,1773134,95363,1001,26155,6920,18000),(192135,8.358,38,10,1996,2487186,46427,617,15408,9982,10544),(200680,7.964,76,58,1950,925936,42009,585,21079,2895,15318),(201808,7.796,74,71,4963,2315259,133182,743,50545,10400,38358),(205059,7.974,50,18,4457,3389464,82338,411,52440,11969,33311),(209010,7.986,64,19,2603,2018505,60282,269,23347,7748,16660),(216132,7.955,60,47,2833,1623849,63501,302,20978,6508,19025),(220308,8.412,12,8,3424,3007296,89956,853,29987,11420,24171),(221107,8.056,49,13,2394,1131988,112870,343,30110,4503,15652),(224517,8.618,1,1,5230,3254639,95651,1406,52017,15189,37595),(225694,7.782,97,1,2614,773357,61582,623,30341,5286,18890),(229853,7.883,80,59,2574,1562715,63038,486,24424,5349,18134),(230802,7.762,70,2,9769,2789652,533783,5929,121484,12771,78416),(231733,8.19,89,23,1750,1144384,32147,880,10880,6125,7466),(233078,8.623,5,3,3050,3184712,33164,373,25402,10410,20539),(236457,7.768,90,77,3709,1605500,85610,1468,35690,6827,25716),(244521,7.838,61,8,5387,1841196,198129,2242,63680,10252,41555),(253344,8.171,77,16,1568,1471078,34563,667,16793,4850,9464),(255984,8.336,56,12,1773,1954999,24953,919,20084,12811,7895),(256960,8.264,39,25,1985,1460924,36634,571,17227,5123,10950),(264220,8.149,88,22,2441,2318746,50281,399,21643,5737,10874),(266810,7.999,66,49,2186,1123919,44004,431,25488,5249,15308),(269385,7.946,101,25,2002,2300591,87249,924,25699,7044,14634),(276025,8.081,51,40,2057,1512418,48852,411,20245,6286,14109),(279537,8.017,93,66,1299,609732,34951,804,16451,5086,8808),(284083,7.858,58,7,4647,1326866,486646,3547,69330,5205,35858),(284378,8.467,59,32,974,707809,13817,321,10864,3806,5834),(285774,8.146,40,2,2693,3572457,372329,5228,34412,5039,20250),(291457,8.514,7,4,3983,2305202,136268,2135,62429,7403,28006),(314040,8.464,52,8,904,451781,46402,524,14050,3562,6136),(316554,8.388,10,9,4473,3244150,104543,3238,46881,11327,32990),(317985,7.967,86,57,1550,962695,39825,745,13675,6015,11184),(324856,8.243,35,2,1573,474044,140525,3913,24286,3971,11551),(341169,8.443,36,20,906,571761,24555,888,13103,3422,7815);
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
  `type_id` int NOT NULL,
  `min_num_players` int DEFAULT NULL,
  `max_num_players` int DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `year_published` int DEFAULT NULL,
  `min_time_duration` int DEFAULT NULL,
  `max_time_duration` int DEFAULT NULL,
  `age_limit` int DEFAULT NULL,
  PRIMARY KEY (`game_id`,`type_id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `general_info_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`site_id`),
  CONSTRAINT `general_info_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `types` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `general_info`
--

LOCK TABLES `general_info` WRITE;
/*!40000 ALTER TABLE `general_info` DISABLE KEYS */;
INSERT INTO `general_info` VALUES (12333,1,2,NULL,3.6,2005,120,180,13),(102794,1,1,7,3.78,2013,30,210,12),(161936,1,2,4,2.83,2015,60,NULL,13),(161936,2,2,4,2.83,2015,60,NULL,13),(162886,1,1,4,4.06,2017,90,120,13),(170216,1,2,4,2.88,2015,60,90,14),(175914,1,2,5,4.21,2015,120,240,14),(182028,1,2,4,4.43,2015,120,NULL,14),(187645,2,2,4,3.74,2016,180,240,14),(192135,1,1,4,3.86,2017,60,120,12),(220308,1,1,4,4.39,2017,60,150,12),(221107,1,2,4,3.25,2017,60,NULL,14),(224517,1,2,4,3.9,2018,60,120,14),(233078,1,3,6,4.3,2017,240,480,14),(256960,1,1,5,3.85,2019,45,120,13),(276025,1,1,4,3.91,2019,30,120,12),(285774,4,1,4,2.92,2019,45,90,14),(291457,1,1,4,3.63,2020,30,120,14),(314040,1,2,4,3.12,2020,45,60,14),(316554,1,1,4,3.02,2020,60,120,14),(324856,5,2,5,2.04,2021,20,NULL,10),(341169,1,1,4,3.71,2021,75,150,12);
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
  `machanic` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mechanic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mechanics`
--

LOCK TABLES `mechanics` WRITE;
/*!40000 ALTER TABLE `mechanics` DISABLE KEYS */;
INSERT INTO `mechanics` VALUES (1,'Hand Management'),(2,'Income'),(3,'Loans'),(4,'Market'),(5,'Network and Route Building'),(6,'Action Points'),(7,'Cooperative Game'),(8,'Legacy Game'),(9,'Point to Point Movement'),(10,'Action Queue'),(11,'Action Retrieval'),(12,'Campaign / Battle Card Driven'),(13,'Card Play Conflict Resolution'),(14,'Communication Limits'),(15,'End Game Bonuses'),(16,'Hexagon Grid'),(17,'Increase Value of Unchosen Resources'),(18,'Action Drafting'),(19,'Area Majority / Influence'),(20,'Area-Impulse'),(21,'Dice Rolling'),(22,'Follow'),(23,'Closed Drafting'),(24,'Contracts'),(25,'Enclosure'),(26,'Area Movement'),(27,'Deck, Bag, and Pool Building'),(28,'Delayed Purchase'),(29,'Force Commitment'),(30,'Automatic Resource Growth'),(31,'Modular Board'),(32,'Auction/Bidding'),(33,'Auction: Dutch'),(34,'Events'),(35,'Action/Event'),(36,'Advantage Token'),(37,'Deck Construction'),(38,'Scenario / Mission / Campaign Game'),(39,'Solo / Solitaire Game'),(40,'Die Icon Resolution'),(41,'Pick-up and Deliver'),(42,'Map Addition'),(43,'Tile Placement'),(44,'Turn Order: Claim Action'),(45,'Worker Placement'),(46,'Trick-taking'),(47,'Ownership'),(48,'Set Collection'),(49,'Flicking'),(50,'Team-Based Game'),(51,'Bias'),(52,'Auction: Turn Order Until Pass'),(53,'Catch the Leader'),(54,'Narrative Choice / Paragraph'),(55,'Open Drafting'),(56,'Variable Phase Order'),(57,'Commodity Speculation'),(58,'Grid Movement'),(59,'Line of Sight'),(60,'Investment'),(61,'Victory Points as a Resource'),(62,'Worker Placement, Different Worker Types'),(63,'Critical Hits and Failures'),(64,'Role Playing'),(65,'Race'),(66,'Secret Unit Deployment'),(67,'Pattern Building'),(68,'Multi-Use Cards'),(69,'Chit-Pull System'),(70,'Movement Points'),(71,'Constrained Bidding'),(72,'Hidden Victory Points'),(73,'Mancala'),(74,'Variable Player Powers'),(75,'Highest-Lowest Scoring'),(76,'Rondel'),(77,'Hidden Roles'),(78,'Resource to Move'),(79,'Neighbor Scope'),(80,'Simultaneous Action Selection'),(81,'Once-Per-Game Abilities'),(82,'Deduction'),(83,'Paper-and-Pencil'),(84,'Turn Order: Time Track'),(85,'Auction: Fixed Placement'),(86,'Auction: Multiple Lot'),(87,'Turn Order: Pass Order'),(88,'Variable Set-up'),(89,'Targeted Clues');
/*!40000 ALTER TABLE `mechanics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellers`
--

DROP TABLE IF EXISTS `sellers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sellers` (
  `seller_id` int NOT NULL AUTO_INCREMENT,
  `seller_name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellers`
--

LOCK TABLES `sellers` WRITE;
/*!40000 ALTER TABLE `sellers` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `types` (
  `type_id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `types`
--

LOCK TABLES `types` WRITE;
/*!40000 ALTER TABLE `types` DISABLE KEYS */;
INSERT INTO `types` VALUES (1,'Strategy'),(2,'Thematic'),(3,'Wargames'),(4,'Customizable'),(5,'Family'),(6,'Abstract'),(7,'Party');
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

-- Dump completed on 2023-04-23 15:03:50
