# Style with SASS

This is the most important feature to customize UI and Color theme.

Let's look into more details in **Packet UI** directory `dist/` which provides **SASS** files for customization.

```
dist/
├── style/ # Overall (Theme) styles for components
│   ├── _mixin.scss
│   └── _var.scss
└── ui/ # <web-component/> Javascript and SASS
```

`style/` contains SASS variables and mixins which can be considered as **Theme** style. All SASS file in `dist/ui/` use these mixins and variables to build each UI Components.