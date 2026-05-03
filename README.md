# graziul.github.io

Personal site for Christopher M. Graziul — narrative hub linking to
[Graziul Advisory](https://graziul.io) and the [Illinois Data Equity
Project](https://idep.org).

## Stack

- [Hugo](https://gohugo.io/) (extended)
- [Wowchemy / Hugo Academic Theme](https://wowchemy.com/) v5 — open-source academic site framework by George Cushen
- Hosted on Netlify, auto-deployed from `master`

## Local development

```sh
hugo server --bind 127.0.0.1 --port 1313
```

Then open http://localhost:1313/.

## Content

```
content/_index.md             home page
content/about/                bio narrative
content/self-organizing/      CRHQ/CEDR, ICML, IDEP recipe
content/academic-research/    policing research + broader arc
content/publications/         full publication list
config/_default/              site config (params, menus, languages)
assets/scss/custom.scss       theme overrides + custom components
layouts/                      local overrides of Wowchemy partials
```

## License

Site content © Chris Graziul, [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
Theme code is licensed under the upstream Wowchemy MIT license.
