#! /bin/bash
#car="{\"name\":\"yee\", \"age\":2, \"owner\":\"${1}\"}"
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"ulala\", \"age\":2, \"owner\":\"${1}\"}" http://localhost:5000/POST/car;
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"yee1\", \"age\":2, \"owner\":\"${1}\"}" http://localhost:5000/POST/car;
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"yee2\", \"age\":2, \"owner\":\"${1}\"}" http://localhost:5000/POST/car;
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"yee3\", \"age\":2, \"owner\":\"${1}\"}" http://localhost:5000/POST/car;
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"yee4\", \"age\":2, \"owner\":\"${1}\"}" http://localhost:5000/POST/car;
curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"yee5\", \"age\":2, \"owner\":\"${1}\"}" http://localhost:5000/POST/car;
#echo ${car};
