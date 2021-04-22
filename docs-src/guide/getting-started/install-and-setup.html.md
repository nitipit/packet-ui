# Install and Setup

## NPM
---
Installing **Packet UI** by **npm** is better option if you want to use **ES6** modules and customize UI styles by **SASS**

```
$ npm install packet-ui
```
Pakcage will be installed at `node_modules/pakcet-ui/`.

## Simple setup
---
The most simple setup can be done by including codes much like as described in
[Quick start](./quick-start.html) section. Just place files below
to directory where web server can access. 
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
</head>
```

## Usage
---
Now **Packet UI Components** are ready. You can look through documents in **UI Components** section and use them in HTML. For example,

```
<pkt-input-number></pkt-input-number>
```

<pkt-input-number></pkt-input-number>