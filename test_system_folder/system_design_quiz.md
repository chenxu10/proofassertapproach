# System Design Interview Quiz: Scale from Zero to Millions of Users

## Instructions
This quiz contains 30 multiple choice questions designed to test your deep understanding of system design concepts from scaling a system from zero to millions of users. Choose the best answer for each question.

---

## Questions

### 1. What is the primary reason companies adopt system design interviews?
A) To test coding skills in specific programming languages
B) To evaluate communication and problem-solving skills similar to daily work
C) To assess knowledge of specific frameworks and tools
D) To measure memorization of design patterns

**Answer: B**

---

### 2. In a single server setup, what is the correct order of the request flow?
A) DNS → IP address → HTTP request → HTML/JSON response
B) HTTP request → DNS → IP address → HTML/JSON response
C) IP address → DNS → HTTP request → HTML/JSON response
D) HTML/JSON response → HTTP request → DNS → IP address

**Answer: A**

---

### 3. Which of the following is NOT a category of NoSQL databases?
A) Key-value stores
B) Graph stores
C) Relational stores
D) Document stores

**Answer: C**

---

### 4. When should you consider using NoSQL databases over relational databases?
A) When you need complex join operations
B) When you need ACID compliance
C) When you need to store massive amounts of unstructured data
D) When you have a small dataset with complex relationships

**Answer: C**

---

### 5. What is the main limitation of vertical scaling?
A) It's too expensive initially
B) It has a hard limit and no failover capability
C) It requires more programming effort
D) It only works with specific databases

**Answer: B**

---

### 6. What is the primary benefit of using a load balancer?
A) It increases database performance
B) It provides better security through encryption
C) It distributes traffic evenly and provides failover capability
D) It reduces the cost of servers

**Answer: C**

---

### 7. In a load balancer setup, why are private IPs used for communication between servers?
A) Private IPs are faster than public IPs
B) Private IPs are cheaper to use
C) For better security - they're only reachable within the same network
D) Private IPs support more concurrent connections

**Answer: C**

---

### 8. In database replication, what operations does a master database typically handle?
A) Only read operations
B) Only write operations (insert, delete, update)
C) Both read and write operations equally
D) Only backup operations

**Answer: B**

---

### 9. What happens when a master database goes offline in a master-slave replication setup?
A) The system shuts down completely
B) All operations are queued until the master returns
C) A slave database is promoted to be the new master
D) Read operations continue but write operations are permanently lost

**Answer: C**

---

### 10. What is the primary purpose of a cache in system design?
A) To permanently store user data
B) To store frequently accessed data in memory for faster retrieval
C) To backup database information
D) To encrypt sensitive information

**Answer: B**

---

### 11. What caching strategy is described when a web server checks the cache first, and if data isn't found, queries the database and stores the response in cache?
A) Write-through cache
B) Write-behind cache
C) Read-through cache
D) Cache-aside

**Answer: C**

---

### 12. Which cache eviction policy removes the least recently used items when the cache is full?
A) FIFO (First In First Out)
B) LFU (Least Frequently Used)
C) LRU (Least Recently Used)
D) Random eviction

**Answer: C**

---

### 13. What does CDN stand for and what is its primary purpose?
A) Content Delivery Network - to deliver static content from geographically dispersed servers
B) Central Data Node - to centralize all data storage
C) Cache Distribution Network - to distribute cache servers
D) Content Database Network - to replicate databases globally

**Answer: A**

---

### 14. What is TTL in the context of CDN?
A) Total Transfer Limit
B) Time-to-Live - describes how long content is cached
C) Traffic Transfer Log
D) Temporary Transfer Location

**Answer: B**

---

### 15. What is the main difference between stateful and stateless servers?
A) Stateful servers are faster than stateless servers
B) Stateless servers can only handle read operations
C) Stateful servers remember client data between requests, stateless servers don't
D) Stateless servers require more memory than stateful servers

**Answer: C**

---

### 16. Why is a stateless web tier preferred for scalability?
A) It uses less memory per server
B) HTTP requests can be sent to any web server, enabling easier auto-scaling
C) It provides better security features
D) It reduces the number of database connections needed

**Answer: B**

---

### 17. What is geoDNS used for in multi-data center setups?
A) To encrypt data transmission between data centers
B) To backup DNS records across multiple locations
C) To resolve domain names to IP addresses based on user location
D) To synchronize databases across data centers

**Answer: C**

---

### 18. What is the main benefit of using message queues in system architecture?
A) They provide faster database access
B) They enable asynchronous communication and decouple system components
C) They reduce memory usage across servers
D) They encrypt messages between services

**Answer: B**

---

### 19. In a message queue system, what are the components that create and consume messages called?
A) Senders and Receivers
B) Writers and Readers
C) Producers/Publishers and Consumers/Subscribers
D) Masters and Slaves

**Answer: C**

---

### 20. Which type of metrics helps understand business performance rather than technical performance?
A) Host level metrics (CPU, Memory, disk I/O)
B) Aggregated level metrics (database tier performance)
C) Key business metrics (daily active users, retention, revenue)
D) Network level metrics (bandwidth, latency)

**Answer: C**

---

### 21. What is database sharding?
A) Creating backup copies of the database
B) Separating large databases into smaller, manageable parts called shards
C) Encrypting database content for security
D) Compressing database files to save space

**Answer: B**

---

### 22. What is the most important factor when choosing a sharding key?
A) The key should be the primary key of the table
B) The key should be as short as possible
C) The key should evenly distribute data across shards
D) The key should be randomly generated

**Answer: C**

---

### 23. What is the "celebrity problem" in database sharding?
A) When celebrity data takes up too much storage space
B) When excessive access to a specific shard causes server overload
C) When celebrities' data gets corrupted during sharding
D) When sharding fails due to privacy regulations

**Answer: B**

---

### 24. Why are join operations challenging in sharded databases?
A) Joins require too much memory
B) Joins are too slow compared to single table queries
C) Data is distributed across multiple servers, making cross-shard joins difficult
D) Sharded databases don't support SQL syntax

**Answer: C**

---

### 25. What technique is commonly used to solve the resharding problem?
A) Database replication
B) Consistent hashing
C) Load balancing
D) Cache invalidation

**Answer: B**

---

### 26. Which of the following is NOT mentioned as a key principle for scaling to millions of users?
A) Keep web tier stateless
B) Cache data as much as possible
C) Use only relational databases
D) Build redundancy at every tier

**Answer: C**

---

### 27. What is the primary reason for moving from a single server to separate web and database servers?
A) To reduce costs
B) To improve security
C) To allow independent scaling of web and data tiers
D) To support more programming languages

**Answer: C**

---

### 28. When should you consider implementing an expiration policy for cached data?
A) Only when using expensive cache servers
B) Always - to prevent cached data from being stored permanently and becoming stale
C) Only for read-heavy applications
D) Never - cached data should persist indefinitely

**Answer: B**

---

### 29. What is the main challenge with maintaining consistency between data store and cache?
A) Cache servers are too slow
B) Data-modifying operations on data store and cache are not in a single transaction
C) Caches don't support the same data types as databases
D) Network latency between cache and database

**Answer: B**

---

### 30. In the evolution from single server to millions of users, which component is typically added LAST in the scaling journey?
A) Load balancer
B) Database replication
C) CDN and caching
D) Database sharding

**Answer: D**

---

## Answer Key

1. B - Communication and problem-solving skills
2. A - DNS → IP → HTTP → Response
3. C - Relational stores (not a NoSQL category)
4. C - Massive unstructured data storage
5. B - Hard limit and no failover
6. C - Traffic distribution and failover
7. C - Better security within network
8. B - Write operations only
9. C - Slave promoted to master
10. B - Faster data retrieval from memory
11. C - Read-through cache
12. C - LRU (Least Recently Used)
13. A - Content Delivery Network for static content
14. B - Time-to-Live for cache duration
15. C - Stateful remembers client data, stateless doesn't
16. B - Any server can handle requests
17. C - Location-based IP resolution
18. B - Asynchronous communication and decoupling
19. C - Producers/Publishers and Consumers/Subscribers
20. C - Business metrics (users, retention, revenue)
21. B - Separating databases into smaller parts
22. C - Even data distribution
23. B - Excessive access causing overload
24. C - Cross-shard joins are difficult
25. B - Consistent hashing
26. C - Use only relational databases
27. C - Independent scaling capability
28. B - Always implement to prevent stale data
29. B - Non-transactional operations
30. D - Database sharding (most complex)

---

## Scoring Guide

- **27-30 correct**: Excellent understanding of system design concepts
- **23-26 correct**: Good grasp with minor gaps
- **18-22 correct**: Adequate understanding, review recommended
- **Below 18**: Significant review needed

## Key Topics for Further Study

If you scored below 80%, focus on these areas:
- Load balancing and failover strategies
- Database replication and sharding concepts
- Caching strategies and CDN implementation
- Stateless vs stateful architecture
- Message queue patterns
- Scaling principles and trade-offs