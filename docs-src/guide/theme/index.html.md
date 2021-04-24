# Theme Design

This guide will show how to transfrom your design into CSS.

> [Material Design: Color System](https://material.io/design/color/the-color-system.html)
> could be a good place to read and understand about color system and design.

Firstly, let's take a look about how to use **Theme Framework** with **SASS**

```scss
@use 'path-to/src/_theme.scss' with (
    $color: (),
    $pallete: (),
    $ui: (),
);
```

## Color set
---
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

## Pallete
---
Pallete are color variations/harmony for the defined primary color. The framework
will generate 3 harmony : monochrome  primary/complmentary and analog.

## UI style
---
