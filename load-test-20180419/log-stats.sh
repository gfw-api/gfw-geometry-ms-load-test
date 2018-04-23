while true; do docker stats -a --no-stream | grep geostore >> stats.txt; done
