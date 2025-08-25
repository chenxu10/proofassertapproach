Minimize stateful components because it can become into a bad stateful.

Instead of having all five services writting to the same table, having one service
talk to database knowing about state and five other services talk to that state