# NetBlast

Estimate the blast radius of a network change from structured dependencies.

## Quick start

```python
from netblast.core import blast_radius

print(blast_radius({'router-a': ['switch-b']}, ['router-a']))
```
