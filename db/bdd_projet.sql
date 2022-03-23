-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: bdd_projet
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employe`
--

DROP TABLE IF EXISTS `employe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employe` (
  `Nom` varchar(45) NOT NULL,
  `Prenom` varchar(45) NOT NULL,
  `Adresse_mail` varchar(45) NOT NULL,
  `id_employe` int NOT NULL AUTO_INCREMENT,
  `questionnaire_idquestionnaire` int NOT NULL,
  `organisation_groupe` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`id_employe`),
  KEY `fk_employe_questionnaire1_idx` (`questionnaire_idquestionnaire`),
  KEY `fk_employe_organisation1_idx` (`organisation_groupe`),
  CONSTRAINT `fk_employe_organisation1` FOREIGN KEY (`organisation_groupe`) REFERENCES `organisation` (`groupe`),
  CONSTRAINT `fk_employe_questionnaire1` FOREIGN KEY (`questionnaire_idquestionnaire`) REFERENCES `questionnaire` (`idquestionnaire`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employe`
--

LOCK TABLES `employe` WRITE;
/*!40000 ALTER TABLE `employe` DISABLE KEYS */;
INSERT INTO `employe` VALUES ('Reinling','Robin','ouioui@gmail.com',1,1,'1','ouioui'),('Sourisse','Robin','nonnon@gmail.com',2,1,'1','nonnon');
/*!40000 ALTER TABLE `employe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `id_manager` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(45) DEFAULT NULL,
  `Prenom` varchar(45) DEFAULT NULL,
  `adresse_mail` varchar(45) DEFAULT NULL,
  `organisation_groupe` varchar(45) NOT NULL,
  `questionnaire_idquestionnaire` int NOT NULL,
  `questionnaire_resultat_questionnaire_id_result_questionnaire` int NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`id_manager`),
  KEY `fk_manager_organisation1_idx` (`organisation_groupe`),
  KEY `fk_manager_questionnaire1_idx` (`questionnaire_idquestionnaire`,`questionnaire_resultat_questionnaire_id_result_questionnaire`),
  CONSTRAINT `fk_manager_organisation1` FOREIGN KEY (`organisation_groupe`) REFERENCES `organisation` (`groupe`),
  CONSTRAINT `fk_manager_questionnaire1` FOREIGN KEY (`questionnaire_idquestionnaire`, `questionnaire_resultat_questionnaire_id_result_questionnaire`) REFERENCES `questionnaire` (`idquestionnaire`, `resultat_questionnaire_id_result_questionnaire`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organisation`
--

DROP TABLE IF EXISTS `organisation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organisation` (
  `groupe` varchar(45) NOT NULL,
  `nom` varchar(45) DEFAULT NULL,
  `adresse` varchar(45) DEFAULT NULL,
  `questionnaire_idquestionnaire` int NOT NULL,
  PRIMARY KEY (`groupe`),
  KEY `fk_organisation_questionnaire1_idx` (`questionnaire_idquestionnaire`),
  CONSTRAINT `fk_organisation_questionnaire1` FOREIGN KEY (`questionnaire_idquestionnaire`) REFERENCES `questionnaire` (`idquestionnaire`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organisation`
--

LOCK TABLES `organisation` WRITE;
/*!40000 ALTER TABLE `organisation` DISABLE KEYS */;
INSERT INTO `organisation` VALUES ('1','tropfort','9 rue du ouioui',1);
/*!40000 ALTER TABLE `organisation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire`
--

DROP TABLE IF EXISTS `questionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire` (
  `idquestionnaire` int NOT NULL,
  `question_libelle` varchar(45) NOT NULL,
  `question_description` varchar(45) DEFAULT NULL,
  `resultat_questionnaire_id_result_questionnaire` int NOT NULL,
  PRIMARY KEY (`idquestionnaire`,`resultat_questionnaire_id_result_questionnaire`),
  KEY `fk_questionnaire_resultat_questionnaire1_idx` (`resultat_questionnaire_id_result_questionnaire`),
  CONSTRAINT `fk_questionnaire_resultat_questionnaire1` FOREIGN KEY (`resultat_questionnaire_id_result_questionnaire`) REFERENCES `resultat_questionnaire` (`id_result_questionnaire`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire`
--

LOCK TABLES `questionnaire` WRITE;
/*!40000 ALTER TABLE `questionnaire` DISABLE KEYS */;
INSERT INTO `questionnaire` VALUES (1,'1','ouioui',1);
/*!40000 ALTER TABLE `questionnaire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resultat_questionnaire`
--

DROP TABLE IF EXISTS `resultat_questionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resultat_questionnaire` (
  `nombre_personne_rep` int NOT NULL,
  `score` int NOT NULL,
  `id_result_questionnaire` int NOT NULL,
  PRIMARY KEY (`id_result_questionnaire`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultat_questionnaire`
--

LOCK TABLES `resultat_questionnaire` WRITE;
/*!40000 ALTER TABLE `resultat_questionnaire` DISABLE KEYS */;
INSERT INTO `resultat_questionnaire` VALUES (2,2,1);
/*!40000 ALTER TABLE `resultat_questionnaire` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-17 12:13:22
