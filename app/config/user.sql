/*
SQLyog Professional v12.08 (64 bit)
MySQL - 5.7.20-log : Database - mahout
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mahout` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mahout`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` char(2) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `occupation` int(255) DEFAULT NULL,
  `zip_code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6048 DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`id`,`gender`,`age`,`occupation`,`zip_code`) values (93,'M',25,17,'95825'),(94,'M',25,17,'28601'),(95,'M',45,0,'98201'),(96,'F',25,16,'78028'),(97,'F',35,3,'66210'),(98,'F',35,7,'33547'),(99,'F',1,10,'19390'),(100,'M',35,17,'95401'),(6043,'F',18,1,'10000'),(6044,'F',18,1,'10000'),(6045,'F',18,1,'10000'),(6046,'F',18,1,'10000'),(6047,'F',18,1,'10000');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
