# Rio Bootstrap 🌊👢

Makes the fabulous icons from Bootstrap available in to [Rio](https://rio.dev).

You can browse all icons [on the Bootstrap
website](https://icons.getbootstrap.com/). The names in Rio are the same, except
using underscores instead of dashes.

## Installation 🛠️

`rio-bootstrap` is available on [PyPI](https://pypi.org/project/rio-jobs/):

```sh
python -m pip install rio-jobs
```

## Quickstart 🚀

To use the icons in your project just import this module, then use the icons as
you'd use any other icon in Rio:

```py
import rio
import rio_bootstrap  # Import the module. This registers the icons with Rio.


class MyRoot(rio.Component):
    def build(self) -> rio.Component:
        return rio.Icon(
            "bootstrap/wifi",  # All icons are available as "bootstrap/<name>"
            fill=rio.Color.BLUE,
            min_width=5,
            min_height=5,
            align_x=0.5,
            align_y=0.5,
        )


app = rio.App(
    build=MyRoot,
)
```

The icons will also show up in the Rio dev-tools, so you can easily browse them.

## License ⚖️

The Python code in this project is available under the permissive **MIT
license**. The icons themselves are not part of this repository. Check [the
Bootsrap icons repo](https://github.com/twbs/icons) for licensing information.
