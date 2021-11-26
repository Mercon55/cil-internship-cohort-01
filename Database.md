# Extensive comparison of different use cases of different databases
## What is a database     
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Its is a collection of tables. Each table has a structured recurring collection of facts about a single item. For example, a table for clients, students, orders, and items. It is frequently shown visually as a spreadsheet. Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database. It is an organized collection of interrelated data stored in a computer. Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized.

A database has numerous importance and some of those important functions are highlighted below:

- A database gives us a highly efficient method for handling large amount of different types of data with ease.

- A database allows large amount of data to be stored systematically and these data to be easily retrieved, filtered, sorted and updated efficiently and accurately.

- A database enforces the intergrity of the data available by ensuring the validity of the data security.

## Different kinds of databases
There are different types of databases and they are:
- Centralized database
- Cloud database
- Commercial database
- Distributed database
- End-user database
- Graph database
- NoSQL database
- Object-oriented database
- Open-source database
- Operational database
- Personal database
- Relational database

### Centralized database
A centralized database is one that operates entirely within a single location. Centralized databases are typically used by bigger organizations, such as a business or university. The database itself is located on a central computer or database system. Users can access the database through a computer network, but it is the central computer that runs and maintains the database.

The information(data) is stored at a centralized location and the users from different locations can access this data. This type of database contains application procedures that help the users to access the data even from a remote location.

Various kinds of authentication procedures are applied for the verification and validation of end users, likewise, a registration number is provided by the application procedures which keeps a track and record of data usage. The local area office handles this thing.

It comforts the users to access the stored data from different locations through several applications. These applications contain the authentication process to let users access data securely. An example of a Centralized database can be Central Library that carries a central database of each library in a college/university.

- ### USE CASES OF CENTRALIZED DATABASE
- Centralized database storage improves data safeguarding. 
- Centralized database provides physical security as locally stored data signifies an ongoing physical security hazard.
- Maintenance of centralized storage is less costly than multiple storage spaces.
- Easy to share ideas across the market analysts.
- It reduces conflicts due to centralization
- Centralized database reduces conflicts amongst organizations and they can focus on their vision and promptly act.
- In centralized database, the data redundancy is negligible.

### Cloud database
A cloud database is one that runs over the Internet. The data is stored on a local hard drive or server, but the information is available online. This makes it easy to access your files from anywhere, as long as you have an Internet connection. To use a cloud database, users can either build one themselves or pay for a service to store their data for them. Encryption is an essential part of any cloud database, as all information needs to be protected as it is transmitted online.

A cloud database is a database service built and accessed through a cloud platform. It serves many of the same functions as a traditional database with the added flexibility of cloud computing. Users install software on a cloud infrastructure to implement the database.

Key features:

- A database service built and accessed through a cloud platform
- Enables enterprise users to host databases without buying dedicated hardware
- Can be managed by the user or offered as a service and managed by a provider
- Can support relational databases (including MySQL and PostgreSQL) and NoSQL databases (including MongoDB and Apache CouchDB)
- Accessed through a web interface or vendor-provided API

- ### USE CASES OF CLOUD DATABASE
Hosting Static Web Sites and Complex Web Applications. 
Software Development Life Cycle Support. 
Training. 
Demos. 
Data Storage. ...
Disaster Recovery and Business Continuity. 
Media Processing and Rendering. 
Business and Scientific Data Processing.

### Commercial database
A commercial database is any that is designed by a commercial business. Businesses develop feature-rich databases, which they then sell to their customers. Commercial databases can vary in terms of composition or the technology they use. The defining trait of commercial databases is having users pay to use them, unlike open source databases.

Also referred to as column data stores, columnar databases store data in columns rather than rows. These types of databases are often used in data warehouses because they’re great at handling analytical queries. When you’re querying a columnar database, it essentially ignores all of the data that doesn’t apply to the query, because you can retrieve the information from only the columns you want.

Examples: Google BigQuery, Cassandra, HBase, MariaDB, Azure SQL Data Warehouse

- ### USE CASES OF COMERCIAL DATABASE
- Customer Relationship Management
A customer relationship management (CRM) database can help a small business manage the lifeblood of its business – its customers. A CRM database organizes all the information a company has about its accounts, contacts, leads and opportunities. A single customer's record may include his contact details, the date and amount of his last order, the total amount of his purchases for the last year, a list of his favorite products and the products he returned, details of customer service calls and more. Databases can also be used to manage marketing and promotions, to export email addresses and to prepare shipping labels.

- Inventory Tracking Database
An inventory tracking database can tell a retail business how much inventory is in a warehouse, in a storage room and on store shelves. Integrated bar codes and scanners form a complete tracking system, monitoring products as they move from one place to another and updating the database so you never need to count the inventory in a warehouse. A database can also alert you when products and supplies are running short so you can order more before you run out of an essential item.

- Payroll and Scheduling Database
Using a database to manage employee information can simplify scheduling and help prevent payroll errors. An employee database contains such fields as hourly wage, salary or commission, tax withholding rates, year-to-date income and accrued vacation time. Other employee benefits, such as health insurance and retirement account contributions, can also be recorded in a database. Two or more databases can be linked to each other to create an association between a sales representative in the personnel database and the accounts she is responsible for in the CRM database.

- Business Data Analysis
The robust reporting features of databases make them useful resources for analyzing data and predicting future trends. For example, a productivity report might show that productivity slows so much on the Friday afternoons before a three-day holiday weekend that you may as well just let the staff go early on those days. A sales promotion effectiveness report might show that sales of certain products increased after an email promotion while sales of other products increased after an in-store promotion. Customer behavior is predictable, and a database can help you anticipate and fulfill your customers' needs.

### Distributed database
A distributed database is one that is spread out over multiple devices. Rather than having all information stored on a single device, like other databases on this list, distributed databases will operate across multiple machines, such as different computers within the same location or across a network. The benefits of a distributed database include increased speed, better reliability and ease of expansion.

The distributed database, in contrast to the centralized database notion, includes contributions from the common database as well as information recorded by local computers. The data is dispersed throughout an organization and is not kept in a single location. These sites are linked together through communication links, making it easier for them to access the spread data.

A distributed database is one in which distinct parts of a database are stored in numerous locations (physical), as well as application procedures that are replicated and spread among different points in a network.


Homogeneous and heterogeneous distributed databases are the two types of distributed databases. 
Homogeneous DDB: Those database systems which execute on the same operating system and use the same application process and carry the same hardware devices.Homogeneous DDBs, for example, all physical locations in a DDB, have the same underlying hardware and run on the same operating systems and application procedures.


Heterogeneous DDB: Those database systems which execute on different operating systems under different application procedures, and carries different hardware devices. Whereas, the operating systems, underlying hardware as well as application procedures can be different at various sites of a DDB which is known as heterogeneous DDB.


- #### USE CASES OF DISTRIBUTED DATABASE 
Instead of limiting data storage and transaction processing to one machine, distributed database utilizes multiple machines across different locations. This, in turn, increases performance, data recovery, and general user experience.


### End-user database
End-user is a term used in product development that refers to the person who uses the product. An end-user database is, therefore, a database that is primarily used by a single person. A good example of this type of database is a spreadsheet stored on your local computer.

The end user is usually not concerned about the transaction or operations done at various levels and is only aware of the product which may be a software or an application. Therefore, this is a shared database which is specifically designed for the end user, just like different levels’ managers. Summary of whole information is collected in this database.

Examples of such software could include, word processors, spreadsheet managers etc. Any database software which allows the end user to create and manage data comes under this category.

### Graph database
Graph databases are databases that focus equally on the data and the connections between them. In this database, data is not constricted to predefined models. Most other databases can find connections between data when you run a search. With a graph database, these connections are stored inside the database right alongside the original data. This makes for a more efficient and faster database when your primary goal is to manage the connections between your data.

Graph databases are a type of NoSQL database that are based on graph theory. Graph-Oriented Database Management Systems (DBMS) software is designed to identify and work with the connections between data points. Therefore graph databases are often used to analyze the relationships between heterogeneous data points, such as in fraud prevention or for mining data about customers from social media.

On the plus side, graph databases have advanced features for relationship querying, traversing, and tracking, are optimized for querying related data, and they avoid row locking. As for the negatives, graph databases have a large ramp up time for developers, high overhead for simple use cases, lack of standardization, poor performance of aggregate queries, and devs typically need to learn a custom query language.

Examples: Datastax Enterprise Graph, Neo4J


- #### USE CASES OF GRAPH DATABASE 
Great for analysis of heterogeneous data points, fraud prevention, advanced enterprise operations, social networking, payment systems, and GeoSpatial routing/visualization.

 

### NoSQL database
A NoSQL database has a hierarchy similar to a file folder system and the data within it is unstructured, or non-relational. This lack of structure allows them to process larger amounts of data at speed and makes it easier to expand in the future. Cloud computing regularly makes use of NoSQL databases. It is a data storage and retrieval system. It is also known as a non-SQL or non-relational database since it accesses and manages data using a range of data models. NoSQL databases are utilized in real-time web applications and for large amounts of data. They may also support SQL-like queries. That is why it is also known as Not simply SQL. 


NoSQL is a broad category that includes any database that doesn’t use SQL as its primary data access language.  Unlike in relational databases, data in a NoSQL database doesn’t have to conform to a pre-defined schema, so these types of databases are great for organizations seeking to store unstructured or semi-structured data. One advantage of NoSQL databases is that developers can make changes to the database on the fly, without affecting applications that are using the database.

Examples: Apache Cassandra, MongoDB, CouchDB, and CouchBase

- #### USE CASES OF NOSQL DATABASE 
Mobile, online, and gaming applications benefit greatly from NoSQL databases. Because it has qualities that are compatible with current applications. Flexibility, scalability, great performance, and extremely useful APIs are among the benefits.

Other important use cases are:

1. Real-time/Near Real-time Big Data Processing
The faster a company can process and act on fresh data, the greater its operational efficiency and business agility, and the greater the bottom-line value of its data. A typical approach to real-time big data processing uses stream processing to ingest new data combined with Apache Hadoop for analyzing historical data, plus a NoSQL database that integrates with both. 

2. Internet of Things
As of 2021, it’s estimated that about 46 billion IoT devices, from smartphones to home appliances to healthcare systems to factory sensors to smart vehicles, are now connected to the Internet. The amount of semi-structured data these devices continuously generate adds up to something like 847 zettabytes. NoSQL databases are better suited than their relational counterparts to scale out to ingest this endless fire hose of diverse data.

3. Content Management
Online shopping now surpasses brick-and-mortar sales, and “content is king” across thousands of online marketplaces and web storefronts. Online sales leaders curate a selection of multimedia content (including user-generated and social media content like reviews, photos and videos) and deliver it to shoppers “at the moment of interaction.” 

NoSQL document databases offer a flexible, open-ended data model that is ideal for storing a mix of structured, semi-structured and/or unstructured content. NoSQL also makes it possible to aggregate data that serves multiple business applications within a single catalog database. Whereas RDBMS with its fixed data models tend to result in the proliferation of multiple, overlapping catalogs for different purposes.  

4. Mobile Apps With Huge Numbers Of Users
Mobile phone and tablet use recently surpassed desktops as the top online platform for searching, shopping and otherwise viewing web content. Interestingly, as much of 90% of mobile data is served via apps and only 10% through browsers, an overwhelming shift in recent years.

Rapidly scaling mobile apps globally to serve tens of millions of users with acceptable performance (think mobile gaming or popular social media apps) often calls for distributed databases, which in turn calls for NoSQL. Flexible NoSQL data models also support rapid app update cycles better than relational data models in many cases. 


### Object-oriented database
Object-oriented databases are ones in which data is represented as objects and classes. An object is an item, such as a name or phone number, while a class is a group of objects. Object-oriented databases are a type of relational database. Consider using an object-oriented database when you have a large amount of complex data that you want to process quickly.

In Object-oriented Model, data is stored in the form of objects. The structure which is called classes which display data within it. It is one of the components of DBMS that defines a database as a collection of objects which stores both data members values and operations.

Some object-oriented databases are designed to work well with object-oriented programming languages such as Delphi, Ruby, Python, JavaScript, Perl, Java, C#, Visual Basic .NET, C++, Objective-C and Smalltalk; others such as JADE have their own programming languages. OODBMSs use exactly the same model as object-oriented programming languages.

### USE CASES OF OBJECT ORIENTED DATABASE

Object databases based on persistent programming acquired a niche in application areas such as engineering and spatial databases, telecommunications, and scientific areas such as high energy physics and molecular biology. Another group of object databases focuses on embedded use in devices, packaged software, and real-time systems.

Many object databases, for example Gemstone or VOSS, offer support for versioning. An object can be viewed as the set of all its versions. Also, object versions can be treated as objects in their own right. Some object databases also provide systematic support for triggers and constraints which are the basis of active databases.


### Open-source database
An open-source database is designed for the public to use for free. Unlike commercial databases, users can download or sign up for open source databases without paying a fee. The term "open source" refers to a program in which users can see how it was written and constructed and are free to make their own changes to the program. Open-source databases are typically much cheaper than commercial databases, but they can also lack some of the more advanced features found in commercial databases.

Open source databases store vital information in software which the organization can control. An open source database allows users to create a system based on their unique requirements and business needs. It is free and can also be shared. The source code can be modified to match any user preference.

Open source databases address the need to analyze data from a growing number of new applications at lower cost. The deluge of social media and the Internet of Things (IoT) has ushered an age of massive data that needs to be collected and analyzed. The data only has value if an enterprise can analyze it to find useful patterns or real-time insights. But the data contains vast amounts of information that can overload a traditional database. The flexibility and cost-effectiveness of open source database software has revolutionized database management systems.

Examples of open source databases include MySQL, PostgreSQL and MongoDB.

The most common open source databases include:

Key-value databases — Store key and value data in memory for speedy lookup.
Document databases — Store document information.
Wide-column store databases — Similar to key-value with a large number of columns. They are well suited for analyzing huge data sets.

### USE CASES OF OPEN SOURCE DATABASE

An open source database is used in analytics to review vast amounts of data so enterprises can better determine business goals. Open source data software is now common in enterprise IT departments in many industries. The best open source database examples include companies such as:

Ford Motor Company — Gathering 25 gigabytes of data per hour per car for its Smart Mobility initiative.
Macy’s — Using open source data technology to reach customers with advertising campaigns targeted to their specific tastes and needs.
Progressive Insurance — Analyzing more than 15 billion miles of driving data with its Snapshot program to give safer drivers discounts.  
Netflix — Runs its own Open Source Software Center as a user and contributor to open source databases for knowing which content customers will prefer.


### Operational database
The purpose of an operational database is to allow users to modify data in real time. Operational databases are critical in business analytics and data warehousing. They can be set up either as relational databases or NoSQL, depending on needs. Conventional databases rely on batch processing, where commands are carried out in groups. Operational databases, on the other hand, allow you to add, edit and remove data at any moment.

Information related to operations of an enterprise is stored inside this database. Functional lines like marketing, employee relations, customer service etc. require such kind of databases.

### USE CASES OF OPERATIONAL DATABASE

- #### Customer 360
- Address the far-reaching effects of the shift in consumer expectations by enabling a holistic view of your business and your customers, from all products, systems, devices, and interaction channels
- Deliver a consistent, personalized, context specific, and relevant experience
- Build churn prediction models to identify at-risk customers and proactively target them with retention programs
- #### Content Depot
- Ensure that all users can access data because of high concurrency and low latency
- Build data-based applications that distribute custom, easy-to-digest information across your organization
- #### Time-series
- Include real-time data and analysis into decision points across your organization
- #### Customer-facing applications
- Enable serving analytics on mobile and web applications directly to end-customers
- Use as a key-value store for applications
- #### Operationalize model scoring and serving
- Build and score models on operational data for prevention, optimization, prescription, and prediction
- Increase conversion rate of cross-sell and upsell opportunities
- Predict credit-worthiness and lifetime customer value
- #### Fraud and threat management
- Perform fraud model serving and detection
- #### IoT - Operation and monetization
- Leverage IoT to evolve or change your business model and operations for greater efficiencies
- Provide an up-to-the-minute picture of the status of the fleet through real-time monitoring, alerting, and diagnosis
- Deliver economic value by enabling new business models
- Increase conversion rate of cross-sell and upsell opportunities
- #### Operational excellence
- Achieve operational excellence by reducing the total cost if ownership (TCO), improving efficiency, and eliminating threats
- Decrease network downtime using predictive maintenance enabled by active collection and monitoring of network data
- Optimize equipment performance and costs using real-time IoT analytics

### Personal database
A personal database is one that is designed for a single person. It is typically stored on a personal computer and has a very simple design, consisting of only a few tables. Personal databases are not typically suitable for complex operations, large amounts of data or business operations.

Data is collected and stored on personal computers which is small and easily manageable. The data is generally used by the same department of an organization and is accessed by a small group of people.

### USE CASES OF PERSONAL DATABASE
A personal database is used to store frequently used, unique, or customized information. This provides faster access to targeted information for use across all studies and projects. Personal databases are a quick and convenient method of accessing frequently used material information in any project or study

### Relational database
A relational database is a collection of data organized into a table structure. Within the table structure, the rows are called “records” or “tuples” and the columns are called “attributes.” The structure allows users to identify and access data in relation to another piece of data in the table, or other tables within the database. Tables can be modified, or rows and columns can be added or removed without affecting the rest of the database.

Relational databases are the other major type of database, opposite of NoSQL. With a relational database, information is stored structured about other data. A good representation of a relational database would be the connection between a person shopping online and their shopping cart. Relational databases are often preferred when you are concerned about the integrity of your data, or when you're not particularly focused on scalability.

Structured Query Language (SQL) is the most common language for reading, creating, updating and deleting data. Relational databases are very reliable. They are compliant with ACID (Atomicity, Consistency, Isolation, Durability), which is a standard set of properties for reliable database transactions. Relational databases work well with structured data. Organizations that have a lot of unstructured or semi-structured data should not be considering a relational database.

Relational databases are the most popular and widely used databases. Some of the popular DDBMS are Oracle, SQL Server, MySQL, SQLite, PostgreSQL and IBM DB2.
Oracle: Oracle Database is commonly referred to as Oracle RDBMS or simply as Oracle. It is a multi-model database management system produced and marketed by Oracle Corporation.
MySQL: MySQL is an open-source relational database management system (RDBMS) based on Structured Query Language (SQL). MySQL runs on virtually all platforms, including Linux, UNIX, and Windows.
Microsoft SQL Server: Microsoft SQL Server is an RDBMS that supports a wide variety of transaction processing, business intelligence, and analytics applications in corporate IT environments.
PostgreSQL: PostgreSQL, often simply Postgres, is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards compliance.
DB2: DB2 is an RDBMS designed to store, analyze, and retrieve data efficiently.
 

- #### USE CASES OF RELATIONAL DATABASE 
The relational database and relational DBMS have been at the core of most mission-critical business and government transactions for decades. Looking ahead, they will continue to evolve in their capabilities and be a critical component for services leveraging modern technologies, such as AI, cognitive, big data, predictive analytics and more. While graphs, cubes, tensors and MapReduce are capturing much of today’s mindshare, tomorrow’s hottest applications will still be built on the back of tried and true SQL. 

As enterprise architects and data scientists embrace newer data architectures, they will want to retain investments in the relational DBMS for reasons such as:

- Performance. The performance of relational databases has been perfected to support the world’s most demanding data-centric services, including modern capabilities like caching and in-memory techniques.
-  Reliability. With a long history of successfully supporting the world’s largest governments and businesses, the relational database has proven to be trustworthy and reliable.
- Integration. Relational databases have supported countless transactions since the 1980’s, meaning virtually every system within a government or enterprise is already integrated with the technology. 
- Security. Today’s relational databases perform like security veterans, having matured over the 30 years that they have been protecting the world’s most sensitive data.

There are also more several important use cases for relational databases; situations where data integrity is absolutely paramount (financial applications, defense and security, private health information), highly structured data, and automation of internal processes.













