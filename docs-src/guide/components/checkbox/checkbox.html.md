# Checkbox

## Preview
---
<div data-is="ui" class="flex">
    <pkt-checkbox class="size-1 color-c">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-2 color-c2">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-3 color-p1">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-4 color-p">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-3 color-p2">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-2 color-c1">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-1 color-c">
        <input type="checkbox" checked>
    </pkt-checkbox>
</div>

## Usage
---

```html
<pkt-checkbox></pkt-checkbox>
<pkt-checkbox>
    <input type="checkbox" checked>
</pkt-checkbox>
```

## SCSS

```scss
@use 'path/to/_ui.scss';

pkt-checkbox {
    @include ui.checkbox(
        $bg-color: grey, // Inactive background color
        $color-active: orange) // Active & Hover color
    }
}
```

|Argument|Description|Example Value|
|---|---|---|
|`$bg-color`|inactive background color|`grey` `#AAA`|
|`$color-active`|background color for **active** and **hover** state|`orange`|
