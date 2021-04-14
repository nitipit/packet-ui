# ES6 Modules

To use ES6 **export & import** in browser, Javascript build/bundler tools is needed.  
We recommend using [Parcel](https://v2.parceljs.org/)


```
// Javascript file : index.html.js
import * as ui from 'packet-ui';

// Define ui.InputNumber component to custom element.
customElements.define('ui-input-number', ui.InputNumber);
```
```
// SASS file : index.html.scss
@use '/path/to/ui/ui.scss';

ui-input-number {
    @include ui.input-number(red);
}
```

```
<!-- HTML -->
<script defer src="./index.html.js"></script>
<link rel="stylesheet" href="./index.html.css">

<ui-input-number></ui-input-number>
```

<ui-input-number></ui-input-number>