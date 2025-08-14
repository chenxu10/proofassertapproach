# Can you calculate QPS and peak QPS for this exchange system?

1 million user 
20 requests per day
1m * 20 / (3600 *24) = 700req/s

Latency:
<200ms

Storage:
1m * 5mb = 5TB
read/write ratio = 9:1
bandwideth = 50kb * 700 = 35mb/s assume each request 50kb