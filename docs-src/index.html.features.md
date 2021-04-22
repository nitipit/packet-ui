## Fast prototype
**Packet UI** provides built-in stylish **User Interface** with **Colors**
and **Theme** to get started and make a user interface prototype.

<pkt-card style="margin-bottom: 2rem;">
    <table style="margin: 0.5rem;">
        <tr>
            <td>badge</td>
            <td>
                <pkt-badge>10</pkt-badge>
            </td>
        </tr>
        <tr>
            <td>checkbox</td>
            <td>
                <pkt-checkbox>
                    <input type="checkbox" name="demo">
                </pkt-checkbox>
            </td>
        </tr>
        <tr>
            <td>button</td>
            <td><button>Submit</button></td>
        </tr>
        <tr>
            <td>switch</td>
            <td>
                <pkt-switch>
                    <input type="checkbox">
                    <div el="label">
                        <span>ON</span>
                        <span>OFF</span>
                    </div>
                </pkt-switch>
            </td>
        </tr>
        <tr>
            <td>input-number</td>
            <td>
                <pkt-input-number>
                    <input type="number" min="0" max="100">
                </pkt-input-number>
            </td>
        </tr>
        <tr>
            <td>dotpulse</td>
            <td>
                <pkt-dotpulse></pkt-dotpulse>
            </td>
        </tr>
    </table>
    <button class="bg-int-a1" style="text-align: center;">
        and much more...
    </button>
</pkt-card>

Built-in UI components are based on <pkt-tag class="bg-blue-grey">&lt;web-components/></pkt-tag>. Just place `<pkt-*>` anywhere in html `<body>`, for examples:

```html
<body>
    <pkt-badge></pkt-badge>
    <pkt-switch></pkt-switch>
</body>
```

## Fast development
Quickly transfrom your design into CSS with **Theme Framewok** written in **SASS**

### Theme color set

There are 19 pre-defined color in CSS class which based on
[Material Design](https://material.io/). 
Just put `class="{color}"` or `class={bg-color}` 
on any element to render color with legible text.

<div class="row">
    <div el="bg-color">
        <pkt-badge class="bg-red">red</pkt-badge>
        <pkt-badge class="bg-pink">pink</pkt-badge>
        <pkt-badge class="bg-purple">purple</pkt-badge>
        <pkt-badge class="bg-deep-purple">deep-purple</pkt-badge>
        <pkt-badge class="bg-indigo">indigo</pkt-badge>
        <pkt-badge class="bg-blue">blue</pkt-badge>
        <pkt-badge class="bg-light-blue">light-blue</pkt-badge>
        <pkt-badge class="bg-cyan">cyan</pkt-badge>
        <pkt-badge class="bg-teal">teal</pkt-badge>
        <pkt-badge class="bg-green">green</pkt-badge>
        <pkt-badge class="bg-light-green">light-green</pkt-badge>
        <pkt-badge class="bg-lime">lime</pkt-badge>
        <pkt-badge class="bg-yellow">yellow</pkt-badge>
        <pkt-badge class="bg-amber">amber</pkt-badge>
        <pkt-badge class="bg-orange">orange</pkt-badge>
        <pkt-badge class="bg-deep-orange">deep-orange</pkt-badge>
        <pkt-badge class="bg-brown">brown</pkt-badge>
        <pkt-badge class="bg-grey">grey</pkt-badge>
        <pkt-badge class="bg-blue-grey">blue-grey</pkt-badge>
    </div>
</div>

### Theme color pallete

<div id="theme-alt" style="text-align: center; margin-top: 2rem;">
    <button class="bg-a1">A1</button>
    <button class="bg-p">P</button>
    <button class="bg-a2">A2</button>
    <button class="bg-t1">T1</button>
    <button class="bg-c">C</button>
    <button class="bg-t2">T2</button>
</div>

You can easily generate color pallete and user interface with configuration.

```scss
@forward 'path/to/_theme.scss' with (
    $-pallete: (
        color-primary: #2196F3,
        hue-distance: 20,
    )
);
```

### Modular user interface

Written in Javascript **ES6** and **SASS**, you can easily pick and manage
components to make them compact and fast.

```javascript
import * as ui from 'packet-ui';

customElements.define('pkt-progress-bar', ui.ProgressBar);
```