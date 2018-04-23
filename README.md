## gfw-geometry-ms-load-test
This is a very simplistic repo to try and understand the CPU required by various geometry calculations (and their microservices) when under load.

For more information, check out the various load tests (organized by the date they were performed).

### Running summary

#### 2018-04-19
- Attempt to understand CPU requirements of having a microservice (MS) run a GIS dissolve
- Tested a basic python MS, a shapely unary_union, shapely + dask, and turf.js MS
- All tests run locally on docker, logged with `docker stats`
- Preliminary results suggests that this is inherently a CPU-expensive operation
- Turf.js (an easy to implement alternative for this test) had higher CPU than the python MS
- Suggests that we'll need to scale our API instead of making changes to MS code

#### 2018-04-23
- Attempt to understand current request limitations for the `/dissolve` endpoint of polyIntersect
- Sent 100, 200, 500, 1000, 2000 rps for 5 minutes each
- Requests sent directly to the MS (not the gateway)
- 100 rps hits 74.3% CPU, 200 hits 99%, and slows mean response from 0.1 second to 11 seconds
- Next steps: understand if increasing the size of the gfw-pro machine / pool will help with this process
