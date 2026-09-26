// Public-facing content only. This site serves gridex.tech users, not private operators.
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'GrideX · Документация',
  tagline: 'Практично ръководство за GrideX Energy OS',
  url: 'https://doc.gridex.tech',
  baseUrl: '/',
  favicon: 'img/favicon.svg',
  onBrokenLinks: 'throw',
  markdown: {hooks: {onBrokenMarkdownLinks: 'throw'}},
  i18n: {
    defaultLocale: 'bg',
    locales: ['bg', 'en'],
    localeConfigs: {
      bg: {label: 'Български', htmlLang: 'bg-BG'},
      en: {label: 'English', htmlLang: 'en-GB'},
    },
  },
  presets: [
    [
      'classic',
      {
        docs: {routeBasePath: '/', sidebarPath: './sidebars.js'},
        blog: false,
        theme: {customCss: './src/css/custom.css'},
      } satisfies Preset.Options,
    ],
  ],
  themeConfig: {
    colorMode: {defaultMode: 'light', disableSwitch: true},
    navbar: {
      title: 'GrideX',
      logo: {alt: 'GrideX', src: 'img/favicon.svg'},
      items: [
        {type: 'docSidebar', sidebarId: 'mainSidebar', position: 'left', label: 'Ръководство'},
        {href: 'https://gridex.tech/', label: 'Към портала ↗', position: 'right'},
        {type: 'localeDropdown', position: 'right'},
      ],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
