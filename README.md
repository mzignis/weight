
## Run local postgres db - docker 

### 1. Via terminal
Replace user-name and user-password to correct ones
```bash
docker run  -d \             
-p 5432:5432 \
--name psql-db \
-e PGUSER=user-name \
-e POSTGRES_PASSWORD=user-password \
postgres


```

### 2. Via *.yaml file
#### 2.1 Create yaml file
Replace user-name and user-password to correct ones
```yaml
version: '2'
services:
  psql-db:
    image: postgres
    ports:
      - 5432:5432
    environment:
      - PGUSER=username
      - POSTGRES_PASSWORD=userpassword
```
Run via docker compose (replace filename to proper one)
```bash
docker-compose -f psql.yaml up
```


# Database










CREATE TABLE fruits(id SERIAL PRIMARY KEY, date DATE, weight float);

