-- project description
-- date : 201X.00.00
-- author :

-- --------------------------------------------------------------------------
-- DROP TABLE IF EXISTS `member`;
CREATE TABLE IF NOT EXISTS `member` (
    `no`                    INT                 NOT NULL AUTO_INCREMENT,
    `uid`                   VARCHAR(40)         NOT NULL,
    `pwd`                   VARCHAR(100)        NOT NULL,
    `salt`                  VARCHAR(100)        NOT NULL,
    `username`              VARCHAR(30)         NOT NULL,
    `nickname`              VARCHAR(30)         DEFAULT NULL,
    `email`                 VARCHAR(50)         DEFAULT NULL,
    `phone`                 VARCHAR(20)         DEFAULT NULL,
    `level`                 TINYINT             NOT NULL DEFAULT 0,
    `point`                 INT                 NOT NULL DEFAULT 0,
    `regist_dt`             DATETIME            NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `login_dt`              DATETIME            NULL,
    `status`                TINYINT             NOT NULL DEFAULT 0,
    PRIMARY KEY  (`no`),
    KEY `uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='member';
