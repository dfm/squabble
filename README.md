3 word lowercase words:

```bash
cat /usr/share/dict/words | grep -e "^[[:lower:]][[:lower:]][[:lower:]]" > src/squabble/data/dict.txt
```
