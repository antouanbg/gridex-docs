// Public documentation only. Never place private runbooks, credentials or device addresses here.
const config = {
  title: 'GrideX · Документация',
  tagline: 'Практично ръководство за GrideX Energy OS',
  url: 'https://doc.gridex.tech',
  baseUrl: '/',
  favicon: 'img/favicon.svg',
  onBrokenLinks: 'throw',
  markdown: { hooks: { onBrokenMarkdownLinks: 'throw' } },
  i18n: { defaultLocale: 'bg', locales: ['bg', 'en'], localeConfigs: { bg: { label: 'Български', htmlLang: 'bg-BG' }, en: { label: 'English', htmlLang: 'en-GB' } } },
  presets: [[ 'classic', {
    docs: { routeBasePath: '/', sidebarPath: require.resolve('./sidebars.js'), editUrl: undefined },
    blog: false,
    theme: { customCss: require.resolve('./src/css/custom.css') },
  } ]],
  themeConfig: {
    colorMode: { defaultMode: 'light', disableSwitch: true },
    navbar: { title: 'GrideX', logo: { alt: 'GrideX', src: 'img/favicon.svg' }, items: [
      { type: 'docSidebar', sidebarId: 'mainSidebar', position: 'left', label: 'Ръководство' },
      { href: 'https://gridex.tech/', label: 'Към портала ↗', position: 'right' },
      { type: 'localeDropdown', position: 'right' },
    ] },
    footer: { style: 'dark', links: [{ title: 'GrideX', items: [{ label: 'Портал', href: 'https://gridex.tech/' }] }], copyright: `© ${new Date().getFullYear()} GrideX` },
  },
};
module.exports = config;
