# ES6 Modules

Javascript build/bundler tools is required to use ES6 **export & import** in browser, 
We recommend using [Parcel](https://v2.parceljs.org/)


```
// Javascript file : index.js
import * as ui from 'packet-ui';

// Define ui.InputNumber component to custom element.
customElements.define('ui-input-number', ui.InputNumber);
```
```
// SASS file : index.scss
@use '/path/to/ui/ui.scss';

ui-input-number {
    @include ui.input-number(red);
}
```

Build Javascript and SASS with Parcel
```
$ npx parcel build 'index.js' 'index.scss'
```

Use built Javascript and CSS in your HTML
```
<!-- HTML -->
<script defer src="./dist/index.js"></script>
<link rel="stylesheet" href="./dist/index.css">

<ui-input-number></ui-input-number>
```

<ui-input-number></ui-input-number>