#!bin/bash
find. -type f -name "*" ! -name "READ.md" -exec chmod u+x {} +
