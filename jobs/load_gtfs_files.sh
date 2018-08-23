#!/usr/bin/env bash
find data -type f | grep -h ".zip" | sudo xargs -I {} bash -c 'docker cp {} navitia_tyr_worker_1:/srv/ed/input/tpp/'