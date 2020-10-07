-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: elevage
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

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
-- Table structure for table `Animal`
--

DROP TABLE IF EXISTS `Animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Animal` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `espece` varchar(40) NOT NULL,
  `sexe` char(1) DEFAULT NULL,
  `date_naissance` datetime NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `commentaires` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Animal`
--

LOCK TABLES `Animal` WRITE;
/*!40000 ALTER TABLE `Animal` DISABLE KEYS */;
INSERT INTO `Animal` VALUES (1,'chien','M','2010-04-05 13:43:00','Rox','Mordille beaucoup'),(2,'chat',NULL,'2010-03-24 02:23:00','Roucky',NULL),(3,'chat','F','2010-09-13 15:02:00','Schtroumpfette',NULL),(4,'tortue','F','2009-08-03 05:12:00',NULL,NULL),(5,'chat',NULL,'2010-10-03 16:44:00','Choupi','Né sans oreille gauche'),(6,'tortue','F','2009-06-13 08:17:00','Bobosse','Carapace bizarre'),(7,'chien','F','2008-12-06 05:18:00','Caroline',NULL),(8,'chat','M','2008-09-11 15:38:00','Bagherra',NULL),(9,'tortue',NULL,'2010-08-23 05:18:00',NULL,NULL),(10,'chien','F','2008-02-20 15:45:00','Canaille',NULL),(11,'chien','F','2009-05-26 08:54:00','Cali',NULL),(12,'chien','F','2007-04-24 12:54:00','Rouquine',NULL),(13,'chien','F','2009-05-26 08:56:00','Fila',NULL),(14,'chien','F','2008-02-20 15:47:00','Anya',NULL),(15,'chien','F','2009-05-26 08:50:00','Louya',NULL),(16,'chien','F','2008-03-10 13:45:00','Welva',NULL),(17,'chien','F','2007-04-24 12:59:00','Zira',NULL),(18,'chien','F','2009-05-26 09:02:00','Java',NULL),(19,'chien','M','2007-04-24 12:45:00','Balou',NULL),(20,'chien','M','2008-03-10 13:43:00','Pataud',NULL),(21,'chien','M','2007-04-24 12:42:00','Bouli',NULL),(22,'chien','M','2009-03-05 13:54:00','Zoulou',NULL),(23,'chien','M','2007-04-12 05:23:00','Cartouche',NULL),(24,'chien','M','2006-05-14 15:50:00','Zambo',NULL),(25,'chien','M','2006-05-14 15:48:00','Samba',NULL),(26,'chien','M','2008-03-10 13:40:00','Moka',NULL),(27,'chien','M','2006-05-14 15:40:00','Pilou',NULL),(28,'chat','M','2009-05-14 06:30:00','Fiero',NULL),(29,'chat','M','2007-03-12 12:05:00','Zonko',NULL),(30,'chat','M','2008-02-20 15:45:00','Filou',NULL),(31,'chat','M','2007-03-12 12:07:00','Farceur',NULL),(32,'chat','M','2006-05-19 16:17:00','Caribou',NULL),(33,'chat','M','2008-04-20 03:22:00','Capou',NULL),(34,'chat','M','2006-05-19 16:56:00','Raccou','Pas de queue depuis la naissance'),(104,'chat','M','2009-05-14 06:42:00','Boucan',NULL),(105,'chat','F','2006-05-19 16:06:00','Callune',NULL),(106,'chat','F','2009-05-14 06:45:00','Boule',NULL),(107,'chat','F','2008-04-20 03:26:00','Zara',NULL),(108,'chat','F','2007-03-12 12:00:00','Milla',NULL),(109,'chat','F','2006-05-19 15:59:00','Feta',NULL),(110,'chat','F','2008-04-20 03:20:00','Bilba','Sourde de l\'oreille droite à 80%'),(111,'chat','F','2007-03-12 11:54:00','Cracotte',NULL),(112,'chat','F','2006-05-19 16:16:00','Cawette',NULL),(113,'tortue','F','2007-04-01 18:17:00','Nikki',NULL),(114,'tortue','F','2009-03-24 08:23:00','Tortilla',NULL),(115,'tortue','F','2009-03-26 01:24:00','Scroupy',NULL),(116,'tortue','F','2006-03-15 14:56:00','Lulla',NULL),(117,'tortue','F','2008-03-15 12:02:00','Dana',NULL),(118,'tortue','F','2009-05-25 19:57:00','Cheli',NULL),(119,'tortue','F','2007-04-01 03:54:00','Chicaca',NULL),(120,'tortue','F','2006-03-15 14:26:00','Redbul','Insomniaque'),(121,'tortue','M','2007-04-02 01:45:00','Spoutnik',NULL),(122,'tortue','M','2008-03-16 08:20:00','Bubulle',NULL),(123,'tortue','M','2008-03-15 18:45:00','Relou','Surpoids'),(124,'tortue','M','2009-05-25 18:54:00','Bulbizard',NULL),(125,'perroquet','M','2007-03-04 19:36:00','Safran',NULL),(126,'perroquet','M','2008-02-20 02:50:00','Gingko',NULL),(127,'perroquet','M','2009-03-26 08:28:00','Bavard',NULL),(128,'perroquet','F','2009-03-26 07:55:00','Parlotte',NULL);
/*!40000 ALTER TABLE `Animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Test_tuto`
--

DROP TABLE IF EXISTS `Test_tuto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Test_tuto` (
  `id` int NOT NULL,
  `prenom` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Test_tuto`
--

LOCK TABLES `Test_tuto` WRITE;
/*!40000 ALTER TABLE `Test_tuto` DISABLE KEYS */;
/*!40000 ALTER TABLE `Test_tuto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-30 12:45:12
