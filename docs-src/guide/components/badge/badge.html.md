# Badge

## Preview
---
<div id="preview">
    <div class="size-1">
        <pkt-badge class="bg-p1">1</pkt-badge>
        <pkt-badge class="bg-p">10</pkt-badge>
        <pkt-badge class="bg-p2">100</pkt-badge>
        <pkt-badge class="bg-c1">1000</pkt-badge>
        <pkt-badge class="bg-c">+</pkt-badge>
        <pkt-badge class="bg-c2">-</pkt-badge>
    </div>
    <div class="size-2">
        <pkt-badge class="bg-p1">1</pkt-badge>
        <pkt-badge class="bg-p">10</pkt-badge>
        <pkt-badge class="bg-p2">100</pkt-badge>
        <pkt-badge class="bg-c1">1000</pkt-badge>
        <pkt-badge class="bg-c">+</pkt-badge>
        <pkt-badge class="bg-c2">-</pkt-badge>
    </div>
    <div class="size-3">
        <pkt-badge class="bg-p1">1</pkt-badge>
        <pkt-badge class="bg-p">10</pkt-badge>
        <pkt-badge class="bg-p2">100</pkt-badge>
        <pkt-badge class="bg-c1">1000</pkt-badge>
        <pkt-badge class="bg-c">+</pkt-badge>
        <pkt-badge class="bg-c2">-</pkt-badge>
    </div>
</div>

## Usage
---

`<pkt-badge>` or `class="pkt-badge"`.

```html
<pkt-badge>1</pkt-badge>
<span class="pkt-badge"></span>
```

## Background Color
---
Badge background color can be changed by using packet-ui background color class.

```html
<!-- Example -->
<pkt-badge class="bg-amber">1</pkt-badge>
```

## SCSS
---

```scss
@use 'path/to/_ui.scss';

pkt-badge {
    @include badge($bg-color: red);
}
```