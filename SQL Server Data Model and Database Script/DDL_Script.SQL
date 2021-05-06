/*
Created: 4/16/2021
Modified: 4/17/2021
Model: Microsoft SQL Server 2014
Database: MS SQL Server 2014
*/


-- Create tables section -------------------------------------------------

-- Table Domain

CREATE TABLE [Domain]
(
 [DBName] Varchar(100) NOT NULL,
 [DomainName] Varchar(50) NOT NULL
)
go

-- Add keys for table Domain

ALTER TABLE [Domain] ADD CONSTRAINT [PK_Domain] PRIMARY KEY ([DBName])
go

-- Table BusinessTerm

CREATE TABLE [BusinessTerm]
(
 [BusinessId] Int IDENTITY(100,1) NOT NULL,
 [BusinessDesc] Varchar(max) NOT NULL,
 [Bustype] Varchar(50) NOT NULL
)
go

-- Add keys for table BusinessTerm

ALTER TABLE [BusinessTerm] ADD CONSTRAINT [PK_BusinessTerm] PRIMARY KEY ([BusinessId])
go

-- Table Nodes

CREATE TABLE [Nodes]
(
 [NodeId] Int IDENTITY(1,1) NOT NULL,
 [Label] Varchar(50) NOT NULL,
 [Counts] Int NOT NULL,
 [DBName] Varchar(100) NULL
)
go

-- Create indexes for table Nodes

CREATE INDEX [IX_Relationship57] ON [Nodes] ([DBName])
go

-- Add keys for table Nodes

ALTER TABLE [Nodes] ADD CONSTRAINT [PK_Nodes] PRIMARY KEY ([NodeId])
go

-- Table Property

CREATE TABLE [Property]
(
 [PropertyId] Int IDENTITY(10,1) NOT NULL,
 [TechTerm] Varchar(max) NOT NULL,
 [UniqueConstraints] Varchar(50) NOT NULL,
 [ExistingConstraints] Varchar(50) NOT NULL,
 [NodeId] Int NOT NULL
)
go

-- Create indexes for table Property

CREATE INDEX [IX_Relationship58] ON [Property] ([NodeId])
go

-- Add keys for table Property

ALTER TABLE [Property] ADD CONSTRAINT [PK_Property] PRIMARY KEY ([PropertyId])
go

-- Table Relationship

CREATE TABLE [Relationship]
(
 [RelationId] Int IDENTITY(200,1) NOT NULL,
 [RelDesc] Varchar(100) NOT NULL,
 [NodeId] Int NOT NULL
)
go

-- Create indexes for table Relationship

CREATE INDEX [IX_Relationship56] ON [Relationship] ([NodeId])
go

-- Add keys for table Relationship

ALTER TABLE [Relationship] ADD CONSTRAINT [PK_Relationship] PRIMARY KEY ([RelationId])
go

-- Table DomBusBrdge

CREATE TABLE [DomBusBrdge]
(
 [DBName] Varchar(100) NOT NULL,
 [BusinessId] Int NOT NULL
)
go

-- Add keys for table DomBusBrdge

ALTER TABLE [DomBusBrdge] ADD CONSTRAINT [PK_DomBusBrdge] PRIMARY KEY ([DBName],[BusinessId])
go

-- Table BusPropBridge

CREATE TABLE [BusPropBridge]
(
 [PropertyId] Int NOT NULL,
 [BusinessId] Int NOT NULL
)
go

-- Add keys for table BusPropBridge

ALTER TABLE [BusPropBridge] ADD CONSTRAINT [PK_BusPropBridge] PRIMARY KEY ([PropertyId],[BusinessId])
go

-- Create foreign keys (relationships) section ------------------------------------------------- 


ALTER TABLE [DomBusBrdge] ADD CONSTRAINT [contains] FOREIGN KEY ([DBName]) REFERENCES [Domain] ([DBName]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [DomBusBrdge] ADD CONSTRAINT [associate] FOREIGN KEY ([BusinessId]) REFERENCES [BusinessTerm] ([BusinessId]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [BusPropBridge] ADD CONSTRAINT [matches] FOREIGN KEY ([PropertyId]) REFERENCES [Property] ([PropertyId]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [BusPropBridge] ADD CONSTRAINT [relates] FOREIGN KEY ([BusinessId]) REFERENCES [BusinessTerm] ([BusinessId]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [Relationship] ADD CONSTRAINT [has] FOREIGN KEY ([NodeId]) REFERENCES [Nodes] ([NodeId]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [Nodes] ADD CONSTRAINT [includes] FOREIGN KEY ([DBName]) REFERENCES [Domain] ([DBName]) ON UPDATE NO ACTION ON DELETE NO ACTION
go



ALTER TABLE [Property] ADD CONSTRAINT [consists] FOREIGN KEY ([NodeId]) REFERENCES [Nodes] ([NodeId]) ON UPDATE NO ACTION ON DELETE NO ACTION
go




