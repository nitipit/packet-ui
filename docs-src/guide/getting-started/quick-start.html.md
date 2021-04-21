# Quick start using CDN
---

To use default style and color, just put codes below in html `<head>` and you're good to go.

```html
<head>
    <!-- Load default CSS -->
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/packet-ui@2.0.0/dist/normalize.css">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/packet-ui@2.0.0/dist/packet-ui.css">

    <!-- Load packet-ui.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/packet-ui@2.0.0/dist/packet-ui.js"></script>
</head>
```

Then, use web components `<pkt-*>` anywhere in html `<body>`, for examples:

```html
<body>
    <pkt-badge>1</pkt-badge>
    <pkt-switch></pkt-switch>
</body>
```

<pkt-badge style="vertical-align: middle;">1</pkt-badge>
<pkt-switch style="margin-left: 1rem;"></pkt-switch>

See more components in **UI Components** section.