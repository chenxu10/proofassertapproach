# Scaling from 0 to 1 Million Users - Try to draw a diagram to scale your app containing load balancer and database with replicas

## System Architecture Diagram

```
                                    Internet
                                       |
                              Load Balancer (L7)
                                 /    |    \
                                /     |     \
                         App Server App Server App Server
                            1         2         3
                            |         |         |
                            \         |         /
                             \        |        /
                              \       |       /
                               \      |      /
                                \     |     /
                                 \    |    /
                                  \   |   /
                                   \  |  /
                                    \ | /
                               Master Database
                                     |
                      +-------------+-------------+
                      |                           |
                 Read Replica 1            Read Replica 2
```