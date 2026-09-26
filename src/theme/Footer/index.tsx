import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function Footer(): React.JSX.Element {
  const {i18n} = useDocusaurusContext();
  const en = i18n.currentLocale === 'en';
  return (
    <footer className="gridex-doc-footer">
      <div className="gridex-doc-footer__inner">
        <div>
          <a className="gridex-doc-footer__brand" href="https://gridex.tech/" aria-label="GrideX Energy OS">G<span>ri</span>deX</a>
          <p>{en ? 'Clear guidance for live energy operations.' : 'Ясни указания за работа с реални енергийни обекти.'}</p>
        </div>
        <nav aria-label={en ? 'Documentation footer' : 'Навигация в документацията'}>
          <a href={en ? '/en/' : '/'}>{en ? 'Documentation' : 'Документация'}</a>
          <a href={en ? '/en/organisations-and-access/' : '/organisations-and-access/'}>{en ? 'Access & roles' : 'Покани и права'}</a>
          <a href="https://gridex.tech/">{en ? 'GrideX portal ↗' : 'Портал GrideX ↗'}</a>
        </nav>
      </div>
      <div className="gridex-doc-footer__bottom">© {new Date().getFullYear()} GrideX <span>{en ? 'Public guide · Illustrative images' : 'Публично ръководство · Илюстративни изображения'}</span></div>
    </footer>
  );
}
