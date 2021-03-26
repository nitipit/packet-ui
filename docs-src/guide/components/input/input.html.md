# Input

## Text, Email, Password, etc.
---
<div>
    <input type="text" placeholder="Text">
    <input type="email" placeholder="Email">
    <input type="password" placeholder="Password">
</div>

```html
<input type="text" placeholder="Text">
<input type="email" placeholder="Email">
<input type="password" placeholder="Password">
```

## Number Input
---
<pkt-input-number>
    <input type="number" max="1000" min="0">
</pkt-input-number>

```html
<pkt-input-number></pkt-input-number>

<!-- Customized input -->
<pkt-input-number>
    <input type="number" max="1000" min="0">
</pkt-input-number>
```

## Radio Input
---
<div>
    <pkt-input-radio>
        <input type="radio" name="gender" value="m">
    </pkt-input-radio>
    <span>Male</span>
    <pkt-input-radio>
        <input type="radio" name="gender" value="f">
    </pkt-input-radio>
    <span>Female</span>
</div>

<div class="pkt-button-group" style="margin-top: 2rem;">
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="left">
        <button>Left</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Center</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Right</button>
    </pkt-input-radio-btn>
</div>


```html
<pkt-input-radio>
    <input type="radio" name="gender" value="m">
</pkt-input-radio>
<span>Male</span>
<pkt-input-radio>
    <input type="radio" name="gender" value="f">
</pkt-input-radio>
<span>Female</span>
```

```html
<pkt-button-group>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="left">
        <button>Left</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Center</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Right</button>
    </pkt-input-radio-btn>
</pkt-button-group>
```

## Range Input
---

<div style="display: flex; justify-content: center;">
    <input type="range" style="min-width: 200px; width: 50%;
        margin-top: 3rem; margin-bottom: 2rem;">
</div>

### Usage

```html
<input type="range">
```

### SCSS

```scss
@use 'sass:color';
@use 'path/to/_ui.scss';

input[type="range"] {
    @include ui.slider(
        $thumb-color: color.adjust(white, $lightness: -10%),
        $thumb-color-active: orange,
        $thumb-width: 1.2em,
        $thumb-height: 1.2em,
        $thumb-border: 1px solid,
        $thumb-border-radius: 50%,
        $bar-color: color.adjust(white, $lightness: -20%),
        $bar-height: 0.25em
    )
}
```

## Tag Input
---
<div style="margin-top: 2rem;">
    <pkt-input-tag></bitsinput-tag>
</div>

### Usage

```html
<pkt-input-tag></pkt-input-tag>
```

### API
|API|Description|
|---|---|
|`add_tag(value)`|Add `value` as a tag|
|`tags`|Get tag list from input|
