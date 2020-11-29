3 word lowercase words:

```bash
cat /usr/share/dict/words | grep -e "^[[:lower:]][[:lower:]][[:lower:]]" > src/squabble/data/dict.txt
```

Python setup:

```bash
conda create --name=squabble python=3.8
conda activate squabble
poetry install
```

Database:

```bash
conda install postgresql  # Optional

initdb -D postgres/squabble
pg_ctl -D postgres/squabble -l postgres/squabble.db.log start

createuser --encrypted --pwprompt squabble
createdb --owner=squabble squabble

psql squabble < src/squabble/sql/tables.sql
```
