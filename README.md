
Guetzli is a Google program to optimize JPEG images. Unfortunately, it only works one file at a time. With this script in Python you can do it recursively a whole folder.

# Install 

Guetzli must be installed on your system. Follow the official instructions.
[Guetzli](https://github.com/google/guetzli)

and Python 3.

# Use

```bash
python3 guetzli-recursively.py [folder]
```

## Example

```bash
python3 guetzli-recursively.py img
```

out

```bash
img/tasks.jpg
Save 6%
img/portfolio/idecrea/space.jpg
It is not necessary to optimize
img/portfolio/home.jpg
Save 3%
```
