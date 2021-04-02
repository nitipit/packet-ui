import { html, render } from 'lit-html'

export class Edge extends HTMLElement {
    constructor() {
        super();
    }

    template() {

    }

    render() {
        render(this.template, this);
    }

    connectedCallback() {
        this.render();
    }
}
