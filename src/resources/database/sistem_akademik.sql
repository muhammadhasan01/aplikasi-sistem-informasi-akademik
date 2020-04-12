-- MariaDB dump 10.17  Distrib 10.4.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: sistem_akademik
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jadwal`
--

DROP TABLE IF EXISTS `jadwal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jadwal` (
  `id_jadwal` int NOT NULL,
  PRIMARY KEY (`id_jadwal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jadwal`
--

LOCK TABLES `jadwal` WRITE;
/*!40000 ALTER TABLE `jadwal` DISABLE KEYS */;
INSERT INTO `jadwal` VALUES (1),(2),(3),(4),(5);
/*!40000 ALTER TABLE `jadwal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurusan`
--

DROP TABLE IF EXISTS `jurusan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jurusan` (
  `kode_jurusan` varchar(3) NOT NULL,
  `nama_jurusan` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`kode_jurusan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurusan`
--

LOCK TABLES `jurusan` WRITE;
/*!40000 ALTER TABLE `jurusan` DISABLE KEYS */;
INSERT INTO `jurusan` VALUES ('BIO','Biomedis'),('EL','Elektro'),('IF','Informatika'),('POW','Power'),('STI','Sistem Teknologi Informasi'),('TEL','Telkom');
/*!40000 ALTER TABLE `jurusan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mata_kuliah`
--

DROP TABLE IF EXISTS `mata_kuliah`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mata_kuliah` (
  `kode_matkul` char(5) NOT NULL,
  `nama_matkul` text NOT NULL,
  `deskripsi_matkul` text,
  `kode_jurusan` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`kode_matkul`),
  KEY `kode_jurusan` (`kode_jurusan`),
  CONSTRAINT `mata_kuliah_ibfk_1` FOREIGN KEY (`kode_jurusan`) REFERENCES `jurusan` (`kode_jurusan`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mata_kuliah`
--

LOCK TABLES `mata_kuliah` WRITE;
/*!40000 ALTER TABLE `mata_kuliah` DISABLE KEYS */;
INSERT INTO `mata_kuliah` VALUES ('BM410','Prosthetic Limbs','Membuat tangan dan kaki buatan dengan arduino','BIO'),('EL111','Arduino','Merangkai dan membuat program dengan arduino','EL'),('IF120','ESport','Belajar ESport seperti dota, scgo, dan TF2','IF'),('II121','Probabilitas dan statistika','Mempelajari kemungkinan dari suatu kejadian','STI'),('PW123','Kerja di PLN','Kerja praktik ke salah satu PLN','POW'),('TL110','Radar','Mempelajari server, host, dan cloud computing','TEL');
/*!40000 ALTER TABLE `mata_kuliah` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mata_kuliah_diambil`
--

DROP TABLE IF EXISTS `mata_kuliah_diambil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mata_kuliah_diambil` (
  `nim` varchar(3) NOT NULL,
  `kehadiran` int DEFAULT NULL,
  `indeks` enum('A','AB','B','BC','C','D','E') DEFAULT NULL,
  `kode_matkul` char(5) DEFAULT NULL,
  `semester` enum('GENAP','GANJIL') DEFAULT NULL,
  `tahun` int DEFAULT NULL,
  KEY `nim` (`nim`),
  KEY `semester` (`semester`,`tahun`,`kode_matkul`),
  CONSTRAINT `mata_kuliah_diambil_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `profil_mahasiswa` (`nim`) ON DELETE CASCADE,
  CONSTRAINT `mata_kuliah_diambil_ibfk_2` FOREIGN KEY (`semester`, `tahun`, `kode_matkul`) REFERENCES `waktu` (`semester`, `tahun`, `kode_matkul`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mata_kuliah_diambil`
--

LOCK TABLES `mata_kuliah_diambil` WRITE;
/*!40000 ALTER TABLE `mata_kuliah_diambil` DISABLE KEYS */;
INSERT INTO `mata_kuliah_diambil` VALUES ('001',0,'A','IF120','GANJIL',2018),('002',0,'A','PW123','GANJIL',2019);
/*!40000 ALTER TABLE `mata_kuliah_diambil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mata_kuliah_diampu`
--

DROP TABLE IF EXISTS `mata_kuliah_diampu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mata_kuliah_diampu` (
  `nip` varchar(3) NOT NULL,
  `total_pertemuan` int DEFAULT NULL,
  `kode_matkul` char(5) DEFAULT NULL,
  `semester` enum('GENAP','GANJIL') DEFAULT NULL,
  `tahun` int DEFAULT NULL,
  KEY `nip` (`nip`),
  KEY `semester` (`semester`,`tahun`,`kode_matkul`),
  CONSTRAINT `mata_kuliah_diampu_ibfk_1` FOREIGN KEY (`nip`) REFERENCES `profil_dosen` (`NIP`) ON DELETE CASCADE,
  CONSTRAINT `mata_kuliah_diampu_ibfk_2` FOREIGN KEY (`semester`, `tahun`, `kode_matkul`) REFERENCES `waktu` (`semester`, `tahun`, `kode_matkul`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mata_kuliah_diampu`
--

LOCK TABLES `mata_kuliah_diampu` WRITE;
/*!40000 ALTER TABLE `mata_kuliah_diampu` DISABLE KEYS */;
INSERT INTO `mata_kuliah_diampu` VALUES ('001',16,'IF120','GANJIL',2018);
/*!40000 ALTER TABLE `mata_kuliah_diampu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profil_dosen`
--

DROP TABLE IF EXISTS `profil_dosen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profil_dosen` (
  `NIP` varchar(3) NOT NULL,
  `nama_dosen` varchar(50) NOT NULL,
  `alamat_dosen` varchar(50) DEFAULT NULL,
  `no_hp` varchar(20) DEFAULT NULL,
  `email` text,
  `user_id_dosen` int DEFAULT NULL,
  `kode_jurusan` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`NIP`),
  KEY `user_id_dosen` (`user_id_dosen`),
  KEY `kode_jurusan` (`kode_jurusan`),
  CONSTRAINT `profil_dosen_ibfk_1` FOREIGN KEY (`user_id_dosen`) REFERENCES `user` (`id`),
  CONSTRAINT `profil_dosen_ibfk_2` FOREIGN KEY (`kode_jurusan`) REFERENCES `jurusan` (`kode_jurusan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profil_dosen`
--

LOCK TABLES `profil_dosen` WRITE;
/*!40000 ALTER TABLE `profil_dosen` DISABLE KEYS */;
INSERT INTO `profil_dosen` VALUES ('001','Rinilda Numir','Dago atas','087771123232','pakrin@gmail.com',4,'IF');
/*!40000 ALTER TABLE `profil_dosen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profil_mahasiswa`
--

DROP TABLE IF EXISTS `profil_mahasiswa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profil_mahasiswa` (
  `nim` varchar(3) NOT NULL,
  `angkatan` int DEFAULT NULL,
  `nama_mahasiswa` varchar(64) NOT NULL,
  `tempat_lahir` varchar(64) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `alamat_rumah` text,
  `alamat_tinggal` text,
  `email` text,
  `user_id_mahasiswa` int DEFAULT NULL,
  `kode_jurusan` char(5) DEFAULT NULL,
  `nip_dosen_wali` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`nim`),
  KEY `nip_dosen_wali` (`nip_dosen_wali`),
  KEY `user_id_mahasiswa` (`user_id_mahasiswa`),
  KEY `kode_jurusan` (`kode_jurusan`),
  CONSTRAINT `profil_mahasiswa_ibfk_1` FOREIGN KEY (`nip_dosen_wali`) REFERENCES `profil_dosen` (`NIP`),
  CONSTRAINT `profil_mahasiswa_ibfk_2` FOREIGN KEY (`user_id_mahasiswa`) REFERENCES `user` (`id`),
  CONSTRAINT `profil_mahasiswa_ibfk_3` FOREIGN KEY (`kode_jurusan`) REFERENCES `jurusan` (`kode_jurusan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profil_mahasiswa`
--

LOCK TABLES `profil_mahasiswa` WRITE;
/*!40000 ALTER TABLE `profil_mahasiswa` DISABLE KEYS */;
INSERT INTO `profil_mahasiswa` VALUES ('001',2018,'Dobleh','Bandung','2000-05-11','Tubis','Tubis','doblehkabur@gmail.com',1,'IF','001'),('002',2018,'Cobleh','Bandung','2001-05-21','Tubis','Tubis','coblehjugakabur@gmail.com',2,'IF','001'),('003',2019,'Arif','Bandung','2001-11-24','Tubis','Tubis','arifgadarmawan@gmail.com',3,'EL','001');
/*!40000 ALTER TABLE `profil_mahasiswa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slot_waktu`
--

DROP TABLE IF EXISTS `slot_waktu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slot_waktu` (
  `id_slot_waktu` int NOT NULL,
  `hari` varchar(6) NOT NULL,
  `waktu_mulai` time NOT NULL,
  `waktu_selesai` time NOT NULL,
  PRIMARY KEY (`id_slot_waktu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slot_waktu`
--

LOCK TABLES `slot_waktu` WRITE;
/*!40000 ALTER TABLE `slot_waktu` DISABLE KEYS */;
INSERT INTO `slot_waktu` VALUES (1,'senin','11:00:00','12:00:00'),(2,'selasa','12:00:00','13:00:00'),(3,'rabu','10:00:00','12:00:00'),(4,'kamis','14:00:00','16:00:00'),(5,'jumat','15:00:00','17:00:00');
/*!40000 ALTER TABLE `slot_waktu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slot_waktu_jadwal`
--

DROP TABLE IF EXISTS `slot_waktu_jadwal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slot_waktu_jadwal` (
  `id_jadwal` int DEFAULT NULL,
  `id_slot_waktu` int DEFAULT NULL,
  KEY `id_jadwal` (`id_jadwal`),
  KEY `id_slot_waktu` (`id_slot_waktu`),
  CONSTRAINT `slot_waktu_jadwal_ibfk_1` FOREIGN KEY (`id_jadwal`) REFERENCES `jadwal` (`id_jadwal`) ON DELETE CASCADE,
  CONSTRAINT `slot_waktu_jadwal_ibfk_2` FOREIGN KEY (`id_slot_waktu`) REFERENCES `slot_waktu` (`id_slot_waktu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slot_waktu_jadwal`
--

LOCK TABLES `slot_waktu_jadwal` WRITE;
/*!40000 ALTER TABLE `slot_waktu_jadwal` DISABLE KEYS */;
INSERT INTO `slot_waktu_jadwal` VALUES (1,1),(1,2),(2,3),(2,1),(2,2),(3,4),(4,5),(5,1),(5,2);
/*!40000 ALTER TABLE `slot_waktu_jadwal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` enum('admin','dosen','mahasiswa') NOT NULL,
  `image` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'dobleh','dobleh?kabur','mahasiswa','-'),(2,'cobleh','cobleh?kabur','mahasiswa','-'),(3,'arif','sayainiduaorang','mahasiswa','-'),(4,'pakrin','StrategiAlgoritma','dosen','-'),(5,'hasan','doyanngecp','admin','-');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `waktu`
--

DROP TABLE IF EXISTS `waktu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `waktu` (
  `semester` enum('GENAP','GANJIL') NOT NULL,
  `tahun` int NOT NULL,
  `kode_matkul` varchar(5) NOT NULL,
  `id_jadwal` int NOT NULL,
  PRIMARY KEY (`semester`,`tahun`,`kode_matkul`),
  KEY `kode_matkul` (`kode_matkul`),
  KEY `id_jadwal` (`id_jadwal`),
  CONSTRAINT `waktu_ibfk_1` FOREIGN KEY (`kode_matkul`) REFERENCES `mata_kuliah` (`kode_matkul`),
  CONSTRAINT `waktu_ibfk_2` FOREIGN KEY (`id_jadwal`) REFERENCES `jadwal` (`id_jadwal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waktu`
--

LOCK TABLES `waktu` WRITE;
/*!40000 ALTER TABLE `waktu` DISABLE KEYS */;
INSERT INTO `waktu` VALUES ('GANJIL',2018,'IF120',1),('GANJIL',2019,'II121',2),('GENAP',2019,'BM410',3),('GENAP',2019,'EL111',3),('GENAP',2019,'TL110',4),('GANJIL',2019,'PW123',5);
/*!40000 ALTER TABLE `waktu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-11 22:59:51
