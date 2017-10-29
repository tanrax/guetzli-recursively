
Guetzli is a Google program to optimize JPEG images. Unfortunately, it only works one file at a time. With this script in Python you can do it recursively a whole folder.

**UPDATE** [GUI for Mac OS](https://github.com/tanrax/guetzli-recursively-gui)

# Install 

Guetzli must be installed on your system. Follow the official instructions.
[Guetzli](https://github.com/google/guetzli)

and 2.7.10 or Python 3.

After

```bash
pip3 install guetzli-recursively
```

# Use

```bash
guetzli_recursively [folder]
```

## Example

```bash
guetzli_recursively img/
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
