import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

type GuideCardProps = {
  number: string;
  label: string;
  title: string;
  description: string;
  href: string;
  action: string;
  pending?: boolean;
};

export default function GuideCard({number, label, title, description, href, action, pending = false}: GuideCardProps): React.JSX.Element {
  const {i18n} = useDocusaurusContext();
  const resolvedHref = href.startsWith('./') ? `${i18n.currentLocale === 'en' ? '/en' : ''}/${href.slice(2)}` : href;
  return (
    <a className={`gridex-guide-card ${pending ? 'gridex-guide-card--pending' : ''}`} href={resolvedHref}>
      <span className="gridex-guide-card__number">{number}</span>
      <span className="gridex-guide-card__label">{label}</span>
      <strong>{title}</strong>
      <span className="gridex-guide-card__description">{description}</span>
      <span className="gridex-guide-card__action">{action} <span aria-hidden="true">↗</span></span>
    </a>
  );
}
