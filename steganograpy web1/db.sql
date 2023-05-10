/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - steganography
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`steganography` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `steganography`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `wid` int(11) DEFAULT NULL,
  `tmid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `work` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  `datetocom` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`aid`,`wid`,`tmid`,`date`,`work`,`status`,`datetocom`) values 
(1,NULL,16,'2023-03-27','aaa','pending','2023-03-27'),
(2,5,16,'2023-03-27','aksksk','ggg','2023-03-27'),
(3,5,15,'2023-03-27','ssss','pending',''),
(4,20,16,'2023-03-27','ssssssssss','pending','2023-03-27'),
(5,7,15,'2023-03-28','testing','completed','2023-03-28');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL,
  `type` varchar(500) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'HR','123','HR'),
(5,'Parvathi05','Parvathi05','TM'),
(7,'Harshi05','Harshi05','TL'),
(8,'Parvathi05','Parvathi05','TL'),
(12,'','','TM'),
(14,'Sneha05','Sneha05','TL'),
(15,'Anu05','Anu05','TM'),
(16,'Aswanth05','Aswanth05','TM'),
(17,'Nandhu05','Nandhu05','TL');

/*Table structure for table `team_lead` */

DROP TABLE IF EXISTS `team_lead`;

CREATE TABLE `team_lead` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `Fname` varchar(500) NOT NULL,
  `Lname` varchar(500) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `team_lead` */

insert  into `team_lead`(`tid`,`lid`,`Fname`,`Lname`,`age`,`email`,`phone`) values 
(3,7,'Harshida','PV',22,'harshida@gmail.com\"\"\"',7834785687),
(4,8,'Parvathi','pp\"',22,'parvathi@gmail.com\"',7464848388),
(6,14,'sneha','pm',22,'snehapmanohar05@gmail.com',9895249312),
(7,17,'Nandhu','krishna',23,'nandhu@gmail.com',56886896);

/*Table structure for table `team_member` */

DROP TABLE IF EXISTS `team_member`;

CREATE TABLE `team_member` (
  `tmid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(30) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone` bigint(11) NOT NULL,
  `tid` int(11) NOT NULL,
  PRIMARY KEY (`tmid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `team_member` */

insert  into `team_member`(`tmid`,`lid`,`fname`,`lname`,`age`,`email`,`phone`,`tid`) values 
(4,12,'Harshida','PV',0,'harshida@gmail.com',7834785687,3),
(6,15,'chinnu','PP',21,'anu@gmail.com',493893589,14),
(7,16,'ASWANTH','V',25,'aswanth@gmail.com',487438789,14);

/*Table structure for table `worktable` */

DROP TABLE IF EXISTS `worktable`;

CREATE TABLE `worktable` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `work_type` varchar(500) NOT NULL,
  `image` varchar(500) NOT NULL,
  `teamlead` varchar(500) NOT NULL,
  `date_to_be_completed` date NOT NULL,
  `date` date NOT NULL,
  `status` varchar(500) NOT NULL,
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `worktable` */

insert  into `worktable`(`wid`,`work_type`,`image`,`teamlead`,`date_to_be_completed`,`date`,`status`) values 
(1,'fgfgfg','background.png','fgfgg','2023-03-17','0000-00-00','pendiing'),
(2,'testing','background.png','3','2023-03-17','0000-00-00','pendiing'),
(3,'testing','background.png','3','0000-00-00','2023-03-17','pending'),
(4,'nsnne','bus2.jpg','3','0000-00-00','2023-03-17','pending'),
(5,'shdw','bus3.jpg','14','0000-00-00','2023-03-17','pending'),
(6,'sdfsdfs','user_default.jpg','3','0000-00-00','2023-03-17','pending'),
(7,'sdgsg','bus3.jpg','14','0000-00-00','2023-03-17','pending'),
(8,'nsnne','user_default.jpg','3','2023-03-17','0000-00-00','pending'),
(9,'testing','background.png','14','2023-03-23','0000-00-00','pending'),
(10,'testing','bus_notused.jpg','3','2023-03-23','0000-00-00','completed'),
(11,'coding','bus2.jpg','3','0000-00-00','2023-03-23','pending'),
(12,'sdfg','background.png','3','2023-03-31','2023-03-23','pending'),
(13,'coding','user_default.jpg','3','2023-03-30','2023-03-23','pending'),
(14,'kkkkkkk','background.png','3','2023-04-05','2023-03-24','pending'),
(15,'ppppp','bus_notused.jpg','3','2023-04-05','2023-03-24','pending'),
(16,'coding','bus5.jpg','8','2023-04-13','2023-03-24','pending'),
(17,'testing','bus4.jpg','7','2023-04-13','2023-03-24','pending'),
(18,'codiing','bus3.jpg','14','2023-03-30','2023-03-27','pending'),
(19,'TESTNG','bus3.jpg','7','2023-03-27','2023-03-27','pending'),
(20,'CODING','bus3.jpg','14','2023-03-27','2023-03-27','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
