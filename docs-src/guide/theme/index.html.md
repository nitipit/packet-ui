# Theme Framework

**Packet UI** let you customize CSS style through **Theme Framework** which is written
in **SASS** languange

> Read more about SASS lang at [](https://sass-lang.com/)

## Create and build your own `packet-ui.scss`
---

Learning how to build your own `packet-ui.scss` is a good starting point so you can try modifying it and see what happen to your user interface.

Let's take a look at directory: `node_modules/packet-ui/src/`

```
// $ tree src -L 1 -F --dirsfirst -v
src
├── font/
├── ui/
├── _break-point.scss
├── _constant.scss
├── _function.scss
├── _mixin.scss
├── _theme-default.scss
├── _theme.scss
├── class.scss
├── packet-ui.js
├── packet-ui.scss
├── typography.scss
├── ui.js
└── ui.scss
```

In this directory, `packet-ui.scss` is the main **SASS** which generates all CSS style. To make your own, just copy `packet-ui.scss` file to somewhere else in your project and run:

```
$ npx sass packet-ui.scss your_destination_directory/packet-ui.css
```

Then, include `your_destination/packet-ui.css` in your **HTML**

```html
<link rel="stylesheet" href="your_destination/packet-ui.css">
```

## Theme customization in `packet-ui.scss`
---

`packet-ui.scss` contains 4 main parts:
1. Theme variables : `_theme.scss`
2. CSS classes for general use : `class.scss`
3. Typography : `typography.scss`
4. User Interface styles : `ui.scss`


```
// file: packet-ui.scss

// Theme variables
@use '_theme.scss';

// CSS classes for general use
@use 'class.scss' with (
    $-color: theme.$color,
    $-pallete: theme.$pallete,
    $-ui: theme.$ui,
);

// Typography
@use 'typography.scss' with (
    $-font-responsive: theme.$font-responsive,
    $-text-font-size: theme.$text-font-size,
    $-ui: () theme.$ui,
);


// User Interface styles
@use 'ui.scss' with (
    $-pallete: theme.$pallete,
    $-ui: theme.$ui,
);
```

Just modify `_theme.scss` and build `packet-ui.scss` again to use your own theme.