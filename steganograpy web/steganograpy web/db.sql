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
  `image` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`aid`,`wid`,`tmid`,`date`,`work`,`status`,`datetocom`,`image`) values 
(1,28,16,'2023-05-07','dodododododood','pending','2023-05-25','20230507111838.png'),
(2,32,49,'2023-05-07','yoyoyoyoyo','completed','2023-05-26','20230507150431.png');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(500) NOT NULL,
  `password` varchar(500) NOT NULL,
  `type` varchar(500) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'HR','123','HR'),
(7,'Harshi05','Harshi05','TL'),
(8,'Parvathi05','Parvathi05','TL'),
(14,'Sneha05','Sneha05','TL'),
(16,'Aswanth05','Aswanth05','TM'),
(19,'Sajna05','Sajna05','TM'),
(20,'Sajna05','Sajna05','TM'),
(21,'Sajna05','Sajna05','TM'),
(22,'Sajna05','Sajna05','TM'),
(23,'Sajna05','Sajna05','TM'),
(24,'Sajna05','Sajna05','TM'),
(25,'Sajna05','Sajna05','TM'),
(26,'Sajna05','Sajna05','TM'),
(27,'Sajna05','Sajna05','TM'),
(28,'Sajna05','Sajna05','TM'),
(29,'Sajna05','Sajna05','TM'),
(30,'Sajna05','Sajna05','TM'),
(31,'Sajna05','Sajna05','TM'),
(32,'Sajna05','Sajna05','TM'),
(33,'Sajna05','Sajna05','TM'),
(34,'Sajna05','Sajna05','TM'),
(35,'Sajna05','Sajna05','TM'),
(37,'','','TM'),
(38,'','','TM'),
(39,'','','TM'),
(40,'Manu05','Manu05','TM'),
(41,'Vijay05','Vijay05','TM'),
(42,'Akshay05','Akshay05','TM'),
(43,'Pallavi05','Pallavi@05','TM'),
(45,'Haritha05','Haritha@05','TL'),
(46,'Nisha@05','Nisha@05','TL'),
(47,'Medha@05','Medha@05','TM'),
(48,'Shilpa@05','Shilpa@05','TL'),
(49,'Sreenath@05','Sreenath@05','TM');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) DEFAULT NULL,
  `report` varchar(300) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `date` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`rid`,`title`,`report`,`lid`,`date`) values 
(1,'gioiioo','bus_notused.jpg',16,'2023-04-18'),
(2,'hhhh','bus1.jpg',16,'2023-04-18'),
(3,'kkkkk','dataflow1.png',40,'2023-04-21'),
(4,'fgjfjfj','dfd.png',40,'2023-04-25'),
(5,'Aswanthreport','Blank_diagram2.png',16,'2023-04-25'),
(6,'sreenaths report','dataflow2.png',49,'2023-05-07');

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `team_lead` */

insert  into `team_lead`(`tid`,`lid`,`Fname`,`Lname`,`age`,`email`,`phone`) values 
(3,7,'Harshida','PV',23,'harshida@gmail.com\"\"\"\"\"',7834785687),
(4,8,'Parvathi','pp\"',22,'parvathi@gmail.com\"',7464848388),
(6,14,'sneha','pm',22,'snehapmanohar05@gmail.com',9895249312),
(8,45,'Haritha','Ashokh',27,'haritha@gmail.com',9848588282),
(9,46,'nisha','vijay',29,'niisha@gmail.com',9999992399),
(10,48,'shilpa','das',25,'shilpa@gmail.com',9897456312);

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `team_member` */

insert  into `team_member`(`tmid`,`lid`,`fname`,`lname`,`age`,`email`,`phone`,`tid`) values 
(9,40,'MANU','NAIR',26,'manu@gmal.com',45534657,14),
(10,41,'vijay','sekhar',28,'vijay@gmail.com',3275628635,14),
(11,42,'Akshay','Das',24,'akshay@gmail.com',764667868,5),
(12,43,'Pallavi','Reghunath',22,'pallavi@gmail.com',9895249312,14),
(13,47,'Medha','Das',25,'medha@gmail.com',9856234212,46),
(14,49,'sreenath','raveendran',26,'sreenath@gmail.com',9897465312,48),
(16,16,'ASWANTH','V',26,'aswanth@gmail.com',487438789,14);

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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

/*Data for the table `worktable` */

insert  into `worktable`(`wid`,`work_type`,`image`,`teamlead`,`date_to_be_completed`,`date`,`status`) values 
(28,'TESTING','img1.jpg','14','2023-04-25','2023-04-21','Allocated'),
(29,'ppppppp','wrk1.png','14','2023-04-28','2023-04-21','Allocated'),
(30,'VERIFICATION','dataflow2.png','7','0000-00-00','2023-04-25','pending'),
(31,'just check it','dataflow2.png','46','2023-05-25','2023-05-04','Allocated'),
(32,'check check','cloud_new.jpg','48','2023-05-24','2023-05-07','Allocated');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
