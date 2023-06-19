#!/bin/bash

cache_ways=("8" "4" "2")
cache_sets=("1024" "2048" "4096")
cache_bytes=("32" "16" "8")

for cache_set in "${cache_sets[@]}"
do
	for cache_way in "${cache_ways[@]}"
	do
		for cache_byte in "${cache_bytes[@]}"
		do
			echo "Running following config: <$cache_set>:<$cache_way>:<$cache_byte>" >> cache_configs_efficiancy_data.txt
			
			spike --dc=$cache_set:$cache_way:$cache_byte --ic=$cache_set:$cache_way:$cache_byte pk matrix_multiply >> cache_configs_efficiancy_data.txt
			
			echo "Completed config: <$cache_set>:<$cache_way>:<$cache_byte>" >> cache_configs_efficiancy_data.txt
		done
	done
done

