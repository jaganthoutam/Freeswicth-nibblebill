-- MySQL dump 10.11
--
-- Host: localhost    Database: billing
-- ------------------------------------------------------
-- Server version	5.0.95

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `pricelist_id` int(20) NOT NULL,
  `name` varchar(255) default NULL,
  `cash` double NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (2013011,1,'2013011',9.998923),(2013010,2,'JAGAN',0.04);
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dialplan`
--

DROP TABLE IF EXISTS `dialplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dialplan` (
  `id` int(20) NOT NULL auto_increment COMMENT 'ID for account',
  `pricelist_id` int(20) NOT NULL,
  `prefix` int(20) NOT NULL,
  `price_buy` double NOT NULL,
  `price_sell` double NOT NULL,
  `incriment` int(2) default NULL,
  `provider` varchar(20) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `prefix` (`prefix`),
  KEY `prefix_2` (`prefix`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dialplan`
--

LOCK TABLES `dialplan` WRITE;
/*!40000 ALTER TABLE `dialplan` DISABLE KEYS */;
INSERT INTO `dialplan` VALUES (1,2,12,0.0084,0.0092,6,'VOIPPRO'),(2,1,1212,0.0089,0.0098,6,'COMMPEAK'),(3,1,12127,0.0089,0.0098,6,'COMMPEAK'),(4,2,918,0.0089,0.0098,6,'COMMPEAK'),(5,2,123,0.0089,0.0098,6,'COMMPEAK'),(6,1,121,0.0089,0.0098,6,'COMMPEAK');
/*!40000 ALTER TABLE `dialplan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sip_users`
--

DROP TABLE IF EXISTS `sip_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sip_users` (
  `id` int(10) NOT NULL auto_increment,
  `user` varchar(25) NOT NULL,
  `pass` varchar(25) NOT NULL,
  `account_code` int(20) NOT NULL,
  `Domain` varchar(25) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `account_code` (`account_code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sip_users`
--

LOCK TABLES `sip_users` WRITE;
/*!40000 ALTER TABLE `sip_users` DISABLE KEYS */;
INSERT INTO `sip_users` VALUES (1,'2013010','2101301',2013010,'172.18.9.250'),(2,'2013011','2013011',2013011,'172.18.9.250');
/*!40000 ALTER TABLE `sip_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-11 12:45:00

