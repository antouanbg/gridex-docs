import React from 'react';
import OriginalFooter from '@theme-original/DocItem/Footer';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function DocItemFooter(): React.JSX.Element {
  const {i18n} = useDocusaurusContext();
  const en = i18n.currentLocale === 'en';
  return (
    <>
      <div className="gridex-doc-help-strip">
        <div><span>{en ? 'NEXT STEP' : 'СЛЕДВАЩА СТЪПКА'}</span><strong>{en ? 'Ready to open GrideX?' : 'Готови ли сте да отворите GrideX?'}</strong></div>
        <a href="https://gridex.tech/">{en ? 'Go to the portal' : 'Към портала'} <span aria-hidden="true">↗</span></a>
      </div>
      <OriginalFooter />
    </>
  );
}
