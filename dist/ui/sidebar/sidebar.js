import {html, render} from 'lit-html';

export class Sidebar extends HTMLElement {
    constructor() {
        super();
        if (typeof this.getAttribute('show') === 'undefined') {
            return;
        }
        this.el = {};
        this.el.sidebar = null;
        this.el.overlay = null;
    }

    template() {
        let sidebar = this.querySelector('[el="sidebar"]')
            || html`<div el="sidebar">`;
        let overlay = this.querySelector('[el="overlay"]')
            || html`<div el="overlay">`;
        return html`
            ${sidebar}
            ${overlay}
        `
    }

    render() {
        render(this.template(), this);
        this.el.sidebar = this.querySelector('[el="sidebar"]');
        this.el.overlay = this.querySelector('[el="overlay"]');
        this.el.overlay.addEventListener('click', () => {
            this.hide_sidebar();
        })
    }

    connectedCallback() {
        this.render();
        let media_query = '(min-width: ' + this.getAttribute('show') + ')';
        this.media_query = window.matchMedia(media_query);
        if (this.media_query.matches) {
            setTimeout(() => {
                this.show_sidebar_no_overlay()
            }, 0)
        }
        this.media_query.addEventListener("change", () => {
            this.media_change();
        })
    }

    media_change() {
        if (this.media_query.matches) {
            this.show_sidebar_no_overlay();
        } else {
            this.hide_sidebar();
        }
    }

    show_sidebar() {
        this.el.sidebar.classList.add('show');
        this.el.overlay.classList.add('show');
    }

    show_sidebar_no_overlay() {
        this.el.sidebar.classList.add('show');
        this.el.overlay.classList.remove('show');
    }

    hide_sidebar() {
        this.el.sidebar.classList.remove('show');
        this.el.overlay.classList.remove('show');
    }
}