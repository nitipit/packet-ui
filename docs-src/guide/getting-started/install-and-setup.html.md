# Install and Setup

## NPM
---
Installing **Packet UI** by **npm** is better option if you want to use **ES6** modules and customize UI styles by **SASS**

```
npm install packet-ui
```
Pakcage will be installed at `node_modules/pakcet-ui/` with directory tree as follows.

```
.
├── dist/
│   ├── font/
│   ├── normalize.css
│   ├── normalize.css.map
│   ├── packet-ui.css
│   ├── packet-ui.css.map
│   ├── packet-ui.js
│   ├── packet-ui.js.map
│   ├── style/
│   └── ui/
├── LICENSE
├── package.json
├── readme.md
```

## Simple setup
---
The most simple setup can be done by including codes like in [Quick start](./quick-start.html) section. Just place files below to directory where web server can access. 
```
1. dist/normailize.css
2. dist/packet-ui.css
3. dist/packet-ui.js
4. dist/font/Cantarell-Regular.ttf
```

Then, put codes below in HTML <head> section. 

```
<head>
    <!-- Load default CSS -->
    <link rel="stylesheet" href="//to/normalize.css">
    <link rel="stylesheet" href="//to/packet-ui.css">

    <!-- Load packet-ui.js -->
    <script defer src="//to/packet-ui.js"></script>

    <!-- Set up font for UI components. Cantarell is recommended -->
    <style>
    @font-face {
        font-family: 'packet-ui';
        src: url('//to/Cantarell-Regular.ttf');
    }
    </style>
</head>
```

## Usage
---
Now **Packet UI Components** are ready. You can look through documents in **UI Components** section and use them in HTML. For example,

```
<pkt-input-number></pkt-input-number>
```

<pkt-input-number></pkt-input-number>