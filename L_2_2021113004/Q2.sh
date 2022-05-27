#!/bin/bash
find ./ -type f -name "*.txt" -exec grep 'Linux'  {} \;| wc -l


