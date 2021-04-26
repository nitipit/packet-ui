# Theme Framework

**Packet UI** let you customize CSS style through **Theme Framework** which is written
in **SASS** languange

> Read more about SASS lang at [](https://sass-lang.com/)

You can make a customized theme by creating 2 files as follow
1. `_theme.scss` : This is the theme configuration file. You can modify this file
   to change theme.
2. `packet-ui.scss` : **SASS** file to build theme CSS.

```scss
// file: _theme.scss
@forward 'node_modules/packet-ui/src/_theme.scss' with (
    $-color: (
        red: #F44336,
        pink: #E91E63,
        purple: #9C27B0,
        deep-purple: #673AB7,
        indigo: #3F51B5,
        blue: #2196F3,
        light-blue: #03A9F4,
        cyan: #00BCD4,
        teal: #009688,
        green: #4CAF50,
        light-green: #8BC34A,
        lime: #CDDC39,
        yellow: #FFEB3B,
        amber: #FFC107,
        orange: #FF9800,
        deep-orange: #FF5722,
        brown: #795548,
        grey: #9E9E9E,
        blue-grey: #607D8B,
        blue-gray: #607D8B,
    ),
    $pallete: (
        primary: #FFC107,
        saturate: 0%,
        hue-distance: 30,
    ),
    $font-responsive: (
        vw-min: 320px,
        vw-max: 1200px,
        font-size-min: 16px,
        font-size-max: 18px,
        line-height: 1.7,
    ),
    $text-font-size: (
        h1: 2rem,
        h2: 1.5rem,
        h3: 1.17rem,
        h4: 1rem,
        h5: 0.83rem,
        h6: 0.67rem,
        p: 1rem,
    ),
    $ui: (
        ui-color: #FFC107,
        border-radius: 4px,
        font-family: Cantarell,
    ),
);
```

```scss
// file: packet-ui.scss
@use '_theme.csss';

@use 'node_modules/packet-ui/src/typography.scss' with (
    $-font-responsive: theme.$font-responsive,
    $-text-font-size: theme.$text-font-size,
    $-ui: theme.$ui,
);

@use 'node_modules/packet-ui/src/ui.scss' with (
    $-pallete: theme.$pallete,
    $-ui: theme.$ui,
);

@use 'node_modules/packet-ui/src/class.scss' with (
    $-color: theme.$color,
    $-pallete: theme.$pallete,
    $-ui: theme.$ui,
);
```

To build `packet-ui.css`, run
```
$ npx sass packet-ui.scss packet-ui.css
```

## Theme configuration file explanation `_theme.scss`
---



### Color set

Color set are pre-defined colors with name, such as:
red, blue, green, yellow, pink, brown, white, green, etc. **Packet UI** use
19 color from Material Design.

```scss
@use 'path-to/src/_theme.scss' with (
    $color: (
        red: #F44336,
        pink: #E91E63,
        purple: #9C27B0,
        // ... + 16 more colors
    )
)
```

You can defined color name as much as you want and Theme Framework will generated
color and background CSS class for all the colors defined.

```html
    <!-- text color: blue, background color: amber -->
    <div class="blue bg-amber"><div>
    <button class="blue bg-int-amber"></div>
```

### Pallete

Pallete are color variations/harmony for the defined primary color. The framework
will generate 3 harmony : monochrome  primary/complmentary and analog.

> [Material Design: Color System](https://material.io/design/color/the-color-system.html)
> could be a good place to read and understand about color system and design.

### UI style

