import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

type DocsHeroProps = {
  eyebrow: string;
  title: string;
  description: string;
  imageAlt: string;
  primaryHref: string;
  primaryLabel: string;
  secondaryHref?: string;
  secondaryLabel?: string;
  compact?: boolean;
};

export default function DocsHero({
  eyebrow,
  title,
  description,
  imageAlt,
  primaryHref,
  primaryLabel,
  secondaryHref,
  secondaryLabel,
  compact = false,
}: DocsHeroProps): React.JSX.Element {
  const {i18n} = useDocusaurusContext();
  const localHref = (href: string): string => href.startsWith('./')
    ? `${i18n.currentLocale === 'en' ? '/en' : ''}/${href.slice(2)}`
    : href;
  return (
    <section className={`gridex-doc-hero ${compact ? 'gridex-doc-hero--compact' : ''}`}>
      <img className="gridex-doc-hero__image" src="/img/solar-hero.jpg" alt={imageAlt} />
      <div className="gridex-doc-hero__content">
        <span className="gridex-doc-hero__eyebrow"><i aria-hidden="true" />{eyebrow}</span>
        <h1>{title}</h1>
        <p>{description}</p>
        <div className="gridex-doc-hero__actions">
          <a className="gridex-doc-button gridex-doc-button--primary" href={localHref(primaryHref)}>{primaryLabel}<span aria-hidden="true">↗</span></a>
          {secondaryHref && secondaryLabel && (
            <a className="gridex-doc-button gridex-doc-button--ghost" href={localHref(secondaryHref)}>{secondaryLabel}</a>
          )}
        </div>
      </div>
    </section>
  );
}
