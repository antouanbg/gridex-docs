import React from 'react';

type GuideNoticeProps = {
  label: string;
  children: React.ReactNode;
  tone?: 'green' | 'amber';
};

export default function GuideNotice({label, children, tone = 'green'}: GuideNoticeProps): React.JSX.Element {
  return (
    <aside className={`gridex-guide-notice gridex-guide-notice--${tone}`}>
      <span aria-hidden="true" className="gridex-guide-notice__mark">{tone === 'green' ? '●' : '!'}</span>
      <div><strong>{label}</strong><div>{children}</div></div>
    </aside>
  );
}
