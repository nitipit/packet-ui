import hljs from 'highlight.js/lib/core.js';
import xml from 'highlight.js/lib/languages/xml.js';
import javascript from 'highlight.js/lib/languages/javascript.js';
import css from 'highlight.js/lib/languages/css.js';
import scss from 'highlight.js/lib/languages/scss.js';
import shell from 'highlight.js/lib/languages/shell.js';

hljs.registerLanguage('html', xml);
hljs.registerLanguage('javascript', javascript);
hljs.registerLanguage('css', css);
hljs.registerLanguage('scss', scss);
hljs.registerLanguage('shell', shell);
hljs.highlightAll();